#! /bin/bash

echo "Install gTTS"
pip install gTTS==2.0.1
pip install gTTS-token --upgrade

echo "Install mpg321"
sudo apt install mpg321 -y

echo "Install voice data"
sudo apt install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001 -y

echo "Install wave"
pip install wave

echo "Install mutagen"
pip install mutagen

echo "Install pico2wave"
sudo apt install libttspico-utils

echo "Install alsa"
sudo apt install alsa alsa-utils

echo "Install soundfile"
sudo pip install soundfile
sudo apt install python-soundfile

echo "finish"
