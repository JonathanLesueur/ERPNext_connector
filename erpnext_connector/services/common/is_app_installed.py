import frappe
from frappe import _

def is_app_installed(app_name: str) -> bool:
    """Check if a Specific App is installed"""
    return app_name in frappe.get_installed_apps()

def is_erpnext_installed() -> bool:
    """Check if ERPNext is installed"""
    return "erpnext" in frappe.get_installed_apps()

def is_drive_installed() -> bool:
    """Check if Frappe Drive is installed"""
    return "drive" in frappe.get_installed_apps()

def is_gameplan_installed() -> bool:
    """Check if Frappe Gameplan is installed"""
    return "gameplan" in frappe.get_installed_apps()

def is_helpdesk_installed() -> bool:
    """Check if Frappe Helpdesk is installed"""
    return "helpdesk" in frappe.get_installed_apps()

def is_wiki_installed() -> bool:
    """Check if Frappe Wiki is installed"""
    return "helpdesk" in frappe.get_installed_apps()

def is_lms_installed() -> bool:
    """Check if Frappe Learning is installed"""
    return "helpdesk" in frappe.get_installed_apps()