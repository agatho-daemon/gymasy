# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class GymasySettings(Document):
	def validate(self):
		if not self.lockers_list:
			keys = [f'{i:03}' for i in range(1, self.number_of_lockers + 1)]
			kvs = dict.fromkeys(keys, "free")
			self.lockers_list = json.dumps(kvs)
		
		# When down-sizing on number of lockers best to handle it manually.
		elif self.number_of_lockers < len(self.lockers_list):
			frappe.throw(
				title = "Error",
				msg = "It seems the Gym is reducing the number of lockers. Please contact the developer to do the necessary adjustments."
			)

		# When up-sizing the number of lockers, make sure not to overwrite the existing locker data.
		else:
			keys = [f'{i:03}' for i in range(1, self.number_of_lockers + 1)]
			kvs = dict.fromkeys(keys, "free")
			
			for v in kvs:
				if kvs[v] != "free":
					kvs[v] = self.lockers_list[v]
			
			self.lockers_list = json.dumps(kvs)