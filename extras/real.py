from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from gtts import gTTS
from pygame import mixer
import socket
from pygame import mixer
import time
import re
import _thread
from gtts import gTTS
import datetime
#import RPi.GPIO as GPIO
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3,GPIO.OUT)
# pwm=GPIO.PWM(3,50)

reply1=('hii dude')
reply2=('hellooo')
reply3=('i am maahi the chatbot')
reply4=('i am can control everything in the special team')
reply5=('I entertain and interact with the special team')
reply6=('noo I want to interact with these guys')
reply7=('sorry!!!!')
reply8=('i live in the special teams coolest place')
reply9=('i too love you but as a bot')

now = datetime.datetime.now()
HOST = '10.1.1.115'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
    exit()
print('Socket Bind Success!')

s.listen(10)
print('Socket is now listening')

mixer.init()
search = "lights"
search1 = "on"
search2 = "off"
search3 = "fans"
search4 = "projector"
search5 = "room"
search6 = "1"
search7 = "2"
search8 = "open"
search9 = "unlock"
search10 = "door"
search11 = "mahi"
search12 = "501"
search13 = "doors"
search14 = "one"
search15 = "two"

li = ['lights']
on = ['on']
off = ['off']
fan = ['fans']
door = ['door']
doors = ['doors']
opn = ['open']
ul = ['unlock']
pro = ['projector']
mahi = ['mahi']
numb = ['501']
room = ['room']
roomno1 = ['1']
roomno2 = ['2']
one = ['one']
two = ['two']


def lights1():
    return;


def hand1():
    return;


def lights():
    try:
        _thread.start_new_thread(lights, ())
    except:
        print("Error: unable to start thread")


def hand():
    try:
        _thread.start_new_thread(hand, ())
    except:
        print("Error: unable to start thread")

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/pi/Desktop/Central TJ1/haa/'):
          data = open('/home/pi/Desktop/Central TJ1/haa/' + files, 'r').readlines()
          bot.train(data)


while True:
    conn, addr = s.accept()
    print('Connect with ' + addr[0] + ':' + str(addr[1]))
    print(str(conn) +":"+ str(addr))
    buf = conn.recv(64)
    print(buf)

    request = str(buf)
    if request.strip() != 'bye':
        reply = bot.get_response(request)
        print('ChatBot:', reply)

        string = ("Invalid Inputs")
        tts = gTTS(text=string, lang='en')
        tts.save("music/cal.mp3")
        mixer.music.load("music/cal.mp3")

        if (reply == reply1):
            mixer.music.load("hid.mp3")
            mixer.music.play()

        elif ("turn" and "on" in request):
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "turn on the lights"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "blink LED"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "turn on the fans"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()

        elif (reply == reply2):
            mixer.music.load("helo.mp3")
            mixer.music.play()

        elif(reply == reply3):
            mixer.music.load("iam.mp3")
            mixer.music.play()

        elif (reply == reply4):
            mixer.music.load("ican.mp3")
            mixer.music.play()

        elif (reply == reply5):
            mixer.music.load("ienter.mp3")
            mixer.music.play()


        elif (reply == reply6):
            mixer.music.load("music/no.mp3")

            mixer.music.play()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "turn off the lights"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "stop LED"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output = "turn off the fans"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()

        elif (reply == reply7):
            mixer.music.load("sorry.mp3")
            mixer.music.play()

        elif (reply == reply8):
            mixer.music.load("live.mp3")
            mixer.music.play()

        elif (reply == reply9):
            mixer.music.load("love.mp3s")
            mixer.music.play()

        elif (reply != 0):
                read=str(reply)
                string = (read)
                tts = gTTS(text=string, lang='en')
                tts.save("cal.mp3")
                mixer.music.load("cal.mp3")
                mixer.music.play()
        
        elif (("Mahi" or "Maahi" or "mahi" or "maahi") in request):
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            st = str(buf).split(" ", 1)
            if ("love" in st[1]):
                mixer.music.load("music/love.mp3")
                mixer.music.play()
            r1 = re.findall(r"\b" + search + r"\b", st[1])
            r2 = re.findall(r"\b" + search1 + r"\b", st[1])
            r3 = re.findall(r"\b" + search2 + r"\b", st[1])
            r4 = re.findall(r"\b" + search3 + r"\b", st[1])
            r5 = re.findall(r"\b" + search4 + r"\b", st[1])
            r6 = re.findall(r"\b" + search5 + r"\b", st[1])
            r7 = re.findall(r"\b" + search6 + r"\b", st[1])
            r8 = re.findall(r"\b" + search7 + r"\b", st[1])
            r9 = re.findall(r"\b" + search8 + r"\b", st[1])
            r10 = re.findall(r"\b" + search9 + r"\b", st[1])
            r11 = re.findall(r"\b" + search10 + r"\b", st[1])
            r12 = re.findall(r"\b" + search11 + r"\b", st[1])
            r13 = re.findall(r"\b" + search12 + r"\b", st[1])
            r14 = re.findall(r"\b" + search13 + r"\b", st[1])
            r15 = re.findall(r"\b" + search14 + r"\b", st[1])
            r16 = re.findall(r"\b" + search15 + r"\b", st[1])

            if (r1 == li and r2 == on and r6 == room and (
                    (r7 == roomno1 or r14 == one) and (r8 == roomno2 or r15 == two))):
                mixer.music.load("music/lonall.mp3")
                mixer.music.play()

            elif (r1 == li and r2 == on and r6 == room and (r8 == roomno2 or r16 == two)):
                mixer.music.load("music/lon2.mp3")
                mixer.music.play()

            elif (r1 == li and r3 == off and r6 == room and (r7 == roomno1 or r15 == one)):
                mixer.music.load("music/loff1.mp3")
                mixer.music.play()


            elif (r1 == li and r3 == off and r6 == room and (r8 == roomno2 or r16 == two)):
                mixer.music.load("music/loff2.mp3")
                mixer.music.play()


            elif (r4 == fan and r2 == on and r6 == room and (r7 == roomno1 or r15 == one)):
                mixer.music.load("music/fon1.mp3")
                mixer.music.play()


            elif (r4 == fan and r2 == on and r6 == room and (r8 == roomno2 or r16 == two)):
                mixer.music.load("music/fon2.mp3")
                mixer.music.play()


            elif (r4 == fan and r3 == off and r6 == room and (r7 == roomno1 or r15 == one)):
                mixer.music.load("music/foff1.mp3")
                mixer.music.play()

            elif (r4 == fan and r3 == off and r6 == room and (r8 == roomno2 or r16 == two)):
                mixer.music.load("music/foff2.mp3")
                mixer.music.play()


            elif (r1 == li and r2 == on and r6 == room and (r7 == roomno1 or r15 == one)):
                mixer.music.load("music/lon1.mp3")
                mixer.music.play()
            elif (r1 == li and r2 == on):
                mixer.music.load("music/lonall.mp3")
                mixer.music.play()
            elif (r1 == li and r3 == off):
                mixer.music.load("music/loffall.mp3")
                mixer.music.play()
            elif (r4 == fan and r2 == on):
                mixer.music.load("music/fonall.mp3")
                mixer.music.play()
            elif (r4 == fan and r3 == off):
                mixer.music.load("music/foffall.mp3")
                mixer.music.play()
            if (len(st) > 1):
                output = st[1]
                sd1.sendall(output.encode('utf-8'))
            sd1.close()


        
