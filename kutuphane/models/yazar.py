from odoo import fields, models


class Yazar(models.Model):
    _name = "kutuphane.yazar"
    _description = "Yazar"

    name = fields.Char(string="Ad Soyad", required=True)
    dogum_yili = fields.Integer(string="Doğum Yılı")
    ulke = fields.Char(string="Ülke")