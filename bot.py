import requests
import random

import telebot
from bs4 import BeautifulSoup as b
URL = 'https://www.anekdot.ru/last/good/' # страница для выгрузки
ARI_KEY = '5361434260:AAHH4TLnsAZh2X-5Bl6qS5YiV-avLfNAVOM'
def parser(url):
    r = requests.get(url) # get запрос
    #print(r.status_code) # проверяем ответ от сервера
    #print(r.text) # выгружаем все содержимое страниц
    soup = b(r.text, 'html.parser') # парсим всесь тест в соуп
    anekdots = soup.find_all('div', class_='text') # сjздаем коллекцию див с классом тег
    return [c.text for c in anekdots] # возвращенем очищенный текс из text с помошью цикла
list_anekdot = parser(URL)
random.shuffle(list_anekdot) # перемешиваем анекдоты
# далее создает токинг бота Gvildisyn_bot

bot = telebot.TeleBot(ARI_KEY)
@bot.message_handler(commands = ['начать'])
def hello(message):
    bot.send_message(message.chat.id, 'Что бы посмеяться введите любую цифру:') # функция созвращае пользователю по его id свежий анекдот
@bot.message_handler(content_types = ['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_anekdot[0])
        del list_anekdot[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')
bot.polling() # для обновления запросов от всех пользователей


