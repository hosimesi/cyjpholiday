# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2019(unittest.TestCase):
    def test_holiday(self):
        """
        2019年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 1, 14)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 3, 21)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 4, 30)), '国民の休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 1)), '天皇の即位の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 2)), '国民の休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 5, 6)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 7, 15)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 8, 11)), '山の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 8, 12)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 9, 16)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 9, 23)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 10, 14)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 10, 22)), '即位礼正殿の儀')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 11, 4)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2019, 11, 23)), '勤労感謝の日')
