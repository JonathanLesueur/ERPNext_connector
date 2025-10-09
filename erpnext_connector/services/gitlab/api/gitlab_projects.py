import requests
import frappe
from frappe import _
from erpnext_connector.services.gitlab.gitlab_request import gitlab_request

def gitlab_get_projects():
    """Récupérer les projets GitLab de l'utilisateur"""
    return gitlab_request("GET", "projects", params={"membership": True})

# -----------------------------
# Fonction de synchronisation ERPNext
# -----------------------------

def sync_gitlab_projects():
    """Créer ou mettre à jour les projets dans le Doctype 'Gitlab Project'"""
    projects = gitlab_get_projects()

    for proj in projects:
        if not frappe.db.exists("Gitlab Project", {"project_id": proj["id"]}):
            doc = frappe.get_doc({
                "doctype": "Gitlab Project",
                "project_id": proj["id"],
                "name1": proj["name"],  # ⚠️ 'name' est réservé
                "description": proj.get("description"),
                "web_url": proj.get("web_url"),
            })
            doc.insert(ignore_permissions=True)
        else:
            frappe.db.set_value(
                "Gitlab Project",
                {"project_id": proj["id"]},
                {
                    "name1": proj["name"],
                    "description": proj.get("description"),
                    "web_url": proj.get("web_url"),
                },
            )

    frappe.db.commit()
