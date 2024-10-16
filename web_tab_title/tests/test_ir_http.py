import json
import re
from parameterized import parameterized

from odoo.tests import HttpCase


class TestIrHttp(HttpCase):
    def setUp(self):
        super().setUp()
        user = self.env.ref("base.user_admin")
        self.company = user.company_id

    def _get_session_info_str(self, line_items):
        key = "odoo.__session_info__ = "
        line = next(filter(lambda item: key in item, line_items), None)
        match = re.match(rf".*{key}(.*);", line)
        return match.group(1)

    @parameterized.expand(
        [
            ("default", None, False),
            ("set", "Demo Company", "Demo Company"),
        ]
    )
    def test_session_info(self, _, tab_title, expected):
        # setup
        self.company.tab_title = tab_title
        # action
        self.authenticate("admin", "admin")
        r = self.url_open("/web")
        line_items = r.text.splitlines()
        session_info_str = self._get_session_info_str(line_items)
        session_info = json.loads(session_info_str)
        # verify
        self.assertEqual(
            session_info.get("company_tab_title")[str(self.company.id)],
            expected
        )
