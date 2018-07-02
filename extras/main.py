from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from gtts import gTTS
import socket
from pygame import mixer
#conv=open('chat.txt','r')

HOST = '192.168.0.25'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
    sys.exit()
print('Socket Bind Success!')

s.listen(10)
print('Socket is now listening')

mixer.init()

bot=ChatBot('Tj')
bot.set_trainer(ListTrainer)
#bot.train(conv)
conversations = [

        'Hi', ' Hi mastaruu',
        'what do you do', ' I serve the Special team ',
         'yes then say Hi to them ', ' Haai',
         "they can't hear", ' Haaaai guyyssss',
        "Have you heard the news", "Yes, It's the inaugaration ceremony of the first year students",
        'ok bye ',' Welcome to UshaRama Everyone,  T J Signing Off',
        "Good morning", "Good Morning Master",
          "how are you","I am doing well, how about you?",
          "I'm also good.","That's good to hear.",
          "What is your favorite book", "I can't read.",
            "So what's your favorite color","Blue"
  
]
bot.train(conversations)
while True:
    conn, addr = s.accept()
    print('Connect with ' + addr[0] + ':' + str(addr[1]))
    buf = conn.recv(64)
    print(buf)
    spl=str(buf).split("'")
    if "'" in str(buf):
        request = str(spl[1])
    else:
        request=str(buf)
    if 'stop' in request:
        conn.close()
        break;
   # request = input('You: ')
    response = bot.get_response(request)
    blabla = str(response)
    print(blabla)
    tts = gTTS(text=blabla, lang='hi')
    tts.save("sound.mp3")
    mixer.music.load("sound.mp3")
    mixer.music.play()
    #print('Bot: ',response)
s.close()
