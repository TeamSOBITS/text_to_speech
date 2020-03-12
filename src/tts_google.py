#!/usr/bin/env python
# coding: utf-8
import rospy
import rospkg
import codecs
import subprocess
from gtts import gTTS
from text_to_speech.srv import *
from std_msgs.msg import String, Bool
from mutagen.mp3 import MP3

sobit_mini_head_status_publisher = rospy.Publisher("/sobit_mini_head/status", String, queue_size=10)

def text_to_speech(text):
    rospy.loginfo("Served text '''" + str(text) + "'''.")

    """ decode """
    speech_text = codecs.decode(str(text),"utf-8")

    """ Blank Error process """
    if speech_text and speech_text.strip():pass
    else:
        rospy.logerr("Text is empty or blank.")
        return False

    """ Unicode Error process"""
    try:rospy.loginfo("speech_text="+str(speech_text))
    except Exception as e:
        rospy.logerr(e)
        return False

    """ text to speech """
    tts = gTTS(text=speech_text,lang='en',slow=False)

    """ save """
    rospack = rospkg.RosPack()
    save_path = rospack.get_path('text_to_speech') + "/voice/speech_word.mp3"
    tts.save(save_path)
    #rospy.loginfo("save_path=" + str(save_path))

    """ play back """
    play_cmd = "mpg321 " + str(save_path)
    #rospy.loginfo("play_cmd=" + play_cmd)
    sobit_mini_head_status_publisher.publish("speaking")
    subprocess.Popen(play_cmd, shell=True)

    """ get play_time """
    mp3 = MP3(save_path)
    play_time = mp3.info.length #音声ファイルの再生時間を取得
    #rospy.loginfo("play_time:[%s]"%str(play_time))
    rospy.sleep(play_time) #再生時間分だけsleep
    sobit_mini_head_status_publisher.publish("normal")

    return True

def tts_srv(srv_req):
    srv_result = text_to_speech(srv_req.text)
    if srv_result == True:
        return TextToSpeechResponse(True)
    else:
        return TextToSpeechResponse(False)

def tts_msg(msg_req):
    pub = rospy.Publisher('speech_word_msg_result', Bool, queue_size = 1)
    msg_result = text_to_speech(msg_req.data)
    if msg_result == True:
        pub.publish(True)
    else:
        pub.publish(False)

if __name__ == "__main__":
    rospy.init_node('text_to_speech_node')
    srv = rospy.Service('/speech_word', TextToSpeech, tts_srv)
    sub = rospy.Subscriber('/speech_word', String, tts_msg)
    rospy.loginfo("Ready to 'text to speech'.")
    rospy.spin()
