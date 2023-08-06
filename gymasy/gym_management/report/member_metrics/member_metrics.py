# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [
		{
			'fieldname': 'entry_date',
			'label': 'Entry Date',
			'fieldtype': 'Date',
			'options': 'Gymasy Member Metrics',
			'width': 100
		},
		{
			'fieldname': 'member_name',
			'label': 'Member Name',
			'fieldtype': 'Link',
			'options': 'Gymasy Member',
			'width': 150
		},
		{
			'fieldname': 'member_weight',
			'label': 'Weight (Kg)',
			'fieldtype': 'Float',
			'width': 150
		},
		{
			'fieldname': 'waist_circumference',
			'label': 'Waist (cm)',
			'fieldtype': 'Float',
			'width': 150
		},
		{
			'fieldname': 'muscle_mass',
			'label': 'Muscle Mass (Kg)',
			'fieldtype': 'Float',
			'width': 150
		},
		{
			'fieldname': 'body_fat_percentage',
			'label': 'Body Fat (%)',
			'fieldtype': 'Float',
			'width': 150
		},
		{
			'fieldname': 'daily_calorie_intake',
			'label': 'Daily Calorie (Kcal)',
			'fieldtype': 'Int',
			'width': 150
		}

	], [
		{
			'entry_date': '2023-06-01',
			'member_weight': 80,
			'waist_circumference': 100,
			'muscle_mass': 50,
			'body_fat_percentage': 20,
			'daily_calorie_intake': 2000
		}
	]

	# Working on records to be used in the chart
	metrics_doctype = frappe.qb.DocType("Gymasy Member Metrics")

	records = frappe.qb.from_('Gymasy Member Metrics') \
				.select('entry_date',
	    				'member_name',
	    				'member_weight',
						'waist_circumference',
						'muscle_mass',
						'body_fat_percentage',
						'daily_calorie_intake') \
				.run(as_dict = True)
	data = records

	chart = {
		'data': {
			'labels': [record.entry_date for record in records],
			'datasets': [
				{
					'name': 'Weight (Kg)',
					'values': [record.member_weight for record in records]			},
				{
					'name': 'Waist (cm)',
					'values': [record.waist_circumference for record in records]
				},
				{
					'name': 'Muscle Mass (Kg)',
					'values': [record.muscle_mass for record in records]
				},
				{
					'name': 'Body Fat (%)',
					'values': [record.body_fat_percentage for record in records]
				}
			]
		},
		'type': 'line',
		'maxLegendPoints': 2,
		'title': 'Member Metrics',
		'showLegend': 1
	}

	# report_summary = [
	# 	{
	# 		'indicator': 'reduction',
	# 		'indicator': 'Green',
	# 		'label': 'Metrics',
	# 		'datatype': 'Percent'
	# 	}
	# ]



	return columns, data, None, chart#, report_summary
