# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2012(unittest.TestCase):
    def test_holiday(self):
        """
        2012年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 1, 2)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 1, 9)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 3, 20)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 4, 30)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 7, 16)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 9, 17)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 9, 22)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 10, 8)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 12, 23)), '天皇誕生日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2012, 12, 24)), '振替休日')
