import random
import time
import telepot

from chatbot import sendAI

TELEGRAM_API_KEY = "**************************"

bot = telepot.Bot(TELEGRAM_API_KEY)


#chat entre terminal e bot
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg['text'])

    if content_type == 'text':
        time.sleep(random.randint(1, 5))
        bot.sendMessage(chat_id, sendAI(msg['text']))

bot.message_loop(handle)

print('Ouvindo ...')


while 1:
    time.sleep(10)

