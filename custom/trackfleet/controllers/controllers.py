# -*- coding: utf-8 -*-
# from odoo import http


# class Trackfleet(http.Controller):
#     @http.route('/trackfleet/trackfleet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trackfleet/trackfleet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trackfleet.listing', {
#             'root': '/trackfleet/trackfleet',
#             'objects': http.request.env['trackfleet.trackfleet'].search([]),
#         })

#     @http.route('/trackfleet/trackfleet/objects/<model("trackfleet.trackfleet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trackfleet.object', {
#             'object': obj
#         })

