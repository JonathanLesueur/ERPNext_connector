erpnext_fields = [

]

drive_fields = [
    {
        "fieldname": "custom_drive",
        "label": "Drive",
        "fieldtype": "Tab Break",
        "dt": "Project",
        "insert_after": "projets_gitlab",
        "application": "erpnext"
    },
    {
        "fieldname": "custom_create_drive_space",
        "label": "Create Drive Space",
        "fieldtype": "Check",
        "dt": "Project",
        "insert_after": "drive_tab",
        "application": "erpnext"
    },
    {
        "fieldname": "project_reference",
        "label": "Project Reference",
        "fieldtype": "Link",
        "options": "Project",
        "dt": "Drive Team",
        "insert_after": "title",
        "application": "drive"
    }
]

helpdesk_fields = []

lms_fields = []

gameplan_fields = []

wiki_fields = [
    {
        "fieldname": "custom_wiki",
        "label": "Wiki",
        "fieldtype": "Tab Break",
        "dt": "Project",
        "insert_after": "custom_create_drive_space",
        "application": "erpnext"
    },
    {
        "fieldname": "custom_create_wiki_space",
        "label": "Create Wiki Space",
        "fieldtype": "Check",
        "dt": "Project",
        "insert_after": "wiki_tab",
        "application": "erpnext"
    }
]

gitlab_fields = [
    {
        "fieldname": "gitlab_tab",
        "label": "Gitlab",
        "fieldtype": "Tab Break",
        "dt": "Project",
        "insert_after": "to_time",
        "application": "erpnext"
    },
    {
        "fieldname": "projets_gitlab",
        "label": "Gitlab Projects",
        "fieldtype": "Table",
        "options": "Gitlab Project ERPNext",
        "dt": "Project",
        "insert_after": "gitlab_tab",
        "application": "erpnext"
    }
]