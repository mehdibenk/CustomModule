# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words

from odoo.tools import amount_to_text

# class module_somaprec(models.Model):
#     _name = 'module_somaprec.module_somaprec'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100



#class module_somaprec(models.Model):
 #   _name = 'module_somaprec.module_somaprec'
#class MyClass( models.Model ):
#	_inherit = "account.invoice"
  #  _inherit = "account.invoice"
   # def a_new_func()
    #    return 50







class SaleOrderInherit(models.Model):
#    _name = 'module_somaprec.my_sale_order'
    _inherit = 'sale.order'
#    _inherit = 'account.invoice'

#    @api.depends('amount_total', 'currency_id')
#    @api.multi
    @api.model
    def foo(self):
        return 20
