# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SHBranch(models.Model):
    _name = 'sh.branch'

    name = fields.Char()
    room_ids = fields.One2many('sh.room', 'branch_id', 'Rooms')
