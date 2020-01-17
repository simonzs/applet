# -*- encoding: utf-8 -*-
'''
@File    :   attime.py
@Time    :   2019/12/03 20:14:07
@Author  :   Simon 
@Version :   1.0
@Desc    :   None
'''

# here put the import lib


import pytz
import time
from pytz import timezone
from time import daylight
from datetime import datetime, timedelta


"""
Copy form graphite.
"""

"""Copyright 2008 Orbitz WorldWide

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]
weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

default_timezone = timezone("Asia/Shanghai")
# default_timezone = timezone("UTC")


def parseATTime(s, tzinfo=None):
    tzinfo = _ensure_timezone(tzinfo)

    if isinstance(s, (int, float)):
        return from_timestamp_s(s, tzinfo)
    if len(s) == 14:
        dt = parseATTime(s[:8])
        offset = timedelta(
            hours=int(s[8:10]), minutes=int(s[10:12]), seconds=int(s[12:14])
        )
        return dt + offset
    s = s.strip().lower().replace("_", "").replace(",", "").replace(" ", "")
    if s.isdigit():
        if len(s) == 8 and int(s[:4]) > 1900 and int(s[4:6]) < 13 and int(s[6:]) < 32:
            return parseTimeReference(s).replace(tzinfo=tzinfo)
        else:
            return from_timestamp_s(int(s), tzinfo)

    elif ":" in s and len(s) == 13:
        return tzinfo.localize(datetime.strptime(s, "%H:%M%Y%m%d"), daylight)
    offset, ref = parse_offset(s)
    return (parseTimeReference(ref) + parseTimeOffset(offset)).replace(tzinfo=tzinfo)


def parse_offset(s):
    if "+" in s:
        ref, offset = s.split("+", 1)
        offset = "+" + offset
    elif "-" in s:
        ref, offset = s.split("-", 1)
        offset = "-" + offset
    else:
        ref, offset = s, ""
    return offset, ref


def _ensure_timezone(tzinfo):
    if tzinfo is None:
        tzinfo = timezone("Asia/Shanghai")
    elif isinstance(tzinfo, str):
        tzinfo = timezone(tzinfo)
    return tzinfo


def from_timestamp_s(ts, tzinfo):
    if ts > 253402271999:
        ts = ts / 1000

    dt = datetime.fromtimestamp(ts)
    return tzinfo.localize(dt, is_dst=True)


def parseTimeReference(ref):
    if not ref or ref == "now":
        return datetime.utcnow().replace(tzinfo=pytz.utc)

    # Time-of-day reference
    ref, ref_date = parse_reference_date(ref)

    # Day reference
    if ref in ("yesterday", "today", "tomorrow"):  # yesterday, today, tomorrow
        if ref == "yesterday":
            ref_date = ref_date - timedelta(days=1)
        elif ref == "tomorrow":
            ref_date = ref_date + timedelta(days=1)
    elif ref.count("/") == 2:  # MM/DD/YY[YY]
        ref_date = handle_mdy(ref, ref_date)
    elif len(ref) == 8 and ref.isdigit():  # YYYYMMDD
        ref_date = replace_date(ref_date, int(ref[:4]), int(ref[4:6]), int(ref[6:8]))
    elif ref[:3] in months:  # MonthName DayOfMonth
        ref_date = handle_month_name(ref, ref_date)
    elif ref[:3] in weekdays:  # DayOfWeek (Monday, etc)
        ref_date = handle_day_of_week(ref_date, ref)
    elif ref:
        raise Exception("Unknown day reference")
    return ref_date


def handle_day_of_week(ref_date, ref):
    today_day_name = ref_date.strftime("%a").lower()[:3]
    today = weekdays.index(today_day_name)
    two_weeks = weekdays * 2
    day_offset = today - two_weeks.index(ref[:3])
    if day_offset < 0:
        day_offset += 7
    ref_date -= timedelta(days=day_offset)
    return ref_date


def handle_month_name(ref, ref_date):
    month = months.index(ref[:3]) + 1
    if ref[-2:].isdigit():
        day = int(ref[-2])
    elif ref[-1:].isdigit():
        day = int(ref[-1:])
    else:
        raise Exception("Day of month required after month name")
    ref_date = replace_date(ref_date, None, month, day)
    return ref_date


def handle_mdy(ref, ref_date):
    """处理 MM/DD/YY[YY] 格式日期
    """
    m, d, y = map(int, ref.split("/"))
    if y < 1900:
        y += 1900
    if y < 1970:
        y += 100
    ref_date = replace_date(ref_date, y, m, d)
    return ref_date


def parse_reference_date(ref):
    # Time-of-day reference
    i = ref.find(":")
    hour, min = 0, 0
    if i != -1:
        hour = int(ref[:i])
        min = int(ref[i + 1 : i + 3])
        ref = ref[i + 3 :]
        if ref[:2] == "am":
            ref = ref[2:]
        elif ref[:2] == "pm":
            hour = (hour + 12) % 24
            ref = ref[2:]
    if ref.startswith("noon"):
        hour, min = 12, 0
        ref = ref[4:]
    elif ref.startswith("midnight"):
        hour, min = 0, 0
        ref = ref[8:]
    elif ref.startswith("teatime"):
        hour, min = 16, 0
        ref = ref[7:]

    ref_date = datetime.utcnow().replace(
        hour=hour, minute=min, second=0, tzinfo=pytz.utc
    )
    return ref, ref_date


def replace_date(date, year, month, day):
    if year is not None:
        try:
            date = date.replace(year=year)
        except ValueError:  # Feb 29.
            date = date.replace(year=year, day=28)
    try:
        date = date.replace(month=month)
        date = date.replace(day=day)
    except ValueError:  # day out of range for month, or vice versa
        date = date.replace(day=day)
        date = date.replace(month=month)
    return date


def parseTimeOffset(offset):
    if not offset:
        return timedelta()

    t = timedelta()

    if offset[0].isdigit():
        sign = 1
    else:
        sign = {"+": 1, "-": -1}[offset[0]]
        offset = offset[1:]

    while offset:
        i = 1
        while offset[:i].isdigit() and i <= len(offset):
            i += 1
        num = int(offset[: i - 1])
        offset = offset[i - 1 :]
        i = 1
        while offset[:i].isalpha() and i <= len(offset):
            i += 1
        unit = offset[: i - 1]
        offset = offset[i - 1 :]
        unit_string = getUnitString(unit)
        if unit_string == "months":
            unit_string = "days"
            num = num * 30
        if unit_string == "years":
            unit_string = "days"
            num = num * 365
        t += timedelta(**{unit_string: sign * num})

    return t


def getUnitString(s):
    if s.startswith("s"):
        return "seconds"
    if s.startswith("min"):
        return "minutes"
    if s.startswith("h"):
        return "hours"
    if s.startswith("d"):
        return "days"
    if s.startswith("w"):
        return "weeks"
    if s.startswith("mon"):
        return "months"
    if s.startswith("y"):
        return "years"
    raise Exception("Invalid offset unit '%s'" % s)


def get_day_timestamp(ts, tzinfo=None):
    """获取所给POSIX时间戳，在给定时区下的日期下的POSIX时间戳

    :param ts:
    :param tzinfo:
    :return:
    """
    cur = _get_day(int(ts), tzinfo)
    return cur.timestamp()


def get_daytime(ts, tzinfo=None):
    """获取所给POSIX时间戳，在给定时区下的日期，yyyymmdd格式。

    :param ts:
    :param tzinfo:
    :return:
    """
    cur = _get_day(int(ts), tzinfo)
    return cur.year * 10000 + cur.month * 100 + cur.day


def _get_day(ts, tzinfo=None):
    if tzinfo is None:
        tzinfo = default_timezone
    cur = datetime.fromtimestamp(ts,tzinfo)
    # tzinfo.localize(cur)
    delta = timedelta(seconds=cur.second, minutes=cur.minute, hours=cur.hour)
    cur -= delta
    return cur

def _get_one_day_timestamp(_day=1):
    return timedelta(days=_day).total_seconds()

def get_daytime_timestamp(ts, tzinfo=None):
    ts = int(get_day_timestamp(int(ts), tzinfo))
    return str(get_daytime(ts, tzinfo))

def get_current_time_ms():
    return int(time.time() * 1000)

