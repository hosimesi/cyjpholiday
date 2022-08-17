# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2022(unittest.TestCase):
    def test_holiday(self):
        """
        2022年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetimetime(2022, 1, 1, 1, 1, 1)), "元日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 1, 10, 1, 1, 1)), "成人の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 2, 11, 1, 1, 1)), "建国記念の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 2, 23, 1, 1, 1)), "天皇誕生日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 3, 21, 1, 1, 1)), "春分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 4, 29, 1, 1, 1)), "昭和の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 5, 3, 1, 1, 1)), "憲法記念日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 5, 4, 1, 1, 1)), "みどりの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 5, 5, 1, 1, 1)), "こどもの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 7, 18, 1, 1, 1)), "海の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 8, 11, 1, 1, 1)), "山の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 9, 19, 1, 1, 1)), "敬老の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 9, 23, 1, 1, 1)), "秋分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 10, 10, 1, 1, 1)), "スポーツの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 11, 3, 1, 1, 1)), "文化の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2022, 11, 23, 1, 1, 1)), "勤労感謝の日")
