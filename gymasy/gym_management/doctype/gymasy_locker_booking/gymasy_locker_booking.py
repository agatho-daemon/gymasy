# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document


class GymasyLockerBooking(Document):
	# pass
	def validate(self):
		
		# Check if locker booking limit reached.
		available_lockers = frappe.db.get_single_value("Gymasy Settings", "number_of_lockers")
		booked_lockers = frappe.db.count("Gymasy Locker Booking",
				   filters = {
					   "status": "Requested",
					   "status": "Processing",
					   "status": "Assigned"
					   })
		if booked_lockers >= available_lockers:
			frappe.throw(
				title = "Error",
				msg = "Locker booking limit reached. Extra lockers must be installed."
			)

		# Check if member has already booked a locker
		for locker in frappe.db.get_all("Gymasy Locker Booking", filters = {"member_name": self.member_name}):
			if locker.member_name == self.member_name:
				frappe.throw(
					title = "Error",
					msg = f"Member «{self.member_name}» has already booked a locker. Please cancel the current booking first."
				)
		
		# Otherwise just save request for submission


	def on_cancel(self):
		frappe.db.set_value('Gymasy Locker Booking', self.name, 'status', 'Canceled')
		frappe.msgprint("Locker canceled successfully! Advise the member to remove their belongings from the locker.")