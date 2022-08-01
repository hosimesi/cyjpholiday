# cython: language_level=3
# cython: profile=True

from .holiday cimport ALL_HOLIDAY_LIST, BaseHoliday

from cpython.datetime cimport datetime as cydatetime, date as cydate
from datetime import datetime
from .utils cimport _week_day

cpdef bint is_holiday(value: datetime):
    """
    その日が祝日かどうかを返します。
    """
    # Covert
    cdef:
        cydate cy_date = _to_date(value=value)
        BaseHoliday holiday_instance

    for holiday_instance in ALL_HOLIDAY_LIST:
        if holiday_instance.is_holiday(cy_date):
            return True

    return False

cpdef str is_holiday_name(value: datetime):
    """
    その日の祝日名を返します。
    """
    # Covert
    cdef cydate cy_date = _to_date(value=value)

    for holiday_instance in ALL_HOLIDAY_LIST:
        if holiday_instance.is_holiday_name(cy_date):
            return holiday_instance.is_holiday_name(cy_date)

    return None


cpdef list year_holidays(int year):
    """
    その年の祝日日、祝日名を返します。
    """
    cdef cydate cy_date = datetime.date(year, 1, 1)

    cdef list output = []
    while cy_date.year == year:
        name = is_holiday_name(cy_date)
        if name is not None:
            output.append((cy_date, name))

        cy_date = cy_date + datetime.timedelta(days=1)

    return output

cpdef list month_holidays(int year, int month):
    """
    その月の祝日日、祝日名を返します。
    """
    cdef cydate cy_date = datetime.date(year, month, 1)

    cdef list output = []
    while cy_date.month == month:
        name = is_holiday_name(cy_date)
        if name is not None:
            output.append((cy_date, name))

        cy_date = cy_date + datetime.timedelta(days=1)

    return output

cpdef list holidays(cydate start_date, cydate end_date):
    """
    指定された期間の祝日日、祝日名を返します。
    """

    # Covert
    cdef cydate cy_start_date = _to_date(start_date)
    cdef cydate cy_end_date = _to_date(end_date)

    cdef list output = []
    while cy_start_date <= cy_end_date:
        name = is_holiday_name(cy_start_date)
        if name is not None:
            output.append((cy_start_date, name))

        cy_start_date = cy_start_date + datetime.timedelta(days=1)

    return output


cdef cydate _to_date(cydatetime value):
    """
    datetime型をdate型へ変換
    それ以外は例外
    """
    if isinstance(value, cydatetime):
        return value.date()
    elif isinstance(value, cydate):
        return value
