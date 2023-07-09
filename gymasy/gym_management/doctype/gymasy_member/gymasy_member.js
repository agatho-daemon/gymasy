// Copyright (c) 2023, Ismail Tabtabai and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gymasy Member", {
	refresh(frm) {
        // planName = frm.get_field('membership_plan').value;
        // console.log(planName);
	},
    membership_plan(frm) {
        planName = frm.get_field('membership_plan').value;
        duration = frappe.db.get_value('Gymasy Membership', planName, 'membership_plan_duration')
        .then(r => {
            return r.message.membership_plan_duration;
        });
        duration.then(r => {
            ending = frappe.datetime.add_months(frm.doc.start_date, r);
            ending = frappe.datetime.add_days(ending, -1);
            frm.set_value('end_date', ending);
        });
    },
    start_date(frm) {
        if(frm.doc.start_date < frappe.datetime.get_today()) {
            frappe.msgprint(__("Can not select a date in the past!"));
            frappe.validated = false;
        } else {
            planName = frm.get_field('membership_plan').value;
            if (!planName) {
                frappe.msgprint(__("Please select a membership plan before setting dates!"));
            }
            duration = frappe.db.get_value('Gymasy Membership', planName, 'membership_plan_duration')
            .then(r => {
                return r.message.membership_plan_duration;
            });
            duration.then(r => {
                ending = frappe.datetime.add_months(frm.doc.start_date, r);
                ending = frappe.datetime.add_days(ending, -1);
                frm.set_value('end_date', ending);
            });
        }
    }
});

