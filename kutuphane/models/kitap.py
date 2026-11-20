from odoo import api, fields, models
from odoo.exceptions import ValidationError


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

    yazar_id = fields.Many2one("kutuphane.yazar", string="Yazar")
    tur_ids = fields.Many2many("kutuphane.tur", string="Türler")
    aciklama = fields.Text(string="Açıklama")
    sayfa_sayisi = fields.Integer(string="Sayfa Sayısı")
    fiyat = fields.Float(string="Fiyat")
    yayin_tarihi = fields.Date(string="Yayın Tarihi")
    ciltli_mi = fields.Boolean(string="Ciltli mi?")

    def action_odunc_ver(self):
        for kitap in self:
            kitap.durum = "oduncte"
        return True

    def action_rafa_koy(self):
        for kitap in self:
            kitap.durum = "rafta"
        return True

    @api.constrains("sayfa_sayisi", "fiyat")
    def _check_negatif_olmasin(self):
        for kitap in self:
            if kitap.sayfa_sayisi < 0:
                raise ValidationError("Sayfa sayısı negatif olamaz.")
            if kitap.fiyat < 0:
                raise ValidationError("Fiyat negatif olamaz.")