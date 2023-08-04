# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class GymasySettings(Document):
	def validate(self):
		available_lockers = frappe.db.get_single_value("Gymasy Settings", "number_of_lockers")

		if self.number_of_lockers < available_lockers:
			frappe.throw(
				title = "Error",
				msg = "It seems the gym is downgrading. Contact the developer to do the necessary adjustments."
			)