// Copyright (c) 2023, Ismail Tabtabai and contributors
// For license information, please see license.txt

frappe.ui.form.on("Group Class Booking", {
	refresh(frm) {
        frm.set_intro('Wrong date entries must be deleted and a new entry made, they cannot be changed.','yellow')
	},
})

frappe.ui.form.on('Group Class Booking Item', {
    // cdt, child doctype name, i.e. booking_class
    // cdn, row name in child table, i.e. MEM-0001
    date: function(frm, cdt, cdn) {
        d = locals[cdt][cdn];
        if (d.date < frappe.datetime.get_today()) {
            frappe.msgprint(__("Cannot select a date in the past!"));
            frappe.validated = false;
        }
    }
})