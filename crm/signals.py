from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import *
from .bot import *

from django.core.signals import request_finished


@receiver(post_save,sender = Attendance)
def get_activity_coefficient(sender,instance,created, **kwargs):
    user = instance.user
    dates = Attendance.objects.all().filter(user=user)
    working_minutes = 480
    days = 0
    total = 0
    for i in dates:
        if i.time_in and i.time_out is not None:
            days += 1
            datetime1 = datetime.combine(date.today(), i.time_out)
            datetime2 = datetime.combine(date.today(), i.time_in)
            time_elapsed = datetime1 - datetime2
            delta = time_elapsed.total_seconds()
            minutes = int(delta // 60)
            total += minutes
    total_working_minutes = working_minutes * days

    try:
        value = (total * 100) / total_working_minutes
        formatted_string = "{:.2f}".format(value)
        user.activity_coefficient = formatted_string
        return user.save()
    except:
        user.activity_coefficient = 0
        return user.save()


@receiver(post_save,sender = Attendance)
def bot(sender,instance,created,**kwargs):
    print(created)
    send_message(instance)


