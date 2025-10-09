// Copyright (c) 2025, Jonathan Lesueur and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gitlab Settings", {
    refresh(frm) {
        frm.trigger("toggle_extra_info");
	},
    enable_gitlab_connection(frm) {
        // déclenché quand on coche/décoche
        frm.trigger("toggle_extra_info");
    },
    toggle_extra_info(frm) {
        if(frm.doc.enable_gitlab_connection) {
            frm.set_df_property('gitlab_site_url', 'reqd', 1);
            frm.set_df_property('gitlab_site_url', 'hidden', 0);
            
            frm.set_df_property('gitlab_api_version', 'reqd', 1);
            frm.set_df_property('gitlab_api_version', 'hidden', 0);

            frm.set_df_property('gitlab_authentication_token', 'reqd', 1);
            frm.set_df_property('gitlab_authentication_token', 'hidden', 0);

            frm.set_df_property('gitlab_webhook_secret', 'hidden', 0);

        } else {
            frm.set_df_property('gitlab_site_url', 'reqd', 0);
            frm.set_df_property('gitlab_site_url', 'hidden', 1);

            frm.set_df_property('gitlab_api_version', 'reqd', 0);
            frm.set_df_property('gitlab_api_version', 'hidden', 1);

            frm.set_df_property('gitlab_authentication_token', 'reqd', 0);
            frm.set_df_property('gitlab_authentication_token', 'hidden', 1);

            frm.set_df_property('gitlab_webhook_secret', 'hidden', 1);
        }
    }
});
