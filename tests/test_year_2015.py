# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2015(unittest.TestCase):
    def test_holiday(self):
        """
        2015年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 1, 12)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 3, 21)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 5, 6)), '憲法記念日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 7, 20)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 9, 21)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 9, 22)), '国民の休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 9, 23)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 10, 12)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2015, 12, 23)), '天皇誕生日')
