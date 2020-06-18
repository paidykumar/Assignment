# # -*- coding: utf-8 -*-
#
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class lepay(models.Model):
    _name = 'lepay.lepay'

    field1 = fields.Char('field1', size=256, required=True)
    field2 = fields.Char('field2', readonly=True, compute='_compute_field2')
    field3 = fields.Char('field3', readonly=True, compute='_compute_field3')

    @api.constrains('field1')
    def _check_field1(self):
        if self.field1:
            empty_list = []
            record = self.field1
            record = record.split(',')
            for value in record:
                try:
                    value = int(value)
                except:
                    raise ValidationError("Please enter only integer numbers!")
                if value not in empty_list:
                    empty_list.append(value)
                else:
                    raise ValidationError("Dont enter duplicate values!")

    @api.multi
    @api.depends('field1')
    def _compute_field2(self):
        for obj in self:
            if obj.field1:
                string = ''
                empty_list = []
                record = str(obj.field1)
                record = record.split(',')
                for value in record:
                    try:
                        value = int(value)
                    except:
                        raise ValidationError("Validation Error!")
                    if value not in empty_list:
                        empty_list.append(value)
                    else:
                        pass
                odd_numbers = [num for num in empty_list if num % 2 == 1]
                for num in odd_numbers:
                    string += str(num) + ','
                obj.field2 = string.strip(',')

    @api.multi
    @api.depends('field1')
    def _compute_field3(self):
        for obj in self:
            if obj.field1:
                newstring = []
                empty_list = []
                record = str(obj.field1)
                record = record.split(',')
                for value in record:
                    try:
                        value = int(value)
                    except:
                        raise ValidationError("Validation Error!")
                    if value not in empty_list:
                        empty_list.append(value)
                    else:
                        pass
                for i in range(len(empty_list) - 1):
                    if int(empty_list[i]) + int(empty_list[i + 1]) == 20:
                        newstring.append({int(empty_list[i]), int(empty_list[i + 1])})
                obj.field3 = str(newstring)
