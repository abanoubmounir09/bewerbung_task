

import frappe
from frappe import _
from frappe.desk.query_report import build_xlsx_data
from frappe.utils.csvutils import to_csv
 
@frappe.whitelist(allow_guest=1)
def init_mail_user_login_hsitory():
	try: 
		data = get_user_data()
		xlsx_data = init_csv_file(data)
		save_and_send_file(xlsx_data,'user_history_login')
	except Exception:
		frappe.log_error(frappe.get_traceback(), _("init_mail_user"))



def get_user_data():
	sql_data = f"""
	SELECT `tabUser`.first_name,`tabUser`.last_name,count(`tabSessions`.user) as no_login
	FROM `tabUser`
	LEFT JOIN `tabSessions`
	ON `tabUser`.name=`tabSessions`.user
	group by `tabUser`.name
	"""
	return frappe.db.sql(sql_data,as_dict=1)

@frappe.whitelist(allow_guest=1)
def init_csv_file(data):
	try:
		report_data = frappe._dict()
		report_data["columns"] = [{'label':'First Name','fieldname':'first_name'},{'label':'Last Name','fieldname':'last_name'},{'label':'Number of login attempts','fieldname':'no_login'}]
		report_data["result"] = data
		xlsx_data, column_widths = build_xlsx_data(report_data, [], 1, ignore_visible_idx=True)
		return to_csv(xlsx_data)
	except Exception:
			frappe.log_error(frappe.get_traceback(), _("create-csv-file"))


def save_and_send_file(data,file_name):
	try:
		_file = frappe.get_doc(
			{
				"doctype": "File",
				"file_name": f"{file_name}.csv",
				"content": data,
				"folder": "Home"
			}
		)
		_file.save(ignore_permissions=True)
		send_daily_mail(_file)
	except Exception:
			frappe.log_error(frappe.get_traceback(), _("save-file"))

def send_daily_mail(_file):
	dialy_email_doc = frappe.get_doc('Daily Email Login')
	recipients = [email.get("email_id") for email in dialy_email_doc.get('email_notification',[])]
	if recipients:
		frappe.sendmail(
						recipients=recipients,
						subject='Daily Login User Notification',
						header=['Daily login Notification', "green"],
						message="A CSV File Attached.",
						attachments=[
							{
								"fname": _file.file_name,
								"fcontent": _file.get_content(),
							}
						],
					)