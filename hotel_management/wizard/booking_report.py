from odoo import fields, models, api


class BookingReportWizard(models.TransientModel):
    _name = "booking.report.wizard"
    _description = "Print Booking Wizard"

    customer_id = fields.Many2one('hotel.hotel', string="Customer Name")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    # @api.model
    def action_print_report(self):
        bookings = self.env['hotel.hotel'].search_read([])
        data = {
            'model': 'booking.report.wizard',
            'form': self.read()[0],
            'bookings': bookings
        }
        return self.env.ref('hotel_management.action_report_booking').report_action(self, data=data)
