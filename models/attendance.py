from odoo import api, fields, models

class Attendance(models.Model):
    _name = 'attendance.import'
    _description = 'Attendance Import'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date = fields.Date(string='Date', required=True)
    clock_in = fields.Datetime(string='Clock In', required=True)
    clock_out = fields.Datetime(string='Clock Out', required=True)