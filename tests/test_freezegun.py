# coding: utf-8
import datetime
import unittest

import cyjpholiday
import freezegun


class TestFreezegun(unittest.TestCase):

    def setUp(self) -> None:
        self.the_date = datetime.date(2020, 7, 24)

    @freezegun.freeze_time('2022-8-11 12:00:00')
    def test_freezegun_datetime(self):
        now = datetime.datetime.now()
        self.assertTrue(isinstance(now, freezegun.api.FakeDatetime))
        self.assertTrue(cyjpholiday.is_holiday(now))
        self.assertEqual(cyjpholiday.is_holiday_name(now), '山の日')
