# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GymasyMember(Document):
	def on_submit(self):
		doc = frappe.new_doc('Gymasy Member Metrics')
		
		doc.entry_date =  self.start_date
		doc.member_name = self.name
		doc.member_weight = self.member_weight
		doc.waist_circumference = self.waist_circumference
		doc.muscle_mass = self.muscle_mass
		doc.body_fat_percentage = self.body_fat_percentage
		doc.daily_calorie_intake = self.daily_calorie_intake

		doc.insert()