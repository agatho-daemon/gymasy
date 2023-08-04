# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class GymasySettings(Document):
	def validate(self):
		# Testing case!!!
		if self.number_of_lockers < len(self.lockers_list):
			frappe.throw(
				title = "Error",
				msg = "It seems the Gym is reducing the number of lockers. Please contact the developer to do the necessary adjustments."
			)