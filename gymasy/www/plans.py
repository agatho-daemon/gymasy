import frappe

def get_context(context):
    categories = frappe.get_list(
        "Gymasy Workout Plan",
        fields=["name",
                "plan_category",
                "phase_table"],
        order_by="name asc"
    )
    context.categories = categories

    plan_details = frappe.get_all(
        "Gymasy Workout Plan Exercise",
        fields = ['parent',
                  'idx',
                  'workout_plan_phase',
                  'workout_plan_phase_exercise'
                 ],
        order_by = 'parent asc, idx asc'
    )
    context.plan_details = plan_details