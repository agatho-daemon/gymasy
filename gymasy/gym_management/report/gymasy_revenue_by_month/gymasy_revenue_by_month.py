# Copyright (c) 2023, Ismail Tabtabai and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			'fieldname': 'month',
			'label': 'Month',
			# 'fieldtype': 'Date',
			'width': 100
		},
		{
			'fieldname': 'revenue',
			'label': 'Total Revenue',
			'fieldtype': 'Currency',
			'width': 200
		}
	]
	
	data = frappe.db.sql(f"""
SELECT
	DATE_FORMAT(start_date, '%m-%Y') AS month,
	SUM(membership_plan_price) AS revenue
FROM
	`tabGymasy Member`
GROUP BY
	MONTH(start_date)
"""
	)

	chart = {
		'data': {
			'labels': [row[0] for row in data],
			'datasets': [
				{
					'name': 'Revenue By Month',
					'values': [row[1] for row in data]
				}
			]
		},
		'type': 'bar',
		'showLegend': 1
	}

	report_summary = [
		{
			'value': 'Total Revenue Per Month',
			'indicator': 'Green',
			'label': 'Revenue Per Month',
			'datatype': 'Currency'
		}
	]

	return columns, data, None, chart, None
