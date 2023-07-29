# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe
# install pendulum using: ./env/bin/pip install pendulum
# import pendulum
from frappe.model.document import Document


class GymasyTrainerSubscription(Document):
	def on_update(self):

		frappe.db.set_value('Gymasy Member', self.member_name, 'current_trainer', self.trainer_name)

		frappe.db.commit()
		# doc = frappe.get_doc('Gymasy Member', self.member_name)
		# doc.current_trainer = self.trainer_name
		# doc.save()
		# pendulum.week_starts_at(pendulum.SUNDAY)
		# pendulum.week_ends_at(pendulum.SATURDAY)
		# today = pendulum.today()
		# wstart = today.start_of('week')
		# wend = today.end_of('week')
		# print(f'Week Starts on: {wstart}\nWeek ends on: {wend}')
		# if self.subscription_date < wstart:
		# 	frappe.throw(f'Subscription date cannot be earlier than {wstart}')