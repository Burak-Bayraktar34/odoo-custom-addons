# from odoo import http


# class Kutuphane(http.Controller):
#     @http.route('/kutuphane/kutuphane', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kutuphane/kutuphane/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kutuphane.listing', {
#             'root': '/kutuphane/kutuphane',
#             'objects': http.request.env['kutuphane.kutuphane'].search([]),
#         })

#     @http.route('/kutuphane/kutuphane/objects/<model("kutuphane.kutuphane"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kutuphane.object', {
#             'object': obj
#         })

