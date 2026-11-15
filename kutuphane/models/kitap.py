from odoo import fields, models


class Kitap(models.Model):
    _name = "kutuphane.kitap"
    _description = "Kitap"

    name = fields.Char(string="Kitap Adı", required=True)
    durum = fields.Selection(
        selection=[
            ("rafta", "Rafta"),
            ("oduncte", "Ödünçte"),
            ("kayip", "Kayıp"),
        ],
        string="Durum",
        default="rafta",
    )

    yazar = fields.Char(string="Yazar")
    aciklama = fields.Text(string="Açıklama")
    sayfa_sayisi = fields.Integer(string="Sayfa Sayısı")
    fiyat = fields.Float(string="Fiyat")
    yayin_tarihi = fields.Date(string="Yayın Tarihi")
    ciltli_mi = fields.Boolean(string="Ciltli mi?")


