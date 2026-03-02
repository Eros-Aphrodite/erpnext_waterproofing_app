__version__ = "0.0.1"


def _patch_app_route():
	"""Force Waterproofing Inspections app tile to open the Waterproofing Inspection list view."""
	import frappe.apps as apps_module

	_original_get_route = apps_module.get_route

	def _get_route(app, allowed_workspaces=None):
		if app and app.get("name") == "waterproofing_inspections":
			# Route directly to Waterproofing Inspection DocType list
			return "/app/waterproofing-inspection"
		return _original_get_route(app, allowed_workspaces)

	apps_module.get_route = _get_route


_patch_app_route()
