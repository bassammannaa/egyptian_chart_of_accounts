# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2013 E-MIPS (http://www.e-mips.com.ar) All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Egyptian - Chart of Accounts",
    'summary': """
        Egyptian Chart of Accounts for odoo.
    """,
    'description': """
    This module for installing Chart of accounts that comply with Egypt companies.
    """,
    'author': "Bassam Mannaa",
    'website': "https://www.facebook.com/bmannaa",
    'category': 'Localization',
    'version': '12.0.0.1',
    'license': 'AGPL-3',
    'depends': ['base', 'account',],
    'images': [
        'static/description/icon.jpg',],
    'data': [
        'data/account_data.xml',
        'data/l10n_eg_chart_data.xml',
        'data/account_chart_template_data.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,

}
