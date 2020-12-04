# text_to_speech
Text To Speech node.  

- english.launch
    - tts_google.py(修正中)
    - tts_pico.py
    - tts_microsoft.py(修正中)
- japanese.launch
    - tts_open_jtalk.py



## Install
#### Install this repository
```bash
$ cd ~/catkin_ws/src
$ git clone https://gitlab.com/TeamSOBITS/text_to_speech.git
$ cd ../ && catkin_make
```

#### Install depencies  
```bash
$ cd ~/catkin_ws/src/text_to_speech  
$ sh install.sh
```

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

#### Subscribed Topics
    /speech_word (std_msgs/String)

#### Service List
    /speech_word (text_to_speech/TextToSpeech)


## How to change the voice in _open jtalk_
＜open_jtalkの声質の変え方＞  
**text_to_speech/src/tts_open_jtalk.py**の１７行目で声質のデータを読み込んでいます（~.htsvoice)。  
その部分を別のhtsvoiceデータに書き換えてください。  
htsvoiceデータは、**text_to_speech/open_jtalk_voice_data**の中にあります。



## References

### Bing text to speech API

[1] https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput
