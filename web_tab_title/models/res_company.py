from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    tab_title = fields.Char(string="Tab Title", default="Odoo")
