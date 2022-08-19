# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2016(unittest.TestCase):
    def test_holiday(self):
        """
        2016年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 1, 11)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 3, 20)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 3, 21)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 7, 18)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 8, 11)), '山の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 9, 19)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 9, 22)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 10, 10)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2016, 12, 23)), '天皇誕生日')
