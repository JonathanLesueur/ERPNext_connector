import frappe
from frappe import _

def get_project_users(project_name: str) -> list:
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
  
