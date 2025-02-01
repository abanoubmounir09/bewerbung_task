app_name = "bewerbung_task"
app_title = "bewerbung_task"
app_publisher = "Abanoub mounir"
app_description = "bewerbung"
app_email = "abanoubmounir07@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "bewerbung_task",
# 		"logo": "/assets/bewerbung_task/logo.png",
# 		"title": "bewerbung_task",
# 		"route": "/bewerbung_task",
# 		"has_permission": "bewerbung_task.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bewerbung_task/css/bewerbung_task.css"
# app_include_js = "/assets/bewerbung_task/js/bewerbung_task.js"

# include js, css files in header of web template
# web_include_css = "/assets/bewerbung_task/css/bewerbung_task.css"
# web_include_js = "/assets/bewerbung_task/js/bewerbung_task.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bewerbung_task/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "bewerbung_task/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bewerbung_task.utils.jinja_methods",
# 	"filters": "bewerbung_task.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bewerbung_task.install.before_install"
# after_install = "bewerbung_task.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bewerbung_task.uninstall.before_uninstall"
# after_uninstall = "bewerbung_task.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "bewerbung_task.utils.before_app_install"
# after_app_install = "bewerbung_task.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "bewerbung_task.utils.before_app_uninstall"
# after_app_uninstall = "bewerbung_task.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bewerbung_task.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"bewerbung_task.tasks.all"
	# ],
	"daily": [
		"bewerbung_task.controllers.employee_login_api.init_mail_user_login_hsitory"
	]
    # ,
	# "hourly": [
	# 	"bewerbung_task.tasks.hourly"
	# ],
	# "weekly": [
	# 	"bewerbung_task.tasks.weekly"
	# ],
	# "monthly": [
	# 	"bewerbung_task.tasks.monthly"
	# ],
}

# Testing
# -------

# before_tests = "bewerbung_task.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bewerbung_task.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bewerbung_task.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bewerbung_task.utils.before_request"]
# after_request = ["bewerbung_task.utils.after_request"]

# Job Events
# ----------
# before_job = ["bewerbung_task.utils.before_job"]
# after_job = ["bewerbung_task.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bewerbung_task.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

