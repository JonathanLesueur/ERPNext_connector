import frappe
from frappe import _
from frappe.utils import cstr, cint
from erpnext_connector.services.common.is_app_installed import is_drive_installed, is_gameplan_installed, is_helpdesk_installed, is_wiki_installed, is_lms_installed


def get_project_users(project_name):
    """Get all users associated with a project"""
    users = []
    
    # Get users from Project Users child table
    project_users = frappe.get_all(
        "Project User",
        filters={"parent": project_name},
        fields=["user"]
    )
    users.extend([pu.user for pu in project_users])
    
    # Get Project Owner
    # project = frappe.get_doc("Project", project_name)
    #if project.owner and project.owner not in users:
    #    users.append(project.owner)
    
    return users

def create_default_folders(team_name):
    """Create default folder structure for a Drive Team"""
    try:
        main_folder = frappe.get_all(
            "Drive File",
            filters={
                "team": team_name,
                "is_group": 1
            },
            fields=["name"],
            limit=1
        )

        if main_folder:
            root_folders = [
                "Documents partagés",
                "Documents internes",
                "Attachments ERPNext"
            ]
            
            for folder_name in root_folders:
                folder = frappe.get_doc({
                    "doctype": "Drive File",
                    "is_group": "1",
                    "parent_entity": main_folder[0].name,
                    "team": team_name,
                    "title": folder_name,
                    "is_active": "1"
                })
                folder.insert(ignore_permissions=True)
                
            frappe.db.commit()
        
    except Exception as e:
        frappe.log_error(
            title="Error in creating default folders",
            message=f"Failed to create default folders for team {team_name}: {cstr(e)}"
        )
        raise e
    
def create_wiki_global_projects_space(doc):
    """Create a Wiki Space for the projects"""
    space = frappe.get_doc({
        "doctype": "Wiki Space",
        "space_name": "Projects",
        "route": "wiki/projects"
        "owner": doc.owner
    })
    space.insert(ignore_permissions=True)

    return space


def create_drive_team(doc, project_users):
    """Create a new Drive Team for a project"""
    team = frappe.get_doc({
        "doctype": "Drive Team",
        "title": doc.project_name,
        "project_reference": doc.name,
        "owner": doc.owner,
        "storage": 5120,
        "quota": 5120,
        "personal": 0,
        "description": f"Team for project: {doc.project_name}"
    })
    
    add_members_to_team(team, project_users, doc.owner)
    team.insert(ignore_permissions=True)
    
    create_default_folders(team.name)
    
    frappe.msgprint(
        msg=_("Frappe Drive Team created for project {0} with {1} members and default folders").format(
            doc.project_name, len(project_users)
        ),
        alert=True
    )
    
    return team

def update_drive_team(team, doc, project_users):
    """Update an existing Drive Team"""
    if team.title != doc.project_name:
        team.title = doc.project_name
        
    update_team_members(team, project_users, doc.owner)
    team.save(ignore_permissions=True)
    
    show_update_messages(team, doc.project_name)

def add_members_to_team(team, users, owner):
    """Add members to a Drive Team"""
    for user in users:
        access_level = 2 if user == owner else 1
        team.append("users", {
            "user": user,
            "access_level": access_level
        })

def update_team_members(team, project_users, owner):
    """Update members of an existing Drive Team"""
    current_members = [member.user for member in team.users]
    
    # Add new members
    for user in project_users:
        if user not in current_members:
            access_level = 2 if user == owner else 1
            team.append("users", {
                "user": user,
                "access_level": access_level
            })
    
    # Make sure owner is in the list
    if owner not in project_users:
        if owner not in current_members:
            team.append("users", {
                "user": owner,
                "access_level": 2
            })
        project_users.append(owner)
    
    # Remove members who are no longer in the project
    team.users = [member for member in team.users if member.user in project_users]

def show_update_messages(team, project_name):
    """Show update confirmation messages"""
    frappe.msgprint(
        msg=_("Drive Team members updated."),
        alert=True
    )
    
    if team.title == project_name:
        frappe.msgprint(
            msg=_("Drive Team name updated to {0}.").format(project_name),
            alert=True
        )


def create_base_pages_for_space(space):
    
    groups = [
        {"title": "Documentation", "pages": ["Guide de démarrage", "FAQ"]},
        {"title": "Ressources", "pages": ["Liens utiles", "Contacts"]},
        {"title": "Collaboration", "pages": ["Discussions", "Projets en cours"]}
    ]
    for group in groups:
    
        for page in group.pages:
           
            wiki_page = frappe.get_doc({
                "doctype": "Wiki Page",
                "title": page["title"],
                "content": page["content"],
                "route": f"wiki/{space.route}/{page['title'].replace(' ', '-').lower()}",
                "published": 1,
                "allow_guest": 0,
            })
            wiki_page.insert(ignore_permissions=True)

            update_sidebar_for_space(space, wiki_page, group)

def update_sidebar_for_space(space, page, group):
    """Add members to a Drive Team""" 
    space.append("wiki_sidebars", {
        "wiki_page": page.title,
        "parent_label": group.title
    })

def handle_wiki_integration(doc):
    """Handle Wiki Space creation when a project is created"""
    try:
        space_exists = frappe.db.exists("Wiki Space", {"title": "Projects"})
        if not space_exists:
            projects_space = create_wiki_global_projects_space(doc)
        else:
            projects_space = frappe.get_doc("Wiki Space", {"title": "Projects"})

        

    except Exception as e:
        frappe.log_error(
            title="Error in Project Wiki Space Creation",
            message=_("Failed to create Wiki Global Space for projects.")
        )
        frappe.throw(
            _("Could not create Wiki Space")
        )

def handle_drive_integration(doc):
    """Handle Drive Team creation and updates"""
    try:
        team_exists = frappe.db.exists(
            "Drive Team",
            {"project_reference": doc.name}
        )
        
        project_users = get_project_users(doc.name)
        
        if not team_exists:
            create_drive_team(doc, project_users)
        else:
            team = frappe.get_doc("Drive Team", {"project_reference": doc.name})
            update_drive_team(team, doc, project_users)
            
    except Exception as e:
        frappe.log_error(
            title="Error in Project Drive Team Creation/Update",
            message=_("Failed to manage Drive Team {0} for project: {1}.").format(doc.name, cstr(e))
        )
        frappe.throw(
            _("Could not manage Drive Team: {0}").format(str(e))
        )

def on_update(doc, method):
    """
    Handle Project updates and trigger necessary integrations
    Args:
        doc: Project Document
        method: on_update
    """
    if is_drive_installed():
        if cint(doc.custom_create_drive_space):
            handle_drive_integration(doc)

    if is_wiki_installed():
        handle_wiki_integration(doc)
    
    # Future integrations can be added here