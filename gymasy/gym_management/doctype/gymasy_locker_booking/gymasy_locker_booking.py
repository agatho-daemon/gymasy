# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json

from frappe.model.document import Document


class GymasyLockerBooking(Document):
	# pass
	def validate(self):
		
		# Booking a locker
		chosen_locker = self.locker_number

		the_lockers_list = frappe.db.get_single_value("Gymasy Settings", "lockers_list")

		the_lockers_list = json.loads(the_lockers_list)

		if the_lockers_list[chosen_locker] == 1:
			frappe.throw(
				title = "Error",
				msg = f"Locker «{chosen_locker}» is already booked. Please choose another locker."
			)
		else:
			the_lockers_list[chosen_locker] = 1
			frappe.db.set_single_value("Gymasy Settings", "lockers_list", json.dumps(the_lockers_list))
			frappe.msgprint(f"Locker «{chosen_locker}» is booked successfully!")
		
	
	def on_cancel(self):
		# Canceling a locker booking
		booked_locker = self.locker_number

		the_lockers_list = frappe.db.get_single_value("Gymasy Settings", "lockers_list")

		the_lockers_list = json.loads(the_lockers_list)

		if the_lockers_list[booked_locker] == 1:
			the_lockers_list[booked_locker] = 0
			frappe.db.set_single_value("Gymasy Settings", "lockers_list", json.dumps(the_lockers_list))
			frappe.msgprint(f"Locker «{booked_locker}» is canceled successfully! Advise the member to remove his/her belongings from the locker.")
		else:
			frappe.throw(
				title = "Error",
				msg = f"Locker «{booked_locker}» is already available!"
			)