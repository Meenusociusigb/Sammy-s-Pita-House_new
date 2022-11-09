from odoo import models, fields, api

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    seller_name = fields.Char(string="Seller Name")
    new_quotation = fields.Boolean(string="New Quotation")
    confirmed_user_id = fields.Many2one('res.users',string='Confirmed User')
    so_confirmed_user_id = fields.Many2one('res.users', string="SO confirmed User")

    def action_confirm(self):
        super(SaleOrderInherit,self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    # def _prepare_invoice(self):
    #     invoice_vals = super(SaleOrderInherit,self)._prepare_invoice()
    #     invoice_vals['so_confirmed_user_id'] = self.confirmed_user_id
    #     return invoice_vals

    @api.model
    def create(self, vals):
        res = super(SaleOrderInherit, self).create(vals)
        res.seller_name = res.name

        return res
