from __future__ import unicode_literals
import frappe
from frappe.utils.fixtures import sync_fixtures
sync_fixtures()

def execute():
	# add set user permissions rights to HR Manager
	# frappe.reload_doc("Myapp", 'doctype', "meeting")
	# print('123')
	# test1 = frappe.db.sql("""select * from tabmeeting where meeting_subject='met1' """)
	# print(test1)
	# frappe.db.sql("""SET SQL_SAFE_UPDATES=0 ;""");
	

	full_data = frappe.db.sql(""" select test_field from `tabmeeting` WHERE test_field IS NULL """,debug=1)
	for dt in full_data:
		print(dt)

# update `tabmeeting` SET to_date=from_date where to_date=null

	# print(full_data)
	# frappe.db.sql(""" update `tabmeeting` set roomno=4234 where name='7c3fc1579d' """,debug=1);

	frappe.db.sql(""" update `tabmeeting` set test_field='nodata' where test_field IS NULL """,debug=1);
	# frappe.db.commit()
	full_data = frappe.db.sql(""" select test_field from `tabmeeting` WHERE test_field IS NULL """,debug=1)
	for dt in full_data:
		print(dt)
