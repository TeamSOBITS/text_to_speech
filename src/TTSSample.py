#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import http.client, urllib.parse, json
from xml.etree import ElementTree
import wave
import time

# Note: new unified SpeechService API key and issue token uri is per region
# New unified SpeechService key
# Free: https://azure.microsoft.com/en-us/try/cognitive-services/?api=speech-services
apiKey = "fb20da753e454f3f9820b7b09b4e007c"

params = ""
headers = {"Ocp-Apim-Subscription-Key": apiKey}

#AccessTokenUri = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken";
AccessTokenHost = "westus.api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"

# Connect to server to get the Access Token
conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, params, headers)
#response = conn.getresponse()
data = conn.getresponse().read()
conn.close()

accesstoken = data.decode("UTF-8")
headers = {"Content-type": "application/ssml+xml",
			"X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
			"Authorization": "Bearer " + accesstoken,
			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
			"User-Agent": "chrome"}


body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)')

"""
body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'ja-JP')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'ja-JP')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (ja-JP, Ayumi, Apollo)')
"""

voice.text = 'demo to call microsoft text to speech service in Python.'
#voice.text = 'こんにちは、私の名前はソビットです。'

#Connect to server to synthesize the wave
print ("\nConnect to server to synthesize the wave")
conn = http.client.HTTPSConnection("westus.tts.speech.microsoft.com")
conn.request("POST", "/cognitiveservices/v1", ElementTree.tostring(body), headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
conn.close()

w = wave.Wave_write("output.wav")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(22000) #22K[Hz]
w.writeframes(data)
w.close()

print( type(data))
print("The synthesized wave length: %d" %(len(data)))
