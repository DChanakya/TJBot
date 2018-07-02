import socket
from pygame import mixer
#conv=open('chat.txt','r')

HOST = '192.168.0.29'
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

    if(("hi" or "Hi") in request):
        mixer.music.load("1.mp3")
        mixer.music.play()
    elif(("do you do") in request):
        mixer.music.load("serve.mp3")
        mixer.music.play()
    elif(("they") in request):
        mixer.music.load("they.mp3")
        mixer.music.play()
    elif(("say hi" or "say Hi") in request):
        mixer.music.load("Haai.mp3")
        mixer.music.play()
    elif(("bye") in request):
        mixer.music.load("bye.mp3")
        mixer.music.play()
    elif(("here") in request):
        mixer.music.load("yes.mp3")
        mixer.music.play()

    #tts = gTTS(text=blabla, lang='hi')
    #tts.save("sound.mp3")
    #mixer.music.load("sound.mp3")
    #mixer.music.play()
    #print('Bot: ',response)
s.close()
