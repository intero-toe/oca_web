from odoo import models
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        session_info = super().session_info()
        if request.session.uid:
            company_tab_mapping = {}
            user_companies = request.env.user.company_ids
            for company in user_companies:
                company_tab_mapping[company.id] = company.tab_title
            session_info["company_tab_title"] = company_tab_mapping
        return session_info
