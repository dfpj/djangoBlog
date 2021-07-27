from . import jalali
from django.utils import timezone

def jalali_converter(time):
    jmonths=["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
    
    time=timezone.localtime(time)
    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()


    output ="{} {} {} {}:{} ".format(
        time_to_tuple[2],
        jmonths[time_to_tuple[1]-1],
        
        time_to_tuple[0],
        time.hour,
        time.minute
    )
    return output