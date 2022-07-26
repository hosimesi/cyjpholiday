# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2020(unittest.TestCase):
    def test_holiday(self):
        """
        2020年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 1, 13)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 2, 23)), '天皇誕生日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 2, 24)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 3, 20)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 5, 6)), '振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 7, 23)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 7, 24)), 'スポーツの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 8, 10)), '山の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 9, 21)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 9, 22)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2020, 11, 23)), '勤労感謝の日')
