import frappe
from frappe import _
from frappe.utils import cstr, cint

from erpnext_connector.services.common.is_app_installed import is_drive_installed, is_gameplan_installed, is_helpdesk_installed, is_wiki_installed, is_lms_installed
from erpnext_connector.services.drive.team_service import create_drive_team, update_drive_team
from erpnext_connector.services.erpnext.project.project_service import get_project_users
from erpnext_connector.services.wiki.space_service import create_wiki_project_space
from erpnext_connector.services.wiki.page_service import create_base_pages_for_space

def handle_wiki_integration(doc):
    """Handle Wiki Space creation when a project is created"""
    #try:
    space_exists = frappe.db.exists("Wiki Space", {"space_name": doc.project_name})
    if not space_exists:
        projects_space = create_wiki_project_space(doc)
    else:
        projects_space = frappe.get_doc("Wiki Space", {"space_name": doc.project_name})
    
    create_base_pages_for_space(doc, projects_space)

    #if not projects_space:
    #    frappe.throw(_("Wiki Space creation is disabled in Wiki Settings."))
    #except Exception as e:
    #    frappe.log_error(
    #        title="Error in Project Wiki Space Creation",
    #        message=_("Failed to create Wiki Global Space for projects.")
    #    )
    #    frappe.throw(
    #        _("Could not create Wiki Space")
    #    )

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
            message=_("Failed to manage Drive Team '{0}' for project: {1}.").format(doc.name, cstr(e))
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
        if cint(doc.custom_create_wiki_space):
            handle_wiki_integration(doc)
    
    # Future integrations can be added here