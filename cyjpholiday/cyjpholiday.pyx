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
    cdef:
        cydate cy_date = _to_date(value=value)
        BaseHoliday holiday_instance

    for holiday_instance in ALL_HOLIDAY_LIST:
        if holiday_instance.is_holiday_name(cy_date):
            return holiday_instance.is_holiday_name(cy_date)

    return None

cdef cydate _to_date(cydatetime value):
    """
    datetime型をdate型へ変換
    それ以外は例外
    """
    if isinstance(value, cydatetime):
        return value.date()
    elif isinstance(value, cydate):
        return value
