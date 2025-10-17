import frappe
from frappe import _
from frappe.model.document import Document

from erpnext_connector.services.drive.folder_service import create_default_folders

def create_drive_team(doc: Document, project_users: list) -> Document:
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
        msg=_("Frappe Drive Team created for project '{0}' with '{1}' members and default folders").format(
            doc.project_name, len(project_users)
        ),
        alert=True
    )
    
    return team

def update_drive_team(team: Document, doc: Document, project_users: list):
    """Update an existing Drive Team"""
    if team.title != doc.project_name:
        team.title = doc.project_name
        
    update_team_members(team, project_users, doc.owner)
    team.save(ignore_permissions=True)
    
    frappe.msgprint(
        msg=_("Drive Team members updated."),
        alert=True
    )
    
    if team.title == doc.project_name:
        frappe.msgprint(
            msg=_("Drive Team name updated to '{0}'.").format(doc.project_name),
            alert=True
        )


def add_members_to_team(team: Document, users: list, owner: Document):
    """Add members to a Drive Team"""
    for user in users:
        access_level = 2 if user == owner else 1
        team.append("users", {
            "user": user,
            "access_level": access_level
        })

def update_team_members(team: Document, project_users: list, owner: Document):
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
