from odoo import api, fields, models


class Yazar(models.Model):
    _name = "kutuphane.yazar"
    _description = "Yazar"

    name = fields.Char(string="Ad Soyad", required=True)
    dogum_yili = fields.Integer(string="Doğum Yılı")
    ulke = fields.Char(string="Ülke")
    kitap_ids = fields.One2many("kutuphane.kitap", "yazar_id", string="Kitaplar")
    kitap_sayisi = fields.Integer(string="Kitap Sayısı", compute="_compute_kitap_sayisi")

    @api.depends("kitap_ids")
    def _compute_kitap_sayisi(self):
        for yazar in self:
            yazar.kitap_sayisi = len(yazar.kitap_ids)