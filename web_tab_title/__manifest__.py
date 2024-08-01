#
#    Author: Intero Technologies GmbH <https://www.intero-technologies.de>
#    Copyright 2023 Intero Technologies GmbH
#    License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#

{
    "name": "Web Tab Title",
    "version": "17.0.1.0.0",
    "category": "Custom",
    "author": "Intero Technologies GmbH",
    "website": "https://github.com/OCA/web",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "data": [
        "views/res_company_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "web_tab_title/static/src/webclient/webclient.js",
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
