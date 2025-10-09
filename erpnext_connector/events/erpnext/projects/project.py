import frappe
from frappe import _
from frappe.utils import cstr
from frappe.utils import cint

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

def on_update(doc, method):
    """
    Create or update a Frappe Drive Team when a Project is created or updated
    Args:
        doc: Project Document
        method: on_update
    """
    if cint(doc.custom_create_drive_space):
        try:
            # Check if Drive Team already exists
            team_exists = frappe.db.exists(
                "Drive Team",
                {"project_reference": doc.name}
            )

            if not team_exists:
                # Create new Drive Team
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
                
                # Get project users and add them to team
                project_users = get_project_users(doc.name)
                for user in project_users:
                    access_level = 1
                    if doc.owner == user:
                        access_level = 2
                    team.append("users", {
                        "user": user,
                        "access_level": access_level
                    })
                    
                team.insert(ignore_permissions=True)
                
                # Create default folders after team creation
                create_default_folders(team.name)
                
                frappe.msgprint(
                    msg=_("Frappe Drive Team created for project {0} with {1} members and default folders").format(
                        doc.project_name, len(project_users)
                    ),
                    alert=True
                )
            else:
                # Update existing team members
                team = frappe.get_doc("Drive Team", {"project_reference": doc.name})
                current_members = [member.user for member in team.members]
                project_users = get_project_users(doc.name)
                
                # Add new members
                for user in project_users:
                    if user not in current_members:
                        team.append("members", {
                            "user": user,
                            "role": "Editor"
                        })
                
                # Remove members who are no longer in the project
                team.members = [member for member in team.members if member.user in project_users]
                
                team.save(ignore_permissions=True)
                
        except Exception as e:
            frappe.log_error(
                title="Error in Project Drive Team Creation/Update",
                message=f"Failed to manage Drive Team for project {doc.name}: {cstr(e)}"
            )
            frappe.throw(
                _("Could not manage Drive Team: {0}").format(str(e))
            )