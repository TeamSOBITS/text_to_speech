#!/usr/bin/env python
# coding: utf-8
import codecs
import subprocess
from gtts import gTTS

speech_text = codecs.decode("hello world.","utf-8")

tts = gTTS(text=speech_text,lang='en',slow=False)
tts.save('hello.mp3')

subprocess.call("mpg321 /home/sobit-x1/hello.mp3", shell=True)


print "save ok"
