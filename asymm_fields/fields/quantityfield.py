# -*- coding: utf-8 -*-
#    Asymmetric Base Framework :: Fields
#    Copyright (C) 2013-2014  Asymmetric Ventures Inc.
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; version 2 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import absolute_import, division, print_function, unicode_literals

from decimal import Decimal

from django.db import models

ZERO_DOLLARS = ZERO_QTY = Decimal('0.00')

class QtyField(models.DecimalField):
	
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('default', ZERO_QTY)
		kwargs.setdefault('max_digits', 15)
		kwargs.setdefault('decimal_places', 2)
		
		super(QtyField, self).__init__(*args, **kwargs)

DollarField = QtyField

try:
	from south.modelsinspector import add_introspection_rules
	
	add_introspection_rules([], ['^asymm_fields\.fields\.quantityfield\.QtyField'])
	add_introspection_rules([], ['^asymm_fields\.fields\.quantityfield\.DollarField'])
except ImportError:
	pass
