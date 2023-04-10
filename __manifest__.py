{
    'name': 'Attendance Import From Machine',
    'version': '0.1',
    'description': 'This module provides a functionality to import attendance data from a machine to Odoo.',
    'category': 'Human Resources',
    'author': 'RW',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'hr',
        'hr_attendance',
    ],
        'data': [
        'views/attendance_import_views.xml',
        'views/attendance_import_templates.xml',
    ],
    'application': True,
}