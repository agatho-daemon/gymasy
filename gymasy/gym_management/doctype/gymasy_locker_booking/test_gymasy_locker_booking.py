# Copyright (c) 2023, Ismail Tabtabai and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymasyLockerBooking(FrappeTestCase):
	def test_locker_number(self):
		new_booking = frappe.get_doc('Gymasy Locker Booking', '71d49f1b03')
		has_locker = frappe.db.get_value('Gymasy Locker Booking', new_booking.name, 'locker_number')
		fail_case = f'{new_booking.member_name} is using locker {has_locker}'

		self.assertNotEqual(has_locker, 0, fail_case)
	
	def test_locker_limit(self):
		available_lockers = frappe.db.get_single_value("Gymasy Settings", "number_of_lockers")
		booked_lockers = frappe.db.count("Gymasy Locker Booking",
				   filters = {
					   "status": "Requested",
					   "status": "Processing",
					   "status": "Assigned"
					   })
		fail_case = f'Available lockers: {available_lockers}, Booked lockers: {booked_lockers}'
		self.assertLess(booked_lockers, available_lockers, fail_case)