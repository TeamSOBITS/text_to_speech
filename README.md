# text_to_speech
Text To Speech node.  
open_jtalkのサービス化は少々お待ちください

## Install

```bash
$ pip install gTTS==1.2.1
$ sudo apt-get install mpg321
```
- For open_jtalk  
```bash  
$ sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
```

## How to Use
```bash
$ roslaunch text_to_speech tts_google.launch      <- google
$ roslaunch text_to_speech tts_microsoft.launch   <- microsoft
$ roslaunch text_to_speech tts_open_jtalk.launch  <- open_jtalk
```
- How to change the voice in _open jtalk_
  - Open **text_to_speech/src/tts_open_jtalk.py**
  - Re-write **line 31**
  - You can find _.htsvoice_ in **text_to_speech/open_jtalk_voice_data/**

## References

### Bing text to speech API

[1] https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput
