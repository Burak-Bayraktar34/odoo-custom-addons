from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    kutuphane_uyesi = fields.Boolean(string="Kütüphane Üyesi")
    uye_no = fields.Char(string="Üye No")