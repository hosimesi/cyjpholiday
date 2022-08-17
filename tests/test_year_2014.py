# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2014(unittest.TestCase):
    def test_holiday(self):
        """
        2014年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 1, 1)), '元日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 1, 13)), '成人の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 2, 11)), '建国記念の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 3, 21)), '春分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 4, 29)), '昭和の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 5, 3)), '憲法記念日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 5, 4)), 'みどりの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 5, 5)), 'こどもの日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 5, 6)), 'みどりの日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 7, 21)), '海の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 9, 15)), '敬老の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 9, 23)), '秋分の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 10, 13)), '体育の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 11, 3)), '文化の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 11, 23)), '勤労感謝の日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 11, 24)), '勤労感謝の日 振替休日')
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2014, 12, 23)), '天皇誕生日')
