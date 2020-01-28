from parameterized import parameterized

import models.user as module
from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []

    @parameterized.expand([
        ('Gold', 'Gold', False),
        ('Gold', 'Silver', False),
        ('Gold', 'Platinum', True),
        ('Silver', 'Platinum', True),
    ])
    def test_is_below_tier(self, user_tier, threshold_tier, expected):
        assert module._is_below_tier(user_tier, threshold_tier) == expected
