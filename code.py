import sys
import time
import random
import datetime
import telepot

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
        print 'Got command: %s' % command

        if command == '/start':
         bot.sendMessage(chat_id,"Hi! :) Send me the URL that you want to transform in a QRCode.")
        else:
         bot.sendMessage(chat_id,"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="+command)

bot = telepot.Bot('MYPRIVATEKEY')
bot.message_loop(handle)
print 'In ascolto...'

while 1:
        time.sleep(10)
