# cython: language_level=3

import math
# from libcpp cimport bool as bint

from .utils cimport _week_day
from cpython.datetime cimport datetime as cydatetime, date as cydate
import datetime
#

cdef list ALL_HOLIDAY_LIST = [
    NewYear(),
    AdultDay(),
    FoundationDay(),
    EmperorsBirthday(),
    EmperorsBirthday(),
    VernalEquinoxDay(),
    GreeneryDay(),
    ShowaDay(),
    ConstitutionMemorialDay(),
    ChildrensDay(),
    SeaDay(),
    MountainDay(),
    RespectForTheAgedDay(),
    AutumnEquinoxDay(),
    HealthAndSportsDay(),
    SportsDay(),
    CultureDay(),
    LaborThanksgivingDay(),
    ExtraHolidays(),
    TransferHoliday(),
    NationalHoliday()
]

cdef class BaseHoliday:
    cpdef bint is_holiday(self, cydate date):
        return False

    cpdef str is_holiday_name(self, cydate date):
        return ""


cdef class OriginalHoliday:
    cpdef bint is_holiday(self, cydate date):
        return False

    cpdef str is_holiday_name(self, cydate date):
        return ""



# 元日
cdef class NewYear(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 1 and date.day == 1:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "元日"


# 成人の日
cdef class AdultDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year <= 1999 and date.month == 1 and date.day == 15:
            return True
        elif date.year >= 2000 and date.month == 1 and date.day == _week_day(date, 2, 1).day:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "成人の日"


# 建国記念の日
cdef class FoundationDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year >= 1967 and date.month == 2 and date.day == 11:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "建国記念の日"


# 天皇誕生日
cdef class EmperorsBirthday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        # 1948-1988年
        if date.year in range(1948, 1988 + 1) and date.month == 4 and date.day == 29:
            return True
        # 1988-2018年
        # 2019: 国民の祝日に関する法律(昭和23年法律第178号)の一部改正
        elif date.year in range(1988, 2018 + 1) and date.month == 12 and date.day == 23:
            return True
        # 2019: 国民の祝日に関する法律(昭和23年法律第178号)の一部改正
        elif date.year >= 2020 and date.month == 2 and date.day == 23:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "天皇誕生日"


# 春分の日
cdef class VernalEquinoxDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 3 and date.day == self._vernal_equinox_day(date.year):
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "春分の日"

    cpdef double _vernal_equinox_day(self, int year):
        """
        春季皇霊祭: 1879-1947
        春分の日: 1948
        春分の日の日付を返します。
        http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
        """

        if year <= 1948:
            return 0

        if year >= 1851 and year <= 1899:
            i = 19.8277
        elif year >= 1900 and year <= 1979:
            i = 20.8357
        elif year >= 1980 and year <= 2099:
            i = 20.8431
        elif year >= 2100 and year <= 2150:
            i = 21.8510
        else:
            i = 0

        return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))


# みどりの日
cdef class GreeneryDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year >= 1989 and date.year <= 2006 and date.month == 4 and date.day == 29:
            return True
        elif date.year >= 2007 and date.month == 5 and date.day == 4:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "みどりの日"


# 昭和の日
cdef class ShowaDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year >= 2007 and date.month == 4 and date.day == 29:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "昭和の日"


# 憲法記念日
cdef class ConstitutionMemorialDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 5 and date.day == 3:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "憲法記念日"


# こどもの日
cdef class ChildrensDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 5 and date.day == 5:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "こどもの日"


# 海の日
cdef class SeaDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 7, 23):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 7, 22):
                return True

            return False

        if date.year >= 1996 and date.month == 7 and date.year <= 2002 and date.day == 20:
            return True
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        elif date.year >= 2003 and date.month == 7 and date.day == _week_day(date, 3, 1).day:
            return True


        return False

    cpdef str is_holiday_name(self, cydate date):
        return "海の日"


# 山の日
cdef class MountainDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 8, 10):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 8, 8):
                return True

            return False

        # 2016: 国民の祝日に関する法律の一部を改正する法律(平成26年法律第43号)
        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        if date.year >= 2016 and date.month == 8 and date.day == 11:
            return True

        return False

    cpdef str is_holiday_name(self, cydate date):
        return "山の日"


# 敬老の日
cdef class RespectForTheAgedDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year >= 1966 and date.year <= 2002 and date.month == 9 and date.day == 15:
            return True
        elif date.year >= 2003 and date.month == 9 and date.day == _week_day(date, 3, 1).day:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "敬老の日"


# 秋分の日
cdef class AutumnEquinoxDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 9 and date.day == self._autumn_equinox_day(date.year):
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "秋分の日"

    cpdef double _autumn_equinox_day(self, int year):
        """
        秋分の日の日付を返します。
        秋季皇霊祭: 1879-1947
        秋分の日: 1948
        http://mt-soft.sakura.ne.jp/kyozai/excel_high/200_jissen_kiso/60_syunbun.htm
        """

        if year <= 1948:
            return 0

        if year >= 1851 and year <= 1899:
            i = 22.2588
        elif year >= 1900 and year <= 1979:
            i = 23.2588
        elif year >= 1980 and year <= 2099:
            i = 23.2488
        elif year >= 2100 and year <= 2150:
            i = 24.2488
        else:
            i = 0

        return math.floor(i + 0.242194 * (year - 1980) - math.floor((year - 1980) / 4))


# 体育の日
cdef class HealthAndSportsDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.year >= 1966 and date.year <= 1999 and date.month == 10 and date.day == 10:
            return True
        elif date.year >= 2000 and date.year <= 2019 and date.month == 10 and date.day == _week_day(date, 2,
                                                                                                          1).day:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "体育の日"


# スポーツの日
cdef class SportsDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        # 2020: 国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year == 2020:
            if date == datetime.date(2020, 7, 24):
                return True

            return False

        # 2021: 五輪特別措置法改正案
        if date.year == 2021:
            if date == datetime.date(2021, 7, 23):
                return True

            return False

        # 2020: 国民の祝日に関する法律の一部を改正する法律(平成30年法律第57号)
        #       国民の祝日に関する法律(昭和23年法律第178号)の特例
        if date.year >= 2020 and date.month == 10 and date.day == _week_day(date, 2, 1).day:
            return True

        return False

    cpdef str is_holiday_name(self, cydate date):
        return "スポーツの日"


# 文化の日
cdef class CultureDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 11 and date.day == 3:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "文化の日"


# 勤労感謝の日
cdef class LaborThanksgivingDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if date.month == 11 and date.day == 23:
            return True
        return False

    cpdef str is_holiday_name(self, cydate date):
        return "勤労感謝の日"


# 皇室慶弔行事に伴う祝日
cdef class ExtraHolidays(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if self.is_holiday_name(date) is None:
            return False
        return True

    cpdef str is_holiday_name(self, cydate date):
        if date == datetime.date(1959, 4, 10):
            return "皇太子・明仁親王の結婚の儀"
        elif date == datetime.date(1989, 2, 24):
            return "昭和天皇の大喪の礼"
        elif date == datetime.date(1990, 11, 12):
            return "即位の礼正殿の儀"
        elif date == datetime.date(1993, 6, 9):
            return "皇太子・皇太子徳仁親王の結婚の儀"
        elif date == datetime.date(2019, 5, 1):
            return "天皇の即位の日"
        # 2019: 天皇の即位の日及び即位礼正殿の儀の行われる日を休日とする法律
        elif date == datetime.date(2019, 10, 22):
            return "即位礼正殿の儀"
        return None


# 振替休日
cdef class TransferHoliday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):
        if self.is_holiday_name(date) is None:
            return False
        return True

    cpdef str is_holiday_name(self, cydate date):
        if date.year < 1973:
            return None

        # GW
        if date.year > 2006 and date.month == 5 and date.day == 6 and date.isoweekday() in (2, 3):
            for holiday in ALL_HOLIDAY_LIST:
                if holiday.__class__.__name__ == self.__class__.__name__:
                    continue

                if isinstance(holiday, NationalHoliday):
                    continue

                if isinstance(holiday, OriginalHoliday):
                    continue

                if holiday.is_holiday((date + datetime.timedelta(days=-date.isoweekday()))):
                    return "{} {}".format(
                        holiday.is_holiday_name((date + datetime.timedelta(days=-date.isoweekday()))),
                        "振替休日")

        # 月曜日でない
        if date.isoweekday() != 1:
            return None

        # GW以外
        for holiday in ALL_HOLIDAY_LIST:
            if holiday.__class__.__name__ == self.__class__.__name__:
                continue

            if isinstance(holiday, NationalHoliday):
                continue

            if isinstance(holiday, OriginalHoliday):
                continue

            if holiday.is_holiday((date + datetime.timedelta(days=-1))):
                return "{} {}".format(holiday.is_holiday_name((date + datetime.timedelta(days=-1))),
                                      "振替休日")


# 国民の休日
cdef class NationalHoliday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date):

        if date.isoweekday() == 7:
            return False

        result = {
            "old": False,
            "new": False,
        }

        for holiday in ALL_HOLIDAY_LIST:
            if holiday.__class__.__name__ == self.__class__.__name__:
                continue

            if isinstance(holiday, OriginalHoliday):
                continue

            if holiday.is_holiday((date + datetime.timedelta(days=-1))):
                result["old"] = True
            if holiday.is_holiday((date + datetime.timedelta(days=1))):
                result["new"] = True

            if list(result.values()) == [True, True]:
                return True

        return False

    cpdef str is_holiday_name(self, cydate date):
        return "国民の休日"
