                                                        #Инструкция и краткое пояснение#
#  1) Здесь создано несколько функций проверки VIP статуса, то есть, если у человека он есть, он может об этом узнать по кнопке или же, если он захочет снова ее купить, то программа ему этого не позволит
#  2) Qiwi токен можно получить здесь https://qiwi.com/api - даем вот эти разрешения: Запрос информации о профиле кошелька, Запрос баланса кошелька и Просмотр истории платежей
#  3) желательно создать левый QIWI аккаунт с другим номером, так как на этот номер будут переводиться деньги, а это может привести к тому, что вам могут позвонить
#  4) В поле bot = telebot.TeleBot('') в эти кавычки нужно вставить API бота
#  5) Бот будет работать только пока этот код запущен, если он выключится, все данные у игроков сбросятся

import requests
import json
import config
import telebot
import sqlite3
from telebot import types
from random import randint
import time
import threading
import pyqiwi
vip_status = 1                                  #вип статус уровень 1 (обычный статус изначально у всех пользователей)
diamond = 0             #переменная, которая содержит сколько у пользователя алмазов
Gold = 0                #переменная. которая содержит сколько у пользователя золота
bot = telebot.TeleBot('1034185817:AAE--O78MELHNJv8a0TQVjymTlDS8U27vIA')             #вставляете ваш API телеграмм бота (кавычки не убирайте)
QIWI_token = ''             #токен QIWI аккаунта
QIWI_number = ''        #номер телефона QIWI кошелька
wallet = pyqiwi.Wallet(token=QIWI_token, number=QIWI_number)             #вставляете ваш токен и номер телефона (точнее счета QIWI, куда будут переходить деньги)
a = 1

if a == 1:
    vip_status = 1

elif a == 2:
    vip_status = 2



def diamoning():             #запускаем отдельный поток, в котором будут увеличиваться алмазы каждый час
    global diamond
    while diamond < 10000**10000:                           #создаем бескоенечный цикл(который будет увеличивать количество алмазов)
        time.sleep(3600)
        diamond += 100

def vip_diamoning():
    global diamond
    while diamond < 10000**10000:
        time.sleep(3600)                                     #заносим в скобочки время (в секундах) с какой регулярностью будут появляться алмазы
        diamond += 200


if vip_status == 1:
    t = threading.Thread(target = diamoning)
    t.start()
elif vip_status == 2:
    t = threading.Thread(target = vip_diamoning)
    t.start()

@bot.message_handler(commands=['start'])                    #начало диалога, при отправке /start
def start_message(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)          #создаем пока невидимые кнопки
    markup.row('Описание📝')
    markup.row('Как начать зарабатывать💵')
    markup.row('💎Купить VIP аккаунт💎')
    markup.row('Шахта🏭')
    markup.row('Рынок🎪')
    markup.row('Баланс💸')
    markup.row('Вывести💳💰')
    markup.row('💎Узнать о налачии VIP статуса💎')

    bot.send_message(message.chat.id, 'Приветствуем в нашем боте, желаем удачи в заработке!', parse_mode='html', reply_markup=markup)       #делаем кнопки видимыми


@bot.message_handler(content_types=['text'])                                    #при получении текста
def message_btn(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)          #создаем пока невидимые кнопки
    markup.row('Описание📝')
    markup.row('Как начать зарабатывать💵')
    markup.row('💎Купить VIP аккаунт💎')
    markup.row('Шахта🏭')
    markup.row('Рынок🎪')
    markup.row('Баланс💸')
    markup.row('Вывести💳💰')
    markup.row('💎Узнать о налачии VIP статуса💎')

    if message.text == "Описание📝":                #Если приходит сообщение - описание
        bot.send_message(message.chat.id, 'MineCash Bot - Игра, где у каждого есть возможность заработать реальные деньги, не прикладывая больших усилий💰')

    elif message.text == "Как начать зарабатывать💵":       #если приходит сообщение - как начать зарабатывать
        bot.send_message(message.chat.id, 'Заходи в шахту и добывай алмазы🏭💎')
        bot.send_message(message.chat.id, 'Обменивай алмазы на рынке💰')
        bot.send_message(message.chat.id, 'Заходи во вкладку баланс и выводи деньги💸')

    elif message.text == '💎Купить VIP аккаунт💎':
        global vip_status
        if vip_status == 1:
            button2  = types.ReplyKeyboardMarkup(resize_keyboard = True)
            button2.row('💎Купить VIP статус💎')
            button2.row('Назад⬅️')
            bot.send_message(message.chat.id, 'VIP аккаунт - это привилегия, которая увеличивает добычу алмазов💎 в 2 раза', parse_mode = 'html', reply_markup=button2)
            bot.send_message(message.chat.id, 'Цена VIP статуса 150 рублей')
        elif vip_status == 2:
            button4 = types.ReplyKeyboardMarkup(resize_keyboard = True)          #создаем пока невидимые кнопки
            button4.row('Назад⬅️')
            bot.send_message(message.chat.id, 'VIP статус уже приобретен', parse_mode = 'html', reply_markup=button4)

    elif message.text == '💎Купить VIP статус💎':
        button3  = types.ReplyKeyboardMarkup(resize_keyboard = True)
        button3.row('📍Проверить перевод📍')
        button3.row('Назад⬅️')
        bot.send_message(message.chat.id, 'Переведите 150 рублей на счет: ' + str(QIWI_number))
        bot.send_message(message.chat.id, 'Перед нажатием кнопки прождите 5 секунд (воизбежания ошибок)')
        bot.send_message(message.chat.id, 'Только после выполнения перевода нажмите на кнопку: Проверить оплату', parse_mode = 'html', reply_markup=button3)


    elif message.text == '📍Проверить перевод📍':
        if wallet.balance() == 150:
            global a
            bot.send_message(message.chat.id, '💸Деньги пришли💰')
            bot.send_message(message.chat.id, 'Добыча алмазов увеличина в 2 раза', parse_mode = 'html', reply_markup=markup)
            a = 2

        else:
            bot.send_message(message.chat.id, 'Деньги не пришли, либо сумма перевода составила менее 150 рублей', parse_mode = 'html', reply_markup=markup)



    elif message.text == "Шахта🏭":                     #при получении сообщения - Шахта
        global diamond
        bot.send_message(message.chat.id, 'Здесь работают Ваши шахтеры. Они находят 💎, которые вам необходимо собирать и продавать на рынке.')
        bot.send_message(message.chat.id, 'Шахтеры работают ⛏')
        bot.send_message(message.chat.id, 'Добыли: ' + str(diamond) + "💎")

    elif message.text == "Рынок🎪":                 #при получении сообщения - рынок
        button = types.ReplyKeyboardMarkup(resize_keyboard = True)          #создаем пока невидимые кнопки
        button.row('Обменять💰')
        button.row('Назад⬅️')
        global Gold
        bot.send_message(message.chat.id, 'Рынок — место где можно продать добытые вашими шахтерами алмазы, и получить за них золото💰, которое можно использовать для вывода средств из игры на свой RUB кошелек!💵', parse_mode = 'html', reply_markup=button)
        bot.send_message(message.chat.id, "Текущие курсы обмена:\n100💎 = 1💰")
        bot.send_message(message.chat.id, "У Вас в шахте: " + str(diamond) + "💎")

    elif message.text == "Баланс💸":        #при получении сообщения - баланс
        global Gold
        bot.send_message(message.chat.id, 'Золото: ' + str(Gold) + '💰( руб.)')
        bot.send_message(message.chat.id, 'Алмазы: ' + str(diamond) + '💎')
        bot.send_message(message.chat.id, 'Для вывода у вас должно быть не меньше 250 золота💰')

    elif message.text == "Вывести💳💰":
        if Gold >= 250:                                  #проверяем, есть ли у пользователя 250 золота. если да, то предлагаем выбрать платежную систему
            button2 = types.ReplyKeyboardMarkup(resize_keyboard = True)
            button2.row('Киви/Qiwi')             #создает 2 кнопки с выбором платежной системы ДЛЯ ВЫВОДА СРЕДСТВ
            button2.row('Карта')
            button2.row('Назад⬅️')

            bot.send_message(message.chat.id, 'Выберите платежную систему для вывода', parse_mode = 'html', reply_markup=button2)
        else:               #если на балансе меньше 250 золота, пишет, что недостаточно золота и оставляет пользователя в главном меню
            bot.send_message(message.chat.id, 'У вас недостаточно золота')
            bot.send_message(message.chat.id, 'Для вывода у вас должно быть не меньше 250 золота💰')
            bot.send_message(message.chat.id, "Баланс: " + str(Gold) + '💰')

    elif message.text == 'Обменять💰':
        if diamond < 100:
            bot.send_message(message.chat.id, 'У вас недостаточно алмазов')
            bot.send_message(message.chat.id, 'Текущие курсы обмена:\n100💎 = 1💰')
        elif diamond >= 100:
            Gold = Gold + diamond / 100
            diamond = 0
            bot.send_message(message.chat.id, 'Идет обмен...')
            bot.send_message(message.chat.id, 'Обмен выполнен')
            bot.send_message(message.chat.id, "Узнайте ваш баланс, нажав по соответствующей кнопке", parse_mode = 'html', reply_markup=button)

    elif message.text == '💎Узнать о налачии VIP статуса💎':
        if vip_status == 1:
            bot.send_message(message.chat.id, 'У вас нету VIP статуса')
        elif vip_status == 2:
            bot.send_message(message.chat.id, 'VIP статус приобретен')

    elif message.text == 'Назад⬅️':
        bot.send_message(message.chat.id, 'Возвращаю в главное меню',parse_mode = 'html', reply_markup=markup)

bot.polling(none_stop=True)






