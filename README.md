# CYPHoliday

[![image](https://img.shields.io/pypi/l/jpholiday.svg)](https://pypi.org/project/jpholiday/)
[![image](https://img.shields.io/pypi/pyversions/jpholiday.svg)](https://pypi.org/project/jpholiday/)


cythonで実装したjpholiday


## Notice
暫定では、以下の2つのメソッドのみ対応しています。
- is_holiday
- is_holiday_name

また、どちらもdatetime型のみ受けいれます。

## Installation


```bash
pip install cyjpholiday
```

## Sample Code
### 指定日の祝日名を取得
```python
import cyjpholiday
import datetime as dt


# datetime.datetime
jpholiday.is_holiday_name(dt.datetime(2017, 1, 1, 1, 1, 1))
> '元日'
jpholiday.is_holiday_name(dt.datetime(2017, 1, 2, 1, 1, 1))
> '振替休日'
jpholiday.is_holiday_name(dt.datetime(2017, 1, 3, 1, 1, 1))
> None
```

# fork元
https://github.com/Lalcs/jpholiday
