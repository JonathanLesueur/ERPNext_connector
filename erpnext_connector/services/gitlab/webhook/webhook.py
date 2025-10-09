import frappe
import json

@frappe.whitelist(allow_guest=True)
def gitlab_webhook():
    """Endpoint pour recevoir les webhooks GitLab"""
    # Vérifier que c’est une requête POST
    if frappe.request.method != "POST":
        frappe.throw("Method not allowed", frappe.MethodNotAllowedError)
    token = frappe.get_request_header("X-Gitlab-Token")
    expected = frappe.db.get_single_value("GitLab Settings", "gitlab_webhook_secret")
    if token != expected:
        frappe.throw("Invalid GitLab Token", frappe.AuthenticationError)

    event = frappe.get_request_header("X-Gitlab-Event")
    payload = frappe.request.get_data(as_text=True)
    data = json.loads(payload)

    frappe.get_logger("gitlab").info(f"GitLab event {event}: {payload}")

    # Exemple : si merge request
    if event == "Merge Request Hook":
        title = data["object_attributes"]["title"]
        url = data["object_attributes"]["url"]
        # Créer une Issue dans ERPNext (ou Doctype custom)
        frappe.get_doc({
            "doctype": "Issue",
            "subject": f"MR: {title}",
            "description": url,
        }).insert(ignore_permissions=True)

    # Exemples pour d'autres événements à ajouter...
    return "ok"
