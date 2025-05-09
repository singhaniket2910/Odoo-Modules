# from odoo import http


# class MyFirstModule(http.Controller):
#     @http.route('/my__first__module/my__first__module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my__first__module/my__first__module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my__first__module.listing', {
#             'root': '/my__first__module/my__first__module',
#             'objects': http.request.env['my__first__module.my__first__module'].search([]),
#         })

#     @http.route('/my__first__module/my__first__module/objects/<model("my__first__module.my__first__module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my__first__module.object', {
#             'object': obj
#         })
