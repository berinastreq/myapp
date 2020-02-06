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
	# exists = False;
	result = frappe.db.sql(""" SHOW COLUMNS FROM `tabmeeting` LIKE 'test_field'""");
	if result:
		exists = True;
		frappe.db.sql(""" update `tabmeeting` set test_field='nodata' where test_field IS NULL """,debug=1);
	else:
		exists = False;
	
	print(exists)
	# full_data = frappe.db.sql(""" select test_field from `tabmeeting` WHERE test_field IS NULL """,debug=1)
	# for dt in full_data:
	# 	print(dt)

	  

	# full_data = frappe.db.sql(""" select test_field from `tabmeeting` WHERE test_field IS NULL """,debug=1)
	# for dt in full_data:
	# 	print(dt)

	# frappe.db.commit()