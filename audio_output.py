from gtts import gTTS
import subprocess
import os
import time

def speak(s):
	tts = gTTS(text=s, lang='en', slow=False)
	tts.save("/tmp/output.mp3")
	play_mp3("/tmp/output.mp3")

def play_mp3(path):
	subprocess.call(["ffplay", "-loglevel", "panic", "-nostats", "-hide_banner", "-nodisp", "-autoexit", path])
