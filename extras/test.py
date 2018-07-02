from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

i=0
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/pi/Desktop/Central TJ1/haa/'):
    data = open('/home/pi/Desktop/Central TJ1/haa/'+files,'r').readlines()
    bot.train(data)

while True:
    message = input('you:')
    if message.strip() !='bye':
        reply = bot.get_response(message)
        print('ChatBot:',reply)


    elif message.strip() == 'bye':
        print('chatbot: bye')
        break
