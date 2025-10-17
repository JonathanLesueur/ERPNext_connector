// Copyright (c) 2025, Jonathan Lesueur and contributors
// For license information, please see license.txt

frappe.ui.form.on("Connector Settings", {
	refresh(frm) {
        frm.trigger("check_apps_installation");
    },

    check_apps_installation(frm) {
        const apps = [
            {name: 'drive', field: 'enable_drive_connection'},
            {name: 'wiki', field: 'enable_wiki_connection'},
            {name: 'helpdesk', field: 'enable_helpdesk_connection'},
            {name: 'gameplan', field: 'enable_gameplan_connection'},
            {name: 'lms', field: 'enable_learning_connection'}
        ];

        apps.forEach(app => {
            frappe.call({
                method: 'erpnext_connector.erpnext_connector.doctype.connector_settings.connector_settings.check_app_installed',
                args: {
                    app_name: app.name
                },
                callback: function(response) {
                    const isAppInstalled = response.message;
                    frm.set_df_property(app.field, 'disabled', !isAppInstalled);
                    
                    if (!isAppInstalled) {
                        frm.set_value(app.field, 0);
                        frappe.show_alert({
                            message: __(`'${app.name}' app is not installed. Connection cannot be enabled. Please install the app '${app.name}' first.`),
                            indicator: 'orange'
                        });
                    }
                }
            });
        });
    }
});
