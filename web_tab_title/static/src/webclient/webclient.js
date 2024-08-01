/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { useService } from "@web/core/utils/hooks";

patch(WebClient.prototype, {
  setup() {
    super.setup();
    const company = useService("company");
    const companyTabTitle =
      session.company_tab_title[company.currentCompany.id];
    this.title.setParts({ zopenerp: companyTabTitle || "Odoo" });
  },
});
