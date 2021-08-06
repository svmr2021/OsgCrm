import telebot
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
client = telebot.TeleBot(token)

channel_id = os.getenv('CHANNEL_ID')


def send_message(attendance):
    user = attendance.user
    if attendance.time_in is not None:
        if not attendance.finished:
            text = f'{user.full_name} начал рабочий день.\nДата : {attendance.date}\nВремя прибытия : {attendance.time_in} '
            client.send_message(channel_id,text)
        elif attendance.finished:
            text = f'{user.full_name} закончил рабочий день.\nДата : {attendance.date}\nВремя ухода : {attendance.time_out}\n\n' \
                   f'Какая работа была сегодня проделана? - {attendance.standup.answer} \n'
            client.send_message(channel_id, text,parse_mode='html')


def send_standup(standup,created):
    late = 'Причина опоздания'
    reason = 'Не опоздал'
    if created:
        if standup.attendance.is_late:
            reason = f'{standup.reason}'
        text = f'{standup.attendance.user.full_name}\n' \
               f'<b>Опрос</b>:\n' \
               f'<b>{late}</b>:{reason}\n' \
               f'<b>Как Ваше самочувствие?</b> - {standup.q1}\n' \
               f'<b>Над чем вы сегодня будете работать?</b> - {standup.q1}\n' \
               f'<b>Есть ли факторы,которые могут блокировать рабочий прогресс?</b> - {standup.q3}'
        client.send_message(channel_id,text,parse_mode='html')