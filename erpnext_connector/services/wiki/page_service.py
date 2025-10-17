import frappe
from frappe import _
from frappe.utils import cstr
from frappe.model.document import Document

from erpnext_connector.modeles.wiki.wiki_pages import presentation_projet, equipes_contacts
from erpnext_connector.services.wiki.space_service import update_sidebar_for_space, update_navbar_for_space

def create_base_pages_for_space(doc: Document, space: Document):
    groups = [
        {
            "title": "Définition",
            "pages": [
                {
                    "title": "Présentation du projet",
                    "content": presentation_projet
                },
                {
                    "title": "Equipe & Contacts",
                    "content": equipes_contacts
                }
            ]
        }
    ]

    try:
        for group in groups:
            for page in group['pages']:
            
                wiki_page = frappe.get_doc({
                    "doctype": "Wiki Page",
                    "title": page["title"],
                    "content": page["content"],
                    "route": f"{space.route}/{page['title'].replace(' ', '-').lower()}",
                    "published": 1,
                    "allow_guest": 0
                })
                wiki_page.insert(ignore_permissions=True)
                update_sidebar_for_space(space, wiki_page, group)
        
        update_navbar_for_space(space)

        frappe.msgprint(
            msg=_("Default Wiki pages has been created for project '{0}'.").format(doc.project_name),
            alert=True
        )
    except Exception as e:
        frappe.log_error(
            title="Error in creating base wiki pages",
            message=f"Failed to create base wiki pages for space '{space.space_name}': {cstr(e)}"
        )
        raise e
