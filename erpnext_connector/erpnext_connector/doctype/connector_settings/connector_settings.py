# Copyright (c) 2025, Jonathan Lesueur and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

from erpnext_connector.setup.custom_fields.custom_fields import drive_fields
from erpnext_connector.services.common.is_app_installed import is_app_installed

class ConnectorSettings(Document):
    def validate(self):
        self.handle_drive_fields()
    
    def handle_drive_fields(self):
        """Create or remove Drive custom fields based on connection status"""
        if self.enable_drive_connection:
            self.create_drive_custom_fields()
        #else:
        #    self.remove_drive_custom_fields()
    
    def create_drive_custom_fields(self):
        """Create Drive-related custom fields"""
        custom_fields = drive_fields
        
        for field in custom_fields:
            if not frappe.get_meta(field["dt"]).has_field(field["fieldname"]):
                custom_field = frappe.get_doc({
                    "doctype": "Custom Field",
                    "dt": field["dt"],
                    "fieldname": field["fieldname"],
                    "label": field["label"],
                    "fieldtype": field["fieldtype"],
                    "insert_after": field["insert_after"],
                    "options": field.get("options"),
                })
                custom_field.insert(ignore_permissions=True)
                frappe.msgprint(_(f"Created custom field {field['fieldname']} in {field['dt']}"))
    
    def remove_drive_custom_fields(self):
        """Remove Drive-related custom fields"""
        custom_fields = drive_fields
        
        for field in custom_fields:
            custom_field = frappe.db.exists("Custom Field", {
                "dt": field["dt"],
                "fieldname": field["fieldname"]
            })
            if custom_field:
                frappe.delete_doc("Custom Field", custom_field, ignore_permissions=True)
                frappe.msgprint(_(f"Removed custom field {field['fieldname']} from {field['dt']}"))

@frappe.whitelist()
def check_app_installed(app_name: str) -> bool:
    """Check if an app is installed without permission restrictions"""
    return is_app_installed(app_name)