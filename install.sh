#! /bin/bash


echo "╔══╣ Install: Text-to-Speech (STARTING) ╠══╗"


sudo apt-get update

echo "Install gTTS"
python3 -m pip install gTTS==2.0.1
python3 -m pip install gTTS-token --upgrade

echo "Install mpg321"
sudo apt-get install -y \
    mpg321

echo "Install voice data"
sudo apt install -y \
    open-jtalk \
    open-jtalk-mecab-naist-jdic \
    hts-voice-nitech-jp-atr503-m001

echo "Install wave"
python3 -m pip install \
    wave

echo "Install mutagen"
python3 -m pip install \
    mutagen

echo "Install pico2wave"
sudo apt-get install -y \
    libttspico-utils

echo "Install alsa"
sudo apt-get install -y \
    alsa \
    alsa-utils

echo "Install soundfile"
python3 -m pip install soundfile
sudo apt-get install -y \
    python-soundfile


# Install "sobits_msgs"
cd ~/catkin_ws/src/
git clone https://github.com/TeamSOBITS/sobits_msgs.git
cd ~/catkin_ws/src/speech_recognition_vosk/


echo "╚══╣ Install: Text-to-Speech (FINISHED) ╠══╝"