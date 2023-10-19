import telebot
from laba_7_functional import schedule, hello, week_number

bot = telebot.TeleBot("6135698102:AAGnYMEM4kX-qqL4AgYxhz5jTBRCHQ_LVs0")

week_day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "nowweek", "nextweek"]
week_day_command = {"/monday": 0, "/tuesday": 1, "/wednesday": 2, "/thursday": 3, "/friday": 4, "/saturday": 5,
                    "/nowweek": 6, "/nextweek": 7}


@bot.message_handler(commands=['start', 'help'])
def start(message):
    """
    при данных командах бот выводит информацию из переменной hello, которая хранится в laba_7_functional.py
    """
    bot.send_message(message.chat.id, hello)


@bot.message_handler(commands=week_day)
def week_list(message):
    """
    при командах, которе находятся в week_day_command, бот выводит рассписание на заданный промежуток времени
    """
    bot.send_message(message.chat.id, schedule(week_day_command[message.text]))


@bot.message_handler(commands=['week'])
def week(messege):
    """
    При данной команде бот выводит какая сейчас неделя
    """
    if week_number() % 2 == 1:
        bot.send_message(messege.chat.id, f"Верхняя неделя, №{week_number()}")
    else:
        bot.send_message(messege.chat.id, f"Нижняя неделя, №{week_number()}")


@bot.message_handler(commands=['mtuci'])
def href_mtuci(messege):
    """
    При данной команде бот выведет ссылку на оф сайт МТУСИ
    """
    bot.send_message(messege.chat.id, "Оф. сайт МТУСИ: https://mtuci.ru/", disable_web_page_preview = True)


@bot.message_handler()
def say(messege):
    """
    Здесь происходит обработка исключений. Если команда не найдена, то бот ответит "Извините, я Вас не понял"
    """
    bot.send_message(messege.chat.id, "Извините, я Вас не понял")


bot.polling(none_stop=True)
