from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
		{
			"label": _("Employee"),
			"items": [
				{
					"type": "doctype",
					"name": "employee",
				},

			]
		},
]
