# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _order = "date_order asc"
    validity_time = fields.Char(string='Validity', compute='_val_time')
    @api.depends('validity_date', 'date_order')
    def _val_time(self):
        for rec in self:
            validity_date = fields.Datetime.to_datetime(rec.validity_date).date()
            date_order = fields.Datetime.to_datetime(rec.date_order).date()
            total_time = str(int((validity_date - date_order).days / 365))
            rec.validity_time = total_time


    create_date = fields.Datetime(string='Creation Date', compute='_create_date')
    @api.depends('date_order')
    def _create_date(self):
        for rec in self:
            date_order = fields.Datetime.to_datetime(rec.date_order)
            rec.create_date = date_order


    @api.onchange('validity_date')
    def _onchange_validity_date(self):
        # to connect validity_date field to expiration field
        # for rec in self:
        #     if rec.validity_date:
        #         self.order_line = [
        #             (0, 0, {'product_template_id': '', 'name': '', 'expiration_date': self.validity_date})]
        # for value update
        if self.validity_date:
            for line in self.order_line:
                line.update({'expiration_date': self.validity_date})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    expiration_date = fields.Date(string='Expiration')


# class Invoicing(models.Model):
#     _inherit='account.move'