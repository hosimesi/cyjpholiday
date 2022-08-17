# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2018(unittest.TestCase):
    def test_holiday(self):
        """
        2018年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 1, 8)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 2, 12)), '建国記念の日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 3, 21)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 4, 30)), '昭和の日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 7, 16)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 8, 11)), '山の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 9, 17)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 9, 23)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 9, 24)), '秋分の日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 10, 8)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 12, 23)), '天皇誕生日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2018, 12, 24)), '天皇誕生日 振替休日')
