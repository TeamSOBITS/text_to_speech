# text_to_speech
Text To Speech node.  
Microsoftはまだ動かないです.  
英語はtts_google.launch、日本語はtts_open_jtalk.launchを使用してください。  
 


## Install
#### Install this repository
```bash
$ cd ~/catkin_ws/src
$ git clone https://gitlab.com/TeamSOBITS/text_to_speech.gitlab
$ cd ../ && catkin_make
```
#### Install gTTS
```bash
$ pip install gTTS==1.2.1 #これだと動かないかも
$ pip install gTTS==2.0.1
$ pip install gTTS-token --upgrade
$ sudo apt-get install mpg321
```
#### Install wave & voice data
```bash  
$ sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
$ sudo pip install wave  
```

#### Install mutagen
```bash
$ sudo pip install mutagen
```
<br/>
<br/>
## How to Use

#### Launch Node
- google
```bash
$ roslaunch text_to_speech tts_google.launch
```

- microsoft
```bash
$ roslaunch text_to_speech tts_microsoft.launch
```

- open_jtalk
```bash
$ roslaunch text_to_speech tts_open_jtalk.launch
```
<br/>
#### Subscribed Topics
    /speech_word (std_msgs/String)
<br/>
#### Service List
    /speech_word (text_to_speech/TextToSpeech)
<br/>
<br/>
## How to change the voice in _open jtalk_
  - Open **text_to_speech/src/tts_open_jtalk.py**
  - Re-write **line 31**
  - You can find _.htsvoice_ in **text_to_speech/open_jtalk_voice_data/**

<br/>
<br/>
## References

### Bing text to speech API

[1] https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput
