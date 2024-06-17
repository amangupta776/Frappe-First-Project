# Copyright (c) 2024, AMan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class Program(Document):
	def before_save(self):
		startDate = datetime.strptime(self.start_date, "%Y-%m-%d")
		year1 = startDate.year
		month1 = startDate.month
		day1 = startDate.day

		endDate = datetime.strptime(self.end_date, "%Y-%m-%d")
		year2 = endDate.year
		month2 = endDate.month
		day2 = endDate.day

		if startDate > endDate:
			frappe.throw("Start date should be before end date")

		duration = 0.0  # duration is float datatype in months

		if year1 < year2:
			duration += (12 - month1)
			year1 += 1
			month1 = 0

		duration += (year2 - year1) * 12

		day = 0.0

		if day1 > day2:
			day += (31 - day1)
			month1 += 1
			day += day2

		day += (day2 - day1)
		duration += float(day) / 31.0
		duration += (month2 - month1)

		self.duration = duration