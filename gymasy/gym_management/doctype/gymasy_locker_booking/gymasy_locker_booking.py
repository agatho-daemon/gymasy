# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json

from frappe.model.document import Document


class GymasyLockerBooking(Document):
	# pass
	def on_submit(self):
		
		# Booking a locker
		chosen_locker = self.locker_number

		# Early on check if chosen locker is with in range of installed lockers
		# Good case for testing!!!
		if chosen_locker > frappe.db.get_single_value("Gymasy Settings", "number_of_lockers"):
			frappe.throw(
				title = "Error",
				msg = f"Locker «{chosen_locker}» does not exist. Please choose another locker."
			)
		
		# Proceed with booking

		# Format the locker number to 3 digits
		chosen_locker = f'{chosen_locker:03}'

		the_lockers_list = frappe.db.get_single_value("Gymasy Settings", "lockers_list")

		the_lockers_list = json.loads(the_lockers_list)

		if the_lockers_list[chosen_locker] != "free":
			frappe.throw(
				title = "Error",
				msg = f"Locker «{chosen_locker}» is already booked. Please choose another locker."
			)
		else:
			the_lockers_list[chosen_locker] = self.member_name
			frappe.db.set_single_value("Gymasy Settings", "lockers_list", json.dumps(the_lockers_list))
			frappe.db.set_value("Gymasy Member", self.member_name, "locker_number", chosen_locker)
			self.status = "Assigned"
			frappe.msgprint(f'Locker «{chosen_locker}» is booked successfully!')


	def on_trash(self):
		# Another perfect testing case!!!
		# Deleting a locker booking
		booked_locker = self.locker_number

		the_lockers_list = frappe.db.get_single_value("Gymasy Settings", "lockers_list")

		the_lockers_list = json.loads(the_lockers_list)

		if the_lockers_list[booked_locker] == self.member_name:
			the_lockers_list[booked_locker] = "free"
			frappe.db.set_single_value("Gymasy Settings", "lockers_list", json.dumps(the_lockers_list))
			frappe.db.set_value("Gymasy Member", self.member_name, "locker_number", "free")
			frappe.msgprint(f"Locker «{booked_locker}» is canceled successfully! Advise the member to remove his/her belongings from the locker.")
		elif the_lockers_list[booked_locker] != self.member_name:
			frappe.throw(
				title = "Error",
				msg = f"Locker «{booked_locker}» does not belong to member! Check with developer to fix this issue!"
			)
		else:
			frappe.throw(
				title = "Error",
				msg = f"Locker «{booked_locker}» is a free locker! Check with developer to fix this issue!"
			)