import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

mod = 'clear'


#При открытии бота попадаем сюда. /start
@bot.message_handler(commands=['start', 'Меню'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("Модули")
    item2 = types.KeyboardButton("Экзамены")
    item3 = types.KeyboardButton("Контактная информация")
    item4 = types.KeyboardButton("Календарный учебный график")


    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для того, чтобы подсказывать студентам СТАНКИНА.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(regexp="ГСиТ")
def Data_Professor1(message):
    if mod == '1 модуль':
        bot.send_message(message.chat.id, 'Гипермедийные среды и технологии.\n1-2 практические работы + 1 к/р')
    elif mod == '2 модуль':
        bot.send_message(message.chat.id, 'Гипермедийные среды и технологии.\n3-4 практические работы + 1-4 лабораторные работа + 2-3 к/р(*)')


@bot.message_handler(regexp="ОНИТ")
def Data_Professor1(message):
    if mod == '1 модуль':
        bot.send_message(message.chat.id, 'Основы новых информационных технологий.\n1-2 лабораторные работы')
    elif mod == '2 модуль':
        bot.send_message(message.chat.id, 'Основы новых информационных технологий.\n3 лабораторная работа + телеграм бот(презентация)')


@bot.message_handler(regexp="СТиСРПО")
def Data_Professor1(message):
    if mod == '1 модуль':
        bot.send_message(message.chat.id, 'Современные технологии и средства разработки ПО.\n1-2 лабораторные работы(UML)')
    elif mod == '2 модуль':
        bot.send_message(message.chat.id, 'Современные технологии и средства разработки ПО.\n3 лабораторная работа')


@bot.message_handler(regexp="Методы оптимизации")
def Data_Professor1(message):
    if mod == '1 модуль':
        bot.send_message(message.chat.id, 'Методы оптимизации.\n1-4 семинары + 1-2 лабораторные работы')
    elif mod == '2 модуль':
        bot.send_message(message.chat.id, 'Методы оптимизации.\n5-8 семинары + 3-4 лабораторные работы')


@bot.message_handler(regexp="Операционные системы")
def Data_Professor1(message):
    if mod == '1 модуль':
        bot.send_message(message.chat.id, 'Операционные системы.\n1-2 лабораторные работы')
    elif mod == '2 модуль':
        bot.send_message(message.chat.id, 'Операционные системы.\n3-5 лабораторные работы')


@bot.message_handler(regexp="Коган Ю.Г.")
def Data_Professor1(message):
    bot.send_message(message.chat.id, "Коган Ю.Г.\nyugr.kogan@outlook.com")


@bot.message_handler(regexp="Кузовкин К.Н.")
def Data_Professor2(message):
    bot.send_message(message.chat.id, "Кузовкин К.Н.\nkkn777@yandex.ru")


@bot.message_handler(regexp="Третяк И.С.")
def Data_Professor3(message):
    bot.send_message(message.chat.id, "Третяк И.С.\n+7(926)120-60-02")


@bot.message_handler(regexp="Пушкин А.Ю.")
def Data_Professor(message):
    bot.send_message(message.chat.id, "Пушкин А.Ю.\n+7(916)631-02-16")


@bot.message_handler(regexp="Гаврилов А.Г.")
def Data_Professor5(message):
    bot.send_message(message.chat.id, "Гаврилов А.Г.\nДискорд или ВК:)")


@bot.message_handler(regexp="Экзамены")
def Exs(message):
    bot.send_photo(message.chat.id, photo=open('firstphoto.jpg', 'rb')) #отправляем фотографию


@bot.message_handler(regexp="Деканат")
def Dekanat(message):
    bot.send_message(message.chat.id, "dekanat@stankin.ru\n+7(499)973-38-34")


@bot.message_handler(regexp="Преподаватели")
def Professors(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Коган Ю.Г.")
    item2 = types.KeyboardButton("Кузовкин К.Н.")
    item3 = types.KeyboardButton("Третяк И.С.")
    item4 = types.KeyboardButton("Пушкин А.Ю.")
    item5 = types.KeyboardButton("Гаврилов А.Г.")
    item6 = types.KeyboardButton("/Меню")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Выберите преподавателя", reply_markup=markup)


@bot.message_handler(regexp="Календарный учебный график")
def curriculum(message):
    bot.send_photo(message.chat.id, photo=open('secondphoto.jpg', 'rb')) #отправляем фото


@bot.message_handler(regexp="Контактная информация")
def Contact_Data(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)# создаём клавиатуру
    item1 = types.KeyboardButton("Деканат")
    item2 = types.KeyboardButton("Преподаватели")
    item3 = types.KeyboardButton("/Меню")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Нажмите на одну из кнопок", reply_markup=markup)


@bot.message_handler(regexp="Модули")
def Moduls(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1 модуль")# 1 кнопка
    item2 = types.KeyboardButton("2 модуль")# 2 кнопка

    markup.add(item1, item2) #добавляем кнокпи в кллавиатуру

    bot.send_message(message.chat.id, "Выберите модуль", reply_markup=markup)# Отправляем сообщение о показываем клавиатуру3


@bot.message_handler(regexp="1 модуль")
def modul1(message):
    global mod # для опредления в каком модуле мы сейчас находимся
    mod = '1 модуль'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ГСиТ")
    item2 = types.KeyboardButton("ОНИТ")
    item3 = types.KeyboardButton("СТиСРПО")
    item4 = types.KeyboardButton("Методы оптимизации")
    item5 = types.KeyboardButton("Операционные системы")
    item6 = types.KeyboardButton("/Меню")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Выберите предмет", reply_markup=markup)


@bot.message_handler(regexp="2 модуль")
def modul2(message):
    global mod
    mod = '2 модуль'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ГСиТ")
    item2 = types.KeyboardButton("ОНИТ")
    item3 = types.KeyboardButton("СТиСРПО")
    item4 = types.KeyboardButton("Методы оптимизации")
    item5 = types.KeyboardButton("Операционные системы")
    item6 = types.KeyboardButton("/Меню")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, "Выберите предмет:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def first(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


bot.polling()