import frappe
from frappe import _

def custom_install():
     create_custom_fields()


def create_custom_fields():
    custom_fields = [
        {
            "fieldname":"gitlab_tab",
            "label": "Gitlab",
            "fieldtype": "Tab Break",
            "dt": "Project",
            "insert_after": "to_time"
        },
        {
            "fieldname":"projets_gitlab",
            "label": "Gitlab Projects",
            "fieldtype": "Table",
            "options":"Gitlab Project ERPNext",
            "dt": "Project",
            "insert_after": "gitlab_tab"
        },
        {
            "fieldname":"custom_drive",
            "label": "Drive",
            "fieldtype": "Tab Break",
            "dt": "Project",
            "insert_after": "projets_gitlab"
        }
        {
            "fieldname": "custom_create_drive_space",
            "label": "Create Drive Space",
            "fieldtype": "Check",
            "dt": "Project",
            "insert_after": "drive_tab"
        },
        {
            "fieldname": "project_reference",
            "label": "Project Reference",
            "fieldtype": "Link",
            "options": "Project",
            "dt": "Drive Team",
            "insert_after": "title"
        }
    ]

    for field in custom_fields:
        if frappe.db.exists("Custom Field", {
            "dt": field["dt"],
            "fieldname": field["fieldname"]
        }):
            print(_("Custom field '{0}' already exists in '{1}', skipping.").format(field["fieldname"], field["dt"]))
            continue

        try:
            frappe.get_doc({
                "doctype": "Custom Field",
                "dt": field["dt"],
                "fieldname": field["fieldname"],
                "fieldtype": field["fieldtype"],
                "options": field.get("options", ""),
                "label": field.get("label"),
                "insert_after": field.get("insert_after"),
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
            }).insert()
            print(_("Custom field '{0}' inserted.").format(field['fieldname']))
        except frappe.DuplicateEntryError:
                print(_("Duplicate detected for '{0}', skipping insertion.").format(field['fieldname']))
    frappe.db.commit()