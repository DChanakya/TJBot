import socket
from pygame import mixer
import time
import re
import _thread
from gtts import gTTS
import datetime
import RPi.GPIO as GPIO
i=0;
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setwarnings(False)

pwm=GPIO.PWM(3,50)
GPIO.setwarnings(False)
now = datetime.datetime.now()
HOST = '192.168.43.39'
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
mahi=['mahi']
numb=['501']
room = ['room']
roomno1 = ['1']
roomno2 = ['2']
one = ['one']
two = ['two']

def lights1():
    return;
    
def hand1():
    pwm.start(5)
    time.sleep(1)
    time.sleep(2)
    pwm.ChangeDutyCycle(1)
    time.sleep(3)
    pwm.stop()
    GPIO.cleanup()
    return;
     
def lights():
    
    try:
       _thread.start_new_thread( lights1, () )
    except:
       print ("Error: unable to start thread")
       
def hand():
    global i
    i=i+1
    try:
       _thread.start_new_thread( hand1, () )
    except:
       print ("Error: unable to start thread")


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
    if(("hello" in request) and (("Mahi"in request) or ("Maahi" in request) or ("mahi" in request)or ("maahi" in request))):
        print("1")
        mixer.music.load("music/1.mp3")
        mixer.music.play()
        import h180
    elif(("turn"in request) and ("on" in request)):
            print("2")
        
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

    elif(("ok" in request)and ("bye" in request)):
            mixer.music.load("music/no.mp3")
            print("3")
        
            mixer.music.play()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn off the lights"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="stop LED"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn off the fans"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()

    
    
    elif(("hate" in request) or ("heat" in request)):
        mixer.music.load("music/hate.mp3")
        print("4")
        
        mixer.music.play()
    elif(("do you do") in request):
        print("5")
        
        mixer.music.load("music/serve.mp3")
        mixer.music.play()
    elif(("who"in request) and ("are"in request) and ("you" in request)):
        print("6")
        
        mixer.music.load("music/ban.mp3")
        
        mixer.music.play()
        time.sleep(2)
        import h90
    elif((("say "  in request)or( "se" in request)) and (("hello"  in request)or ("hi" in request))):
        print("7")
        mixer.music.load("music/3.mp3")
        mixer.music.play()
        import h181
    elif(("how" in request) and ("are" in request) and ("you" in request)):
        print("8")
        mixer.music.load("music/2.mp3")
       
        mixer.music.play()
    elif(("what"in request)and("can" in request)):
            print("9")
            mixer.music.load("music/yes.mp3")
            mixer.music.play()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn off the lights"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="stop LED"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
            sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sd1.connect(('10.1.1.113', 8888))
            output="turn off the fans"
            sd1.sendall(output.encode('utf-8'))
            sd1.close()
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
    elif("time" in request):
        timerq=str(now.strftime("%H %M"))
        print("10")
        new=timerq.split()
        print(new[0],new[1])
        if(int(new[0])<12):
                string=("The time is "+str(new[0])+ " " +str(new[1]) + ", In the Morning");
                tts = gTTS(text=string, lang='en')
                tts.save("music/time.mp3")
                mixer.init()
                print("Calculating")
                mixer.music.load("music/time.mp3")
                mixer.music.play()  
        elif(int(new[0])>12 and int(new[0])<4):
                string=("The time is "+str(int(new[0])-12)+ " " +str(new[1]) + ", In the Afternoon");
                tts = gTTS(text=string, lang='en')
                tts.save("music/time.mp3")
                mixer.init()
                print("Calculating")
                mixer.music.load("music/time.mp3")
                mixer.music.play()  
        elif(int(new[0])>4):
                string=("The time is "+str(int(new[0])-12)+ " " +str(new[1]) + ", In the Evening");
                tts = gTTS(text=string, lang='en')
                tts.save("music/time.mp3")
                mixer.init()
                print("Calculating")
                mixer.music.load("music/time.mp3")
                mixer.music.play()  


    elif("add" in request):
        try:
            stri=request.split()
            num1=int(stri[1])
            num2=int(stri[3])
            print("Calculating")
            if("add" in stri[0]):
                res=num1+num2
                print("Calculating")
                string=("The sum of " + str(num1) + "and" + str(num2) + "is" + str(res));
                tts = gTTS(text=string, lang='en')
                tts.save("music/cal.mp3")
                mixer.init()
                print("Calculating")
                mixer.music.load("music/cal.mp3")
                mixer.music.play()
        except:
                    string=("Invalid Inputs")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()

    elif((("subtract")) in request):
        try:
            stri=request.split()
            num1=int(stri[1])
            num2=int(stri[3])
            print("Calculating")
            if("subtract" in stri[0]):
                res=num1-num2
                string=("The subtraction of " + str(num1) + "and" + str(num2) + "is" + str(res));
                tts = gTTS(text=string, lang='en')
                tts.save("music/cal.mp3")
                print("Calculating")
                mixer.music.load("music/cal.mp3")
                mixer.music.play()
            
        except:
                    string=("Invalid Inputs")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()
    elif((("multiply")) in request):
        try:
            stri=request.split()
            num1=int(stri[1])
            num2=int(stri[3])
            print("Calculating")
            
            if("multiply" in stri[0]):
                res=num1*num2
                string=("The multiplication of " + str(num1) + "and" + str(num2) + "is" + str(res));
                tts = gTTS(text=string, lang='en')
                tts.save("music/cal.mp3")
                print("Calculating")
                mixer.music.load("music/cal.mp3")
                mixer.music.play()
        except:
                    string=("Invalid Inputs")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()
    elif(("Mahi"in request) or ("Maahi"in request) or ("mahi"in request) or ("maahi"in request)):
        sd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("11")
        sd1.connect(('10.1.1.113', 8888))
        st=str(buf).split(" ",1)          
        r1=re.findall(r"\b" + search + r"\b", st[1])
        r2=re.findall(r"\b" + search1 + r"\b", st[1])
        r3 = re.findall(r"\b" + search2 + r"\b", st[1])
        r4 = re.findall(r"\b" + search3 + r"\b", st[1])
        r5 = re.findall(r"\b" + search4 + r"\b", st[1])
        r6 = re.findall(r"\b" + search5 + r"\b", st[1])
        r7 = re.findall(r"\b" + search6 + r"\b", st[1])
        r8 = re.findall(r"\b" +search7 + r"\b", st[1])
        r9 = re.findall(r"\b" +search8 + r"\b", st[1])
        r10 = re.findall(r"\b" +search9 + r"\b", st[1])
        r11 = re.findall(r"\b" +search10 + r"\b", st[1])
        r12 = re.findall(r"\b" +search11 + r"\b", st[1])
        r13 = re.findall(r"\b" +search12 + r"\b", st[1])
        r14 = re.findall(r"\b" +search13 + r"\b", st[1])
        r15 = re.findall(r"\b" +search14 + r"\b", st[1])
        r16 = re.findall(r"\b" +search15 + r"\b", st[1])
        
    

        if (r1 == li and r2 == on and r6==room and ((r7==roomno1 or r14 == one) and (r8==roomno2 or r15 == two))):
            mixer.music.load("music/lonall.mp3")
            mixer.music.play()

        elif (r1 == li and r2 == on and r6==room and (r8==roomno2 or r16 == two)):
            mixer.music.load("music/lon2.mp3")
            mixer.music.play()

        elif (r1==li and r3==off and r6==room and (r7==roomno1 or r15 == one)):
            mixer.music.load("music/loff1.mp3")
            mixer.music.play()

            
        elif (r1 == li and r3 == off and r6==room and (r8==roomno2 or r16 == two)):
            mixer.music.load("music/loff2.mp3")
            mixer.music.play()


        elif (r4 == fan and r2 == on and r6==room and (r7==roomno1 or r15 == one)):
            mixer.music.load("music/fon1.mp3")
            mixer.music.play()


        elif (r4 == fan and r2 == on and r6==room and (r8==roomno2 or r16 == two)):
            mixer.music.load("music/fon2.mp3")
            mixer.music.play()


        elif (r4 == fan and r3 == off and r6==room and (r7==roomno1 or r15 == one)):
            mixer.music.load("music/foff1.mp3")
            mixer.music.play()

        elif (r4 == fan and r3 == off and r6==room and (r8==roomno2 or r16 == two)):
            mixer.music.load("music/foff2.mp3")
            mixer.music.play()


        elif (r1==li and r2==on and r6==room and (r7==roomno1 or r15 == one)):
            mixer.music.load("music/lon1.mp3")
            mixer.music.play()
        elif (r1 == li and r2 == on):
             mixer.music.load("music/lonall.mp3")
             mixer.music.play()
        elif (r1 == li and r3==off):
             mixer.music.load("music/loffall.mp3")
             mixer.music.play()   
        elif (r4 == fan and r2 == on):
              mixer.music.load("music/fonall.mp3")
              mixer.music.play()
        elif (r4 == fan and r3==off):
              mixer.music.load("music/foffall.mp3")
              mixer.music.play()    
        if(len(st)>1):
            output = st[1]
            sd1.sendall(output.encode('utf-8'))
        sd1.close()
        
    
    elif((("division")) in request):
        try:
            stri=request.split()
            num1=int(stri[1])
            num2=int(stri[3])
            print("Calculating")
            if("divide" in stri[0]):
                if(num1==0):
                    string=("Invalid Inputs")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()
                else:
                    res=num1+num2
                    string=("The division of " + str(num1) + "and" + str(num2) + "is" + str(res));
                    
                    print("Calculating")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()
        except:
                    string=("Invalid Inputs")
                    tts = gTTS(text=string, lang='en')
                    tts.save("music/cal.mp3")
                    mixer.music.load("music/cal.mp3")
                    mixer.music.play()
             
        
s.close()
