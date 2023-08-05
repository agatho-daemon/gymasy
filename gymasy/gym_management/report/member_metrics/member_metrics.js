// Copyright (c) 2023, Ismail Tabtabai and contributors
// For license information, please see license.txt

frappe.query_reports["Member Metrics"] = {
	"filters": [
		{
			fieldname: 'member_name',
			label: __('Member Name'),
			fieldtype: 'Link',
			options: 'Gymasy Member',
			'default': 'Gymasy Member'
		},
		{
			fieldname: 'Metric',
			label: __('Metric'),
			fieldtype: 'Select',
			options: [
				'Weight',
				'Waist',
				'Muscle Mass',
				'Body Fat %',
				'Daily Calorie Intake (Kcal)'
			],
			default: 'Metrics'
		}
	]
};
