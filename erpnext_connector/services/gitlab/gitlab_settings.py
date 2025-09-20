import frappe

def get_gitlab_settings():
    """Récupère la configuration GitLab depuis le Doctype 'GitLab Settings'"""
    if not frappe.db.exists("GitLab Settings"):
        return None

    settings = frappe.get_doc("GitLab Settings")
    if not settings.enable_gitlab_connection:
        return None

    return {
        "url": settings.gitlab_site_url.rstrip("/"),   # on enlève le "/" final si présent
        "token": settings.gitlab_authentication_token
    }