import frappe
from frappe import _

def is_drive_installed():
    """Check if Frappe Drive is installed"""
    return "drive" in frappe.get_installed_apps()

def is_gameplan_installed():
    """Check if Frappe Gameplan is installed"""
    return "gameplan" in frappe.get_installed_apps()

def is_helpdesk_installed():
    """Check if Frappe Helpdesk is installed"""
    return "helpdesk" in frappe.get_installed_apps()

def is_wiki_installed():
    """Check if Frappe Helpdesk is installed"""
    return "helpdesk" in frappe.get_installed_apps()

def is_lms_installed():
    """Check if Frappe Helpdesk is installed"""
    return "helpdesk" in frappe.get_installed_apps()