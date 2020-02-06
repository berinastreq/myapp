
from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days

def run_122():
    # todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
    # todo.insert()
	# result = frappe.db.sql(""" SHOW COLUMNS FROM `tabmeeting` LIKE 'test_field'""");
    # print(result);
    # res = frappe.get_all('meeting')
    # print(res)
    doc = frappe.get_doc({
	"doctype": "meeting",
	"meeting_subject": "myapp newww",
	"status": "Open"
    })
    doc.insert()