import frappe

def get_context(context):
     doc = frappe.get_all('features',fields=['f_title', 'f_desc']);
     context['feature'] = doc;
     # doc = frappe.get_all('services',fields=['f_title', 'f_desc']);
     # context['servicex'] = doc;




#     doc = frappe.get_all('employee',fields=['emp_name', 'emp_age']);
#     context['employee'] = doc[0]['emp_name'];
     # doc = frappe.get_doc('employee', '000001')
     # doc.get_full_name()
    # context['employee'] = frappe.get_doc('employee')
#     context['hub_items'] = frappe.get_all('Hub Item')
