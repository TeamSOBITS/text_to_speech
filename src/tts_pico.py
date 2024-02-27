#!/usr/bin/env python3
# coding: utf-8
import rospy
import rospkg
import subprocess
import codecs
import os
import soundfile as sf
from text_to_speech.srv import TextToSpeechResponse, TextToSpeech
from std_msgs.msg import String, Bool

ROSPACK = rospkg.RosPack()
SAVE_PATH = ROSPACK.get_path("text_to_speech") + "/voice/speech_word.wav"

def text_to_speech(text):
    # decode
    speech_text = codecs.decode(str(text).encode('utf-8'))
    
    # Blank check
    if not speech_text or not speech_text.strip():
        rospy.logerr("Input text is empty or blank.")
        return False
    
    # Unicode error check
    try:
        rospy.loginfo("Input text [" + str(speech_text) + " ] ")
    except Exception as e:
        rospy.logerr(e)
        return False


    # remove old file
    if os.path.exists(SAVE_PATH):
        cmd = "rm %s" % SAVE_PATH
        subprocess.call(cmd, shell=True)
        # os.remove(SAVE_PATH)

    # create wav file
    cmd = "pico2wave -w %s '%s' " % (SAVE_PATH, speech_text)
    subprocess.call(cmd, shell=True)

    # get play time
    f = sf.SoundFile(SAVE_PATH)
    play_time = float(len(f)) / float(f.samplerate)
    print("Time[s]:", str(play_time))

    # play wav file and sleep
    cmd = "aplay %s" % SAVE_PATH
    subprocess.Popen(cmd, shell=True)
    rospy.sleep(play_time)

    return True

    
def tts_srv(srv_req):
    srv_result = text_to_speech(srv_req.text)
    return TextToSpeechResponse(srv_result)

def main():
    rospy.init_node("text_to_speech_node", anonymous=True)
    srv = rospy.Service("/speech_word", TextToSpeech, tts_srv)
    rospy.loginfo("Ready to 'text to speech'.")
    rospy.spin()

if __name__ == "__main__":
    main()