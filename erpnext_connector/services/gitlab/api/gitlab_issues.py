import requests
import frappe
from frappe import _
from erpnext_connector.services.gitlab.gitlab_request import gitlab_request


def gitlab_get_issues(project_id=None):
    """Récupérer les issues GitLab (optionnellement d’un projet spécifique)"""
    endpoint = "issues" if not project_id else f"projects/{project_id}/issues"
    return gitlab_request("GET", endpoint)

def gitlab_create_issue(project_id, title, description=""):
    """Créer une issue dans un projet"""
    data = {"title": title, "description": description}
    return gitlab_request("POST", f"projects/{project_id}/issues", data=data)


