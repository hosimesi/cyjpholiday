# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2013(unittest.TestCase):
    def test_holiday(self):
        """
        2013年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 1, 14)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 3, 20)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 5, 6)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 7, 15)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 9, 16)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 9, 23)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 10, 14)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 11, 4)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2013, 12, 23)), '天皇誕生日')
