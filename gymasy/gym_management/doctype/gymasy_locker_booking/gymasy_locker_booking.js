// Copyright (c) 2023, Ismail Tabtabai and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gymasy Locker Booking", {
	refresh(frm) {
        frm.add_custom_button(__('Assign Locker'), function() {
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
            })
        }, __('Actions'))
	},
    locker_number(frm) {
        console.log(frm.doc.locker_number);
        the_list = frappe.db.get_single_value('Gymasy Settings', 'lockers_list')
        .then(response => {
            response = JSON.parse(response);
            response[frm.doc.locker_number] = 1;
            // console.log(JSON.stringify(response));
            // frappe.db.set_value('Gymasy Settings', 'Gymasy Settings', 'lockers_list', JSON.stringify(response));
        })
    }
});
