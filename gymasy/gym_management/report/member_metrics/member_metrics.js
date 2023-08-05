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
				'member_weight',
				'waist_circumference',
				'muscle_mass',
				'body_fat_percentage',
				'daily_calorie_intake'
			],
			default: 'Metrics'
		}
	]
};
