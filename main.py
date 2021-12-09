# @komlev_artem_bot
import telebot
from telebot import types
token = None
with open("token.txt") as f:
    token = f.read().strip()

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Новости", "/help", "/Расписание")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежие новости МТУСИ? Или узнать расписание своих занятий?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Новости", "/help", "/Расписание")
    bot.send_message(message.chat.id, 'Я могу показать тебе главные новости МТУСИ или твоё актуальное расписание: напиши /Новости или /Расписание', reply_markup=keyboard)

@bot.message_handler(commands=['Новости'])
def news(message):
    bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')

@bot.message_handler(commands=['Расписание'])
def schedule1(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "/help")
    bot.send_message(message.chat.id, 'Тогда напиши мне день недели', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def schedule2(message):
    if message.text.lower() == "понедельник":
        bot.send_message(message.chat.id, ' 9:30-11:05 - Нет \n11:20-12:55 - Физическая культура \n13:10-14:45 - Вычислительная техника\n15:25-17:00 - Иностранный язык\n17:15-18:50 - Компьютерная графика')
    elif message.text.lower() == "вторник":
        bot.send_message(message.chat.id, ' 9:30-11:05 - Нет \n11:20-12:55 - Нет\n13:10-14:45 - Физическая культура \n15:25-17:00 - Философия\n17:15-18:50 - Введение в ИТ / Философия')
    elif message.text.lower() == "среда":
        bot.send_message(message.chat.id, ' 9:30-11:05 - Нет \n11:20-12:55 - Высшая математика\n13:10-14:45 - АГиЛА\n15:25-17:00 - Введение в ИТ\n17:15-18:50 - Введение в ИТ')
    elif message.text.lower() == "четверг":
        bot.send_message(message.chat.id, ' 9:30-11:05 - Нет \n11:20-12:55 - Нет \n13:10-14:45 - Информационная экология\n15:25-17:00 - Вычислительная техника\n17:15-18:50 - Компьютерная графика')
    elif message.text.lower() == "пятница":
        bot.send_message(message.chat.id, 'СРС')
    elif message.text.lower() == "суббота":
        bot.send_message(message.chat.id, ' 9:30-11:05 - Нет \n11:20-12:55 - Высшая математика \n13:10-14:45 - АГиЛА\n15:25-17:00 - Нет \n17:15-18:50 - Нет ')



bot.polling(none_stop=True)


