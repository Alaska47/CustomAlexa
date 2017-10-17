from audio_input import *
from audio_output import *
import time
from alexa_client import AlexaClient
import os

alexa = AlexaClient()
speak("Hi, what can I do for you today?")
while True:
	print("Waiting for voice")
	record_to_file('/tmp/output.wav')
	print("Sending")
	alexa.ask("/tmp/output.wav", save_to="/tmp/output_final.mp3")
	print("Received")
	play_mp3("/tmp/output_final.mp3")
