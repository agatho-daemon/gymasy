import frappe
import json

def execute():
    
    # Current data setup:
    # There is a reference for locker number and/or status stored in three DocTypes: Gymasy Member,
    # Gyamsy Settings and Gymasy Locker Booking. Better scenario is to have only one reference for
    # locker number and/or status. Best place for that is in the Gymasy Locker Booking DocType.
    #
    # Therefore, in this release, we will do the following:
    # 1. The json field of locker_list in Gymasy Settings DocType will be reset to empyt dictionary.
    # 2. The locker_number field in Gymasy Member DocType will be emptied.
    # 3. Both fields are set to read-only and hidden in this release.
    # 4. Both fields will be removed in a future release.

    my_dict = {}
    frappe.db.set_single_value("Gymasy Settings", "lockers_list", json.dumps(my_dict))

    member_locker = frappe.get_list("Gymasy Member", fields=['locker_number', 'name'])

    for locker in member_locker:
        frappe.db.set_value("Gymasy Member", locker.name, locker.locker_number, '')