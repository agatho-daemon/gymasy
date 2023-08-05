// Copyright (c) 2023, Ismail Tabtabai and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gymasy Member", {
	refresh(frm) {
        frm.add_custom_button(
            __('Assign Locker'), function() {
                the_list = frappe.db.get_single_value('Gymasy Settings', 'lockers_list')
                .then(r => {
                    r = JSON.parse(r);
                    lockers = Object.keys(r).filter(key => r[key] === 0)
                    return lockers;
                });
                the_list.then(response => {
                    frappe.prompt(
                        [{
                            'label': 'Available Lockers',
                            'fieldname': 'locker_number',
                            'fieldtype': 'Select',
                            'options': response
                        }],
                        function(values) {
                            frm.set_value('locker_number', values.locker_number);
                        },
                        'Select a Locker',
                        'Assign'
                    );
                });
            },
            __('Actions')
        );
        frm.add_custom_button(
            __('Assign A Trainer'), function() {
                frappe.prompt(
                    [{
                        'label': 'Trainer Name',
                        'fieldname': 'current_trainer',
                        'fieldtype': 'Link',
                        'options': 'Gymasy Trainer'
                    }],
                    function(values) {
                        frm.set_value('current_trainer', values.current_trainer);
                    },
                    'Select a Trainer',
                    'Assign'
                );
            },
            __('Actions')
        )
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
        planPrice = frappe.db.get_value('Gymasy Membership', planName, 'membership_plan_price')
        .then(r => {
            frm.set_value('membership_plan_price', r.message.membership_plan_price);
        });
    },
    start_date(frm) {
        if(frm.doc.start_date < frappe.datetime.get_today()) {
            frappe.msgprint(__("Cannot select a date in the past!"));
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

