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
reply4=('i can control everything in the special team')
reply5=('I entertain and interact with the special team')
reply6=('noo I want to interact with these guys')
reply7=('sorry!!!!')
reply8=('i live in the special teams coolest place')
reply9=('i too love you but as a bot')
reply10=('i love only mahesh sir and my special team')
reply11=('yeah, i like you alot guys learn well and enter the special team, i will be waiting for you all')
reply12=('a very good morning dude')
reply13=('i am awesome, what about you')
reply14=('welocome to the special team and please dont touch anything')

now = datetime.datetime.now()
HOST = '192.168.0.3'
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




while True:
    conn, addr = s.accept()
    print(addr)
    print('Connect with ' + addr[0] + ':' + str(addr[1]))
    buf = conn.recv(64)
    print(buf)

    bot = ChatBot('Bot')
    bot.set_trainer(ListTrainer)

    for files in os.listdir('/home/pi/Desktop/Central TJ1/haa/'):
           data = open('/home/pi/Desktop/Central TJ1/haa/' + files, 'r').readlines()
           bot.train(data)
    

    request = str(buf)
    if request.strip() != 'bye':
        reply = bot.get_response(request)
        print('ChatBot:', reply)

        if (reply == reply1):
            mixer.init()
            mixer.music.load("hid.mp3")
            mixer.music.play()
            import h180

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
            mixer.init()
            mixer.music.load("hello.mp3")
            mixer.music.play()

        elif(reply == reply3):
            mixer.init()
            mixer.music.load("ban.mp3")
            mixer.music.play()
            time.sleep(2)
            import h90

        elif (reply == reply4):
            mixer.init()
            mixer.music.load("ican.mp3")
            mixer.music.play()

        elif (reply == reply5):
            mixer.init()
            mixer.music.load("ido.mp3")
            mixer.music.play()

        elif (reply == reply14):
            mixer.init()
            mixer.music.load("freshers.mp3")
            mixer.music.play()
            import h181

        elif (reply == reply6):
            mixer.init()
            mixer.music.load("no.mp3")
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
            mixer.init()
            mixer.music.load("sorry.mp3")
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn on the lights"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="blink LED"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn on the fans"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()


        elif (reply == reply8):
            mixer.init()
            mixer.music.load("live.mp3")
            mixer.music.play()

        elif (reply == reply9):
            mixer.init()
            mixer.music.load("love.mp3")
            mixer.music.play()

        elif (reply == reply10):
            mixer.init()
            mixer.music.load("love1.mp3")
            mixer.music.play()

        elif (reply == reply11):
            mixer.init()
            mixer.music.load("msg.mp3")
            mixer.music.play()

        elif (reply == reply12):
            mixer.init()
            mixer.music.load("greet.mp3")
            mixer.music.play()
            
        elif (reply == reply13):
            mixer.init()
            mixer.music.load("how.mp3")
            mixer.music.play()


        # elif ((("Add")) in request):
        #     try:
        #         stri = request.split()
        #         num1 = int(stri[1])
        #         num2 = int(stri[3])
        #         print("Calculating")
        #         if ("Add" in stri[0]):
        #             res = num1 + num2
        #             print("Calculating")
        #             string = ("The sum of " + str(num1) + "and" + str(num2) + "is" + str(res));
        #             tts = gTTS(text=string, lang='en')
        #             tts.save("cal.mp3")
        #             mixer.init()
        #             print("Calculating")
        #             mixer.music.load("cal.mp3")
        #             mixer.music.play()
        #     except:
        #         string = ("Invalid Inputs")
        #         tts = gTTS(text=string, lang='en')
        #         tts.save("music/cal.mp3")
        #         mixer.music.load("music/cal.mp3")
        #         mixer.music.play()
        #
        # elif ((("subtract")) in request):
        #     try:
        #         stri = request.split()
        #         num1 = int(stri[1])
        #         num2 = int(stri[3])
        #         print("Calculating")
        #         if ("subtract" in stri[0]):
        #             res = num1 - num2
        #             string = ("The subtraction of " + str(num1) + "and" + str(num2) + "is" + str(res));
        #             tts = gTTS(text=string, lang='en')
        #             tts.save("cal.mp3")
        #             print("Calculating")
        #             mixer.music.load("cal.mp3")
        #             mixer.music.play()
        #
        #     except:
        #         string = ("Invalid Inputs")
        #         tts = gTTS(text=string, lang='en')
        #         tts.save("music/cal.mp3")
        #         mixer.music.load("music/cal.mp3")
        #         mixer.music.play()
        # elif ((("multiply")) in request):
        #     try:
        #         stri = request.split()
        #         num1 = int(stri[1])
        #         num2 = int(stri[3])
        #         print("Calculating")
        #
        #         if ("multiply" in stri[0]):
        #             res = num1 * num2
        #             string = ("The multiplication of " + str(num1) + "and" + str(num2) + "is" + str(res));
        #             tts = gTTS(text=string, lang='en')
        #             tts.save("cal.mp3")
        #             print("Calculating")
        #             mixer.music.load("cal.mp3")
        #             mixer.music.play()
        #     except:
        #         string = ("Invalid Inputs")
        #         tts = gTTS(text=string, lang='en')
        #         tts.save("cal.mp3")
        #         mixer.music.load("cal.mp3")
        #         mixer.music.play()
        #
        # elif ((("divide")) in request):
        #     try:
        #         stri = request.split()
        #         num1 = int(stri[1])
        #         num2 = int(stri[3])
        #         print("Calculating")
        #
        #         if ("divide" in stri[0]):
        #             if (num1 == 0):
        #                 string = ("Invalid Inputs")
        #                 tts = gTTS(text=string, lang='en')
        #                 tts.save("cal.mp3")
        #                 mixer.music.load("cal.mp3")
        #                 mixer.music.play()
        #             else:
        #                 res = num1 + num2
        #                 string = ("The division of " + str(num1) + "and" + str(num2) + "is" + str(res));
        #
        #                 print("Calculating")
        #                 tts = gTTS(text=string, lang='en')
        #                 tts.save("cal.mp3")
        #                 mixer.music.load("cal.mp3")
        #                 mixer.music.play()
        #     except:
        #         string = ("Invalid Inputs")
        #         tts = gTTS(text=string, lang='en')
        #         tts.save("music/cal.mp3")
        #         mixer.music.load("music/cal.mp3")
        #         mixer.music.play()

        elif (("Mahi" or "Maahi" or "mahi" or "maahi") in request):
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            st = str(buf).split(" ", 1)
            # if ("love" in str[request]):
            #     mixer.music.load("love.mp3")
            #     mixer.music.play()
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

            if (r1 == li and r2 == on and r6 == room and ((r7 == roomno1 or r14 == one) and (r8 == roomno2 or r15 == two))):
                mixer.music.load("music/lonall.mp3")
                mixer.music.play()

            elif (r1 == li and r2 == on and r6 == room and (r8 == roomno2 or r16 == two)):
                mixer.music.load("music/lon2.mp3")
                mixer.music.play()

            elif (r1 == li and r3 == off and r6 == room and (r7 == roomno1 or r15 == one)):
                print('lightsoffroom1')
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




s.close()

# # reply1=("ok")
# # # detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
# # # cap = cv2.VideoCapture(0);
# # blabla = (reply1)
# # tts = gTTS(text=blabla, lang='hi')
# # tts.save("id.mp3")
# # mixer.init()
# # mixer.music.load("id.mp3")
# # mixer.music.play()
# i=0
# bot = ChatBot('Bot')
# bot.set_trainer(ListTrainer)
#
# for files in os.listdir('I:/chat/'):
#     data = open('I:/chat/'+files,'r').readlines()
#     bot.train(data)
#
# # for files in os.listdir('C:/Users/HP/Desktop/TREAT/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
# #     data = open('C:/Users/HP/Desktop/TREAT/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
# #     bot.train(data)
#
# while True:
#     message = input('You:')
#     if message.strip() != 'bye':
#         reply = bot.get_response(message)
#         print('Chatbot :',reply)
#         reply1=str(reply)
#         blabla = (reply1)
#         print(blabla)
#         tts = gTTS(text=blabla, lang='hi')
#         tts.save("id"+str(i)+".mp3")
#         mixer.init()
#         mixer.music.load("id"+str(i)+".mp3")
#         mixer.music.play()
#         i = i+1
#
#     if message.strip() == 'bye':
#         print('ChatBot : Bye')
#         break
