import frappe
from frappe import _


def create_custom_field(field: object):
    """Create a custom field if it does not exist"""
    if not frappe.db.exists("Custom Field", {"dt": field["dt"], "fieldname": field["fieldname"]}):
        cf = frappe.get_doc({
            "doctype": "Custom Field",
            "unique": field.get("unique", 0),
            "hidden": field.get("hidden", 0),
            "read_only": field.get("read_only", 0),
            "in_list_view": field.get("in_list_view", 0),
            "reqd": field.get("reqd", 0),
            "no_copy": field.get("no_copy", 0),
            "bold": field.get("bold", 0),
            "translatable": field.get("translatable", 0),
            "allow_in_quick_entry": field.get("allow_in_quick_entry", 0),
            "allow_on_submit": field.get("allow_on_submit", 0),
            **field
        })
        cf.insert(ignore_permissions=True)
        frappe.db.commit()
        print(_("Custom field '{0}' created in '{1}'").format(field["fieldname"], field["dt"]))
        return field
    else:
        print(_("Custom field '{0}' already exists in '{1}', skipping.").format(field["fieldname"], field["dt"]))
    
    return None