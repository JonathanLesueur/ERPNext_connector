import requests
from erpnext_connector.services.gitlab.gitlab_settings import get_gitlab_settings
# -----------------------------
# Utilitaire générique pour appeler l'API GitLab
# -----------------------------
def gitlab_request(method, endpoint, data=None, params=None):
    settings = get_gitlab_settings()
    if not settings:
        frappe.throw(_("GitLab n'est pas configuré ou est désactivé."))

    headers = {"PRIVATE-TOKEN": settings["token"]}
    url = f"{settings['url']}/api/v4/{endpoint}"

    r = requests.request(method, url, headers=headers, json=data, params=params)
    r.raise_for_status()
    return r.json()