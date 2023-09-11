# -*- coding: utf-8 -*-
from odoo import http,fields,_
from odoo.http import request,route,json ,Controller
from odoo.exceptions import ValidationError
from datetime import datetime




# from odoo.addons.website_sale.controllers.main import WebsiteSale


class SalesOrder(http.Controller):
    @http.route('/quotation', auth='public', website=True, type='http')
    def sales_order(self, **kw):
        start_date = kw.get('start_date')
        end_date = kw.get('end_date')
        domain = [('date_order', '>=', start_date), ('date_order', '<=', end_date)]
        quotation_records = request.env['sale.order'].search(domain)

        # sales_order = request.env['sale.order'].sudo().search([('invoice_ids.payment_state','=','paid')])
        sales_order = request.env['sale.order'].sudo().search([('state', '=', 'draft')])
        quotation = ({'records': sales_order})
        return request.render('sales_inherit.tmp_sales_data_id', quotation,{"quotations_record": quotation_records})



    @http.route('/quotation_data_json/', type='json', auth='public', website=True, methods=['POST'])
    def quotation_data_json(self, **kw):
        # Convert start_date and end_date to datetime objects if needed
        # Define a domain to filter records based on start and end date
        start_date = kw.get('start_date')
        end_date = kw.get('end_date')

        domain = [('date_order', '>=', start_date), ('date_order', '<=', end_date)]

        # Fetch quotation records filtered by date range
        quotation_records = http.request.env['sale.order'].search_read(
            domain,
            fields=['name', 'date_order', 'partner_id', 'user_id', 'amount_total', 'state', 'invoice_status', ]
            # Add more fields as needed
        )
        # print(quotation_records)
        # Convert datetime objects to strings in the data
        formatted_records = []
        for record in quotation_records:
            formatted_record = {
                'name': record['name'],
                'date_order': record['date_order'].strftime('%Y-%m-%d %H:%M:%S'),
                'partner_id': record['partner_id'],
                'user_id': record['user_id'],
                'amount_total': record['amount_total'],
                'state': record['state'],
                'invoice_status': record['invoice_status'],
                # Format as needed
                # Add more fields as needed
            }
            formatted_records.append(formatted_record)

        # Prepare the data as a JSON response
        response_data = json.dumps(formatted_records)
        print(response_data)

        return {'response_data': response_data}

    # @http.route(['/quotation'], type ="http", auth ="user", website = 'True')
    # def portal_my_payslip(self,**arg):
    #     start_date=arg.get('start_date')
    #     end_date=arg.get('end_date');

    #     @http.route('/sales_inherit/sales_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_inherit.listing', {
#             'root': '/sales_inherit/sales_inherit',
#             'objects': http.request.env['sales_inherit.sales_inherit'].search([]),
#         })

    # @http.route('/sales_inherit/sales_inherit/objects/<model("sales_inherit.sales_inherit"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('sales_inherit.object', {
    #         'object': obj
    #     })

