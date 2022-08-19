# cython: language_level=3

from cpython.datetime cimport date as cydate

cdef list ALL_HOLIDAY_LIST

cdef class BaseHoliday:
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 元日
cdef class NewYear(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 成人の日
cdef class AdultDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 建国記念の日
cdef class FoundationDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 天皇誕生日
cdef class EmperorsBirthday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 春分の日
cdef class VernalEquinoxDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)
    cpdef double _vernal_equinox_day(self, int year)


# みどりの日
cdef class GreeneryDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 昭和の日
cdef class ShowaDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)

# 憲法記念日
cdef class ConstitutionMemorialDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# こどもの日
cdef class ChildrensDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)

# 海の日
cdef class SeaDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 山の日
cdef class MountainDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 敬老の日
cdef class RespectForTheAgedDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 秋分の日
cdef class AutumnEquinoxDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)
    cpdef double _autumn_equinox_day(self, int year)

# 体育の日
cdef class HealthAndSportsDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# スポーツの日
cdef class SportsDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 文化の日
cdef class CultureDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 勤労感謝の日
cdef class LaborThanksgivingDay(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 皇室慶弔行事に伴う祝日
cdef class ExtraHolidays(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 振替休日
cdef class TransferHoliday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)


# 国民の休日
cdef class NationalHoliday(BaseHoliday):
    cpdef bint is_holiday(self, cydate date)
    cpdef str is_holiday_name(self, cydate date)

