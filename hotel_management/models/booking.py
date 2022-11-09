from odoo import models, fields, api


class HotelBooking(models.Model):
    _name = 'hotel.booking'

    customer_id = fields.Many2one('hotel.hotel', string="Customer Name")
    hotel_section = fields.Text(string="Note")
    hotel_section_lines_ids = fields.One2many('hotel.section.lines', 'booking_id', string='Hotel Sections')
    rating = fields.Selection(string='Rating', related='customer_id.rating', readonly=False)
    serial_no = fields.Char(string='Serial No')

    @api.onchange('customer_id')
    def onchange_customer_id(self):
        self.serial_no = self.customer_id.serial_no


class HotelSectionLines(models.Model):
    _name = 'hotel.section.lines'

    product_id = fields.Many2one('product.product', string="Name")
    price_unit = fields.Float(string='Price')
    number_of_persons = fields.Integer(string='Number Of Persons')
    booking_id = fields.Many2one('hotel.booking', string='Booking')


