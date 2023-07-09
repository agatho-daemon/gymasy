# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class GymasySettings(Document):
	def validate(self):
		if not self.lockers_list:
			keys = [f'{i:03}' for i in range(1, self.number_of_lockers + 1)]
			keys_values = dict.fromkeys(keys, 0)
			self.lockers_list = json.dumps(keys_values)
		
		elif self.number_of_lockers < len(self.lockers_list):
			frappe.throw(
				title = "Error",
				msg = "It seems the Gym is reducing the number of lockers. Please contact the developer to do the necessary adjustments."
			)
		
		else:
			keys = [f'{i:03}' for i in range(1, self.number_of_lockers + 1)]
			keys_values = dict.fromkeys(keys, 0)
			
			for key in keys_values:
				keys_values[key] = self.lockers_list[key]
			
			self.lockers_list = json.dumps(keys_values)