# Copyright (c) 2024, AMan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	#This Function For Insert Value Of Full Name When User Enterted First Name Middle Name and Last Name and Submit it
	def before_save(self):
		self.full_name=f'{self.first_name} {self.middle_name or ""} {self.last_name} '
	