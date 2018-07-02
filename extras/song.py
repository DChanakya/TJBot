import socket
from pygame import mixer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
pwm=GPIO.PWM(8,50)



#conv=open('chat.txt','r')

HOST = '10.1.1.115'
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

    if(("hey" or "Hey") in request):
        mixer.music.load("master.mp3")
       
        mixer.music.play()
    elif(("do you do") in request):
        mixer.music.load("serve.mp3")
        mixer.music.play()
    elif(("they") in request):
        mixer.music.load("they.mp3")
       
        mixer.music.play()
    elif(("say " or "se") in request):
        mixer.music.load("Haai.mp3")
       
        mixer.music.play()
    elif(("turn"and"off") in request):
        mixer.music.load("bye.mp3")
        
        mixer.music.play()
    elif((("why")or("we")) in request):
        mixer.music.load("yes.mp3")
        mixer.music.play()
    



    #tts = gTTS(text=blabla, lang='hi')
    #tts.save("sound.mp3")
    #mixer.music.load("sound.mp3")
    #mixer.music.play()
    #print('Bot: ',response)
s.close()
