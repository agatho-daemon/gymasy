# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [
		{
			'fieldname': 'entry_date',
			'label': 'Entry Date',
			'fieldtype': 'Datetime',
			'options': 'Gymasy Member Metrics',
			'width': 200
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
			'metrics_entry_datetime': '1/7/2023 14:00:00',
			'member_weight': 80,
			'waist_circumference': 100,
			'muscle_mass': 50,
			'body_fat_percentage': 20,
			'daily_calorie_intake': 2000
		}
	]

	chart = {
		'data': {

		},
		'type': 'line',
		'showLegend': 1
	}

	report_summary = [
		{
			'indicator': 'reduction',
			'indicator': 'Green',
			'label': 'Metrics',
			'datatype': 'Percent'
		}
	]



	return columns, data, None, chart, report_summary
