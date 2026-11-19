from odoo import fields, models


class Tur(models.Model):
    _name = "kutuphane.tur"
    _description = "Kitap Türü"

    name = fields.Char(string="Tür", required=True)