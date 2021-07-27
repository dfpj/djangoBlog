from . import jalali
from django.utils import timezone

def persian_numbers_converter(numstr):
    numbers={
        "0":"۰",
        "1":"۱",
        "2":"۲",
        "3":"۳",
        "4":"۴",
        "5":"۵",
        "6":"۶",
        "7":"۷",
        "8":"۸",
        "9":"۹",
    }
    for e,p in numbers.items():
        numstr=numstr.replace(e,p)
    return numstr

def jalali_converter(time):
    jmonths=["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    time=timezone.localtime(time)
    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    day=persian_numbers_converter(str(time_to_tuple[0]))
    month=jmonths[time_to_tuple[1]-1]
    year=persian_numbers_converter(str(time_to_tuple[2]))
    hour=persian_numbers_converter(str(time.hour))
    minute=persian_numbers_converter(str(time.minute))
    return f" انتشار : {year}/{month}/{day} , {hour}:{minute}"