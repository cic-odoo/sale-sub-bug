# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleSub(models.Model):
    _inherit = 'sale.subscription'

    def _prepare_invoice_data(self):
        print("HELLO")

        return super(SaleSub,self)._prepare_invoice_data()
