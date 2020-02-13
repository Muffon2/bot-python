import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Привет, Тимурка, ты лох кста')
        bot.send_message(message.chat.id, 'Напиши привет или /help')

@bot.message_handler(commands=['help', 'anime'])
def send_text(message):
    if message.text.lower() == '/help':
       bot.send_message(message.chat.id, 'Ясно, тупо анальный червяк')
       bot.send_message(message.chat.id, 'Напиши привет падла')
    elif message.text.lower() == '/anime':
        bot.send_message(message.chat.id, 'Вот тебе новинки чертила, кста с 14 февраля')
        bot.send_message(message.chat.id, 'Грабитель - http://fanserial.net/47660-grabitel-6-seriya-hunch.html')
        bot.send_message(message.chat.id, 'Дендограм - https://anistar.org/7032-beskonechnyy-dendrogram-infinite-dendrogram.html')
        bot.send_message(message.chat.id, 'Дефка Герой Щита - https://anistar.org/7029-ne-lyublyu-bol-poetomu-sobirayus-vlozhit-vse-v-zaschitu-itai-no-wa-iya-nano-de-bougyoryoku-ni-kyokufuri-shitai-to-omoimasu.html')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет лох, напиши 300')
    elif message.text.lower() == '300':
        bot.send_message(message.chat.id, 'Отсоси у тракториста, теперь пиши /anime')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока глист')
    else:
        bot.send_message(message.chat.id, 'Пиши /help лошара')

bot.polling()