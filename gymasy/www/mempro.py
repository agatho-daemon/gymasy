import frappe

def get_context(context):

    context.test_dict = [f'{i:03}' for i in range(1, 31)]

    context.members = frappe.get_list(
            'Gymasy Member',
            fields=[
                'name',
                'member_name',
                'membership_plan',
                'end_date',
                'current_trainer'
                ],
                order_by='name asc')