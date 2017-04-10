# __author__ = 'lius'

import datetime
from django import template

register = template.Library()

@register.filter()
def time_filter(value,arg):
    datetimeNow = datetime.datetime.now()
    day = (datetimeNow-arg).days
    if day > 0 and day <= 30:
        value += " --" + str(day) + "天前发布"
    elif day > 30 and day <= 365:
        value += " --" + str(day//30) + "个月前发布"
    elif day > 365:
        value += " --" + str(day//30) + "年前发布"
    else:
        sec = (datetimeNow-arg).seconds
        if sec > 3600:
            value += " --" + str(sec//60//60) + "小时前发布"
        elif sec > 60 and sec <= 3600:
            value += " --" + str(sec//60) + "分钟前发布"
        elif sec > 0 and sec <=60:
            value += " --" + str(sec) + "秒前发布"
        else:
            value += " --刚刚发布"
    return value
