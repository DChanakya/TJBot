import socket
from pygame import mixer
import time
import re
from gtts import gTTS
HOST = '192.168.0.5'
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

def play(file):
    mixer.init();
    mixer.music.load("music/"+ file +".mp3")
    mixer.music.play()
    return;

def voice(string):
    tts = gTTS(text=string, lang='en')
    tts.save("music/cal.mp3")    
    play("cal");
    return;

def 
