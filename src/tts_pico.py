#!/usr/bin/env python3
# coding: utf-8
import rospy
import rospkg
import subprocess
import codecs
import os
import soundfile as sf
from text_to_speech.srv import *
from std_msgs.msg import String, Bool

ROSPACK = rospkg.RosPack()
SAVE_PATH = ROSPACK.get_path("text_to_speech") + "/voice/speech_word.wav"

def text_to_speech(text):
    #decode
    speech_text = codecs.decode(str(text).encode('utf-8'))
    
    #Blank check
    if speech_text and speech_text.strip():
        pass
    
    else:
        rospy.logerr("Input text is empty or blank.")
        return False

    
    #Unicode error check
    try:
        rospy.loginfo("Input text [" + str(speech_text) + " ] ")
    
    except Exception as e:
        rospy.logerr(e)
        return False


    #remove old file
    if os.path.exists(SAVE_PATH) == True:
        cmd = "rm %s" % SAVE_PATH
        subprocess.call(cmd, shell=True)


    #create wav file
    cmd = "pico2wave -w %s '%s' " % (SAVE_PATH, speech_text)
    subprocess.call(cmd, shell=True)


    #get play time
    f = sf.SoundFile(SAVE_PATH)
    play_time = float(len(f)) / float(f.samplerate)
   

    #play wav file and sleep
    cmd = "aplay %s" % SAVE_PATH
    sobit_mini_head_status_publisher.publish("speaking")
    subprocess.Popen(cmd, shell=True)
    rospy.sleep(play_time)

    
    sobit_mini_head_status_publisher.publish("normal")

    return True

    
def tts_srv(srv_req):
    srv_result = text_to_speech(srv_req.text)
    if srv_result == True:
        return TextToSpeechResponse(True)
    else:
        return TextToSpeechResponse(False)

def tts_msg(msg_req):
    pub = rospy.Publisher("speech_word_msg_result", Bool, queue_size = 1)
    msg_result = text_to_speech(msg_req.data)
    if msg_result == True:
        pub.publish(True)
    else:
        pub.publish(False)

if __name__ == "__main__":
    rospy.init_node("text_to_speech_node")
    srv = rospy.Service("/speech_word", TextToSpeech, tts_srv)
    sub = rospy.Subscriber("/speech_word", String, tts_msg)
    sobit_mini_head_status_publisher = rospy.Publisher("/sobit_mini_head/status", String, queue_size=10)
    rospy.loginfo("Ready to 'text to speech'.")
    rospy.spin()

    #text_to_speech("My name is SOBIT.")