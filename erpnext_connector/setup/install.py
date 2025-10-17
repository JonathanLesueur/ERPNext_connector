import frappe
from frappe import _
from erpnext_connector.services.common.is_app_installed import is_app_installed
from erpnext_connector.services.common.custom_fields import create_custom_field
from erpnext_connector.setup.custom_fields.custom_fields import erpnext_fields, drive_fields, helpdesk_fields, lms_fields, gameplan_fields, wiki_fields, gitlab_fields

def custom_install():
     create_custom_fields()


def create_custom_fields():
    custom_fields = erpnext_fields + drive_fields + helpdesk_fields + lms_fields + gameplan_fields + wiki_fields + gitlab_fields

    for field in custom_fields:
        if not is_app_installed(field["application"]):
            print(_("Application '{0}' is not installed. Skipping custom field '{1}' creation.").format(field["application"], field["label"]))
            continue
        if frappe.db.exists("Custom Field", {
            "dt": field["dt"],
            "fieldname": field["fieldname"]
        }):
            print(_("Custom field '{0}' already exists in '{1}', skipping.").format(field["fieldname"], field["dt"]))
            continue

        try:
            if not is_app_installed(field["application"]):
                continue
            create_custom_field(field)

        except frappe.DuplicateEntryError:
                print(_("Duplicate detected for '{0}', skipping insertion.").format(field['fieldname']))
    frappe.db.commit()