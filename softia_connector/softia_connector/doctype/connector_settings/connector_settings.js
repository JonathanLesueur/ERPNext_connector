// Copyright (c) 2025, Jonathan Lesueur and contributors
// For license information, please see license.txt

frappe.ui.form.on("Connector Settings", {
	refresh(frm) {
        frm.trigger("toggle_extra_gameplan");
	},
});
