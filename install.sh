#! /bin/bash

echo "Install gTTS"
pip install gTTS==2.0.1
pip install gTTS-token --upgrade

echo "Install mpg321"
sudo apt install mpg321
  
echo "Install voice data"
sudo apt install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

echo "Install wave"
pip install wave  

echo "Install mutagen"
pip install mutagen


echo "finish"
