# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2021(unittest.TestCase):
    def test_holiday(self):
        """
        2021年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 1, 1)), "元日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 1, 11)), "成人の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 2, 11)), "建国記念の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 2, 23)), "天皇誕生日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 3, 20)), "春分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 4, 29)), "昭和の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 5, 3)), "憲法記念日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 5, 4)), "みどりの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 5, 5)), "こどもの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 7, 22)), "海の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 7, 23)), "スポーツの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 8, 8)), "山の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 8, 9)), "山の日 振替休日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 9, 20)), "敬老の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 9, 23)), "秋分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 11, 3)), "文化の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2021, 11, 23)), "勤労感謝の日")
