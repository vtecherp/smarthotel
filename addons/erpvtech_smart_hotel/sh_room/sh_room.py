# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SHRoom(models.Model):
    _name = 'sh.room'

    name = fields.Char()
