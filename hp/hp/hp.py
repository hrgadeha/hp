from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.mapper import get_mapped_doc
from datetime import date
from frappe.model.document import Document


@frappe.whitelist()
def updateEXP(doc,method):
	for i in doc.references:
		if i.reference_doctype == "Expense Claim":
			exp = frappe.get_doc("Expense Claim",i.reference_name)
			exp.ref_no = doc.reference_no
			exp.ref_date = doc.reference_date
			exp.mode = doc.mode_of_payment
			exp.save(ignore_permissions=True)