import frappe
from frappe import _

from frappe.model.document import Document

def create_wiki_project_space(doc: Document) -> Document:
    """Create a Wiki Space for a project"""
    space_settings = frappe.get_single("Wiki Settings")
    if not space_settings:
        return None
    
    space = frappe.get_doc({
        "doctype": "Wiki Space",
        "space_name": doc.project_name,
        "route": f"wiki/{doc.project_name.replace(' ', '-').lower()[:10]}",
        "owner": doc.owner
    })
    space.insert(ignore_permissions=True)

    space_settings.append("app_switcher_list", {
        "app_title": doc.project_name,
        "wiki_space": space
    })

    space_settings.save(ignore_permissions=True)

    frappe.msgprint(
        msg=_("Wiki Space for project '{0}' has been created.").format(doc.project_name),
        alert=True
    )

    return space

def update_sidebar_for_space(space: Document, page: Document, group: Document):
    """Add page to the sidebar of the Wiki Space""" 
    space.append("wiki_sidebars", {
        "wiki_page": page,
        "parent_label": group['title']
    })
    space.save(ignore_permissions=True)

def update_navbar_for_space(space: Document):
    """Add menus to the top navbar of the Wiki Space""" 

    menus = [
        {
            "title": "Gitlab",
            "url": "https://git.softia.fr",
            "right": 1,
            "open_in_new_tab": 1
        }
    ]

    for menu in menus:
        space.append("navbar_items", {
            "label": menu['title'],
            "url": menu['url'],
            "right": menu['right'],
            "open_in_new_tab": menu['open_in_new_tab']
        })
    space.save(ignore_permissions=True)