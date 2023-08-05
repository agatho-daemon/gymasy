import frappe

# Profile info:
# 1. Active Plan
# 2. Remaining days in the subscription 
# 3. Allocated Trainer (with contact info) Past Plans

def get_context(context):
    gymasy_members = frappe.get_list(
        "Gymasy Member",
        fields=['name', 'member_name', 'membership_plan', 'end_date', 'current_trainer'],
        order_by="name asc")
    
    context.members = gymasy_members

    test_member = [f'{i:03}' for i in range(1, 31)]
    frappe.msgprint(test_member)
    context.test_member = test_member