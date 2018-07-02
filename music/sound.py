from gtts import gTTS
from pygame import mixer
blabla = str("I am awesome., what about you")
tts = gTTS(text=blabla, lang='hi')
tts.save("new/how1.mp3")
mixer.init()
mixer.music.load("new/how1.mp3")
mixer.music.play()
