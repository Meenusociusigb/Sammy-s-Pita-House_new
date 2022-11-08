from odoo import models, fields, api, _





class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    product_note = fields.Char(string="Product Name")
    is_checked = fields.Boolean(string="is checked?")

    @api.model
    def create(self, vals):
        res = super(ProductTemplateInherit, self).create(vals)
        res.product_note = res.name + " New Product"
        print('product name is', res.product_note)
        return res


