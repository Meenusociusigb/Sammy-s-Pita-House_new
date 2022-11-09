from odoo import models, fields, api,_


class AccountMove(models.Model):
    _inherit = 'account.move'

    so_confirmed_user_id = fields.Many2one('res.users', string="SO confirmed User")
    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')



    def action_post(self):
        super(AccountMove, self).action_post
        self.confirmed_user_id = self.env.user.id


