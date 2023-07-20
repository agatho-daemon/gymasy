# Profile info:
# 1. Active Plan
# 2. Remaining days in the subscription 
# 3. Allocated Trainer (with contact info) Past Plans

import frappe

def get_context(context):
    # 1. Active Plan
    active_plans = frappe.get_list('Gymasy Member',
                                   fields=['name', 'membership_plan', 'start_date', 'end_date'])
    # 2. Remaining days in subscription

    # 3. Allocated Trainer (with contact info) & Past Plans