# coding: utf-8
import datetime as dt
import unittest

import cyjpholiday


class TestYear2023(unittest.TestCase):
    def test_holiday(self):
        """
        2023年祝日
        """
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 1, 1, 1, 1, 1)), "元日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 1, 2, 1, 1, 1)), "振替休日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 1, 9, 1, 1, 1)), "成人の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 2, 11, 1, 1, 1)), "建国記念の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 2, 23, 1, 1, 1)), "天皇誕生日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 3, 21, 1, 1, 1)), "春分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 4, 29, 1, 1, 1)), "昭和の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 5, 3, 1, 1, 1)), "憲法記念日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 5, 4, 1, 1, 1)), "みどりの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 5, 5, 1, 1, 1)), "こどもの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 7, 17, 1, 1, 1)), "海の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 8, 11, 1, 1, 1)), "山の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 9, 18, 1, 1, 1)), "敬老の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 9, 23, 1, 1, 1)), "秋分の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 10, 9, 1, 1, 1)), "スポーツの日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 11, 3, 1, 1, 1)), "文化の日")
        self.assertEqual(cyjpholiday.is_holiday_name(dt.datetime(2023, 11, 23, 1, 1, 1)), "勤労感謝の日")
