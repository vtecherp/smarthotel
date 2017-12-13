# -*- coding: utf-8 -*-
from odoo import http

# class ErpvtechSmartHotel(http.Controller):
#     @http.route('/erpvtech_smart_hotel/erpvtech_smart_hotel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erpvtech_smart_hotel/erpvtech_smart_hotel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('erpvtech_smart_hotel.listing', {
#             'root': '/erpvtech_smart_hotel/erpvtech_smart_hotel',
#             'objects': http.request.env['erpvtech_smart_hotel.erpvtech_smart_hotel'].search([]),
#         })

#     @http.route('/erpvtech_smart_hotel/erpvtech_smart_hotel/objects/<model("erpvtech_smart_hotel.erpvtech_smart_hotel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erpvtech_smart_hotel.object', {
#             'object': obj
#         })