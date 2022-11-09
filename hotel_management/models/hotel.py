from datetime import date
from odoo import models, fields, api, _

class HotelManagement(models.Model):
    _name = 'hotel.hotel'
    _description = 'hotel_management'

    serial_no = fields.Char(string='Serial No', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    name = fields.Char(string='Hotel Name')
    phone_no = fields.Char(string='Phone Number')
    rating = fields.Selection(
        [('1star', '*'), ('2star', '**'), ('3star', '***'), ('4star', '****'), ('5star', '*****')], string='Rating')
    tag_ids = fields.Many2many('account.account.tag', string="Tags")
    include_phone_no = fields.Boolean('Include Phone Number')
    started_date = fields.Date(string='Started Date')
    years = fields.Integer(string='Years', compute='_compute_years', tracking=True)
    active = fields.Boolean('Active', default=True)
    time_to_leave = fields.Date('Time To Leave')
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    # computed field
    def _compute_years(self):

        for rec in self:
            today = date.today()
            if rec.started_date:
                rec.years = abs(today.year - rec.started_date.year)
            else:
                rec.years = 0

    def write(self, vals):
        print("Editted data", vals)
        return super(HotelManagement, self).write(vals)

    def action_confirm(self):

        one_star = self.env['hotel.hotel'].search_count([('rating', '=', '1star')])
        print("1 Star rating is", one_star)

        two_star = self.env['hotel.hotel'].search_count([('rating', '=', '2star')])
        print("2 Star rating is", two_star)

        three_star = self.env['hotel.hotel'].search_count([('rating', '=', '3star')])
        print("3 Star rating is", three_star)

        four_star = self.env['hotel.hotel'].search_count([('rating', '=', '4star')])
        print("4 Star rating is", four_star)

        five_star = self.env['hotel.hotel'].search_count([('rating', '=', '5star')])
        print("5 Star rating is", five_star)

    def action_browse(self):
        browse_data = self.env['hotel.hotel'].browse([95, 98, 115, 94])
        print("browse_data", browse_data)
        search = self.env['hotel.hotel'].search([('id', '!=', False)], limit=1)
        print(search, "search")
        print("Filtered datas", browse_data.filtered(lambda o: o.started_date))
        print("mapped data", browse_data.mapped(lambda o: o.rating))
        for rec in browse_data:
            print("Result is...", rec, "Hotel Name:", rec.name, "Phone Number", rec.phone_no,
                  "Rating:", rec.rating, "Started Date", rec.started_date)



    @api.model
    def create(self, vals):
        print("valsss", vals)
        if vals.get('serial_no', _('New')) == 'New':
            vals['serial_no'] = self.env['ir.sequence'].next_by_code('hotel.management')
            print("serial_no", vals['serial_no'])
        res = super(HotelManagement, self).create(vals)
        return res

    def auto_remove_stud(self):
        self.env['hotel.hotel'].search([('time_to_leave', '=', fields.Date.today())]).write({'active': False})