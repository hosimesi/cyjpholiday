# cython: language_level=3

import calendar
import datetime
from cpython.datetime cimport date as cydate


cdef cydate _week_day(cydate date, int week, int weekday)
