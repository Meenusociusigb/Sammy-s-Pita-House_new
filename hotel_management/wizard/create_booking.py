from odoo import api,fields,models

class CreateBookingWizard(models.TransientModel):
    _name = "create.booking.wizard"
    _description = "Create Booking Wizard"

    name = fields.Char(string="Name")
    customer_id = fields.Many2one('hotel.hotel', string="Customer Name")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")


    def action_create_booking(self):
        print("Button clicked")

