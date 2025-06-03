# -*- coding: utf-8 -*-

import sys
import asyncio
import telepot
import telepot.aio
from datetime import date

import pymysql.cursors	# Подключаем библиотеку для работы с mysql

chat_id = CHAT_ID   #замените на свой id
TOKEN = "TOKEN"
bot = telepot.Bot(TOKEN)

dat = date.today()
today = dat.strftime("%d")
month = dat.strftime("%m")
year = dat.strftime("%Y")
week = dat.weekday()


def to_text_weekday(weekday):
    if weekday == 0:
        return 'Понедельник'
    elif weekday == 1:
        return 'Вторник'
    elif weekday == 2:
        return 'Среда'
    elif weekday == 3:
        return 'Четверг'
    elif weekday == 4:
        return 'Пятница'
    elif weekday == 5:
        return 'Суббота'
    elif weekday == 6:
        return 'Воскресенье'

def read_base():
  try:
    conn = pymysql.connect(host='10.10.10.10', port=3306, user='admin', passwd='admin', db='duty_roster', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT on_friday_avr.`name`, on_friday_avr.time, on_friday_avr.date, on_friday_avr.money FROM on_friday_avr WHERE on_friday_avr.date LIKE '"+str(year)+"-"+str(month)+"-"+str(today)+"' LIMIT 1")
    result = cur.fetchall()
    output = ""
    for row in result:
        output += "⚠️Сегодня дежурные:⚠️\n➡️ *"+ row[0] +"* ⬅️\n"+"Время дежурства:"+ row[1] +"\n"+"Дата: "+ row[2].strftime("%Y-%m-%d") +"\n"+"Оплата: "+ row[3] +"\n"
    bot.sendMessage(chat_id, output , parse_mode='Markdown')
    cur.close()
    conn.close()
  except Exception as e:
    output += "🆘Внимание!🆘\n*Пустая база данных*\n"
    bot.sendMessage(chat_id, output , parse_mode='Markdown')


read_base()

