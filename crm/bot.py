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
            text = f'{user.full_name} закончил рабочий день.\nДата : {attendance.date}\nВремя ухода : {attendance.time_out} '
            client.send_message(channel_id, text)


def send_standup(standup):
    text = f'Опрос :\n\n{standup.attendance.user.full_name}\n{standup.q1} '
    client.send_message(channel_id,text)