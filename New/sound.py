from gtts import gTTS
from pygame import mixer
blabla = str("Hello Guyss")
tts = gTTS(text=blabla, lang='hi')
tts.save("say_hi.mp3")
mixer.init()
mixer.music.load("say_hi.mp3")
mixer.music.play()
