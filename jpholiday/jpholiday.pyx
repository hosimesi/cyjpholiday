# cython: language_level=3
# cython: profile=True


from .holiday cimport ALL_HOLIDAY_LIST

from cpython.datetime cimport datetime as cydatetime, date as cydate
from datetime import datetime
from .utils cimport _week_day

# 今dynaで使っているのはここのみ。このis_holidayはpythonから呼び出す必要があるため、defで定義する
cpdef is_holiday(value: datetime):
    """
    その日が祝日かどうかを返します。
    """

    # Covert
    cdef cydate cy_date = _to_date(value=value)

    for holiday_instance in ALL_HOLIDAY_LIST:
        if holiday_instance.is_holiday(cy_date):
            return True

    return False


cdef cydate _to_date(cydatetime value):
    """
    datetime型をdate型へ変換
    それ以外は例外
    """
    if isinstance(value, cydatetime):
        return value.date()
    elif isinstance(value, cydate):
        return value
    # raise JPHolidayTypeError("is type datetime or date isinstance only.")
