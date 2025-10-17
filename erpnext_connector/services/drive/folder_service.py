import frappe
from frappe import _

def create_default_folders(team_name: str):
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
            message=f"Failed to create default folders for team '{team_name}': {cstr(e)}"
        )
        raise e
