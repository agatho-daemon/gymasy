import frappe
import json

def get_context(context):
	# do your magic here
	pass





@frappe.whitelist()
# gymasy.gymasy.gym_management.web_form.group_class_booking.group_class_booking.submit_data
# gymasy.gym_management.doctype.group_class_booking_item.group_class_booking_item.submit_data
def submit_data(member_name, child_table_data):
	child_table_data = json.loads(child_table_data)
	for row in child_table_data:
		# print(row)
		doc = frappe.new_doc("Group Class Booking Item")
		doc.parent = member_name
		doc.parentfield = "booking_class"
		doc.parenttype = "Group Class Booking"
		doc.date = row.get("date")
		doc.group_class = row.get("group_class")
		doc.save()
		frappe.db.commit()