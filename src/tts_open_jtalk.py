#!/usr/bin/env python3
#coding: utf-8
import subprocess
import rospy
import wave
from text_to_speech.srv import TextToSpeechResponse, TextToSpeech
from std_msgs.msg import Bool, String

def open_jtalk(speech_word):
    rospy.loginfo("speech_word:[%s]"%speech_word)
    
    # Storing commands in variables and executing them collectively at the end.
    open_jtalk = ['open_jtalk'] 

    mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic'] # dictionary

    # voice_data
    htsvoice = ['-m', rospy.get_param("voice_data")] 
    #htsvoice = ['-m', '/path/to/hoge.htsvoice']


    # option setting（http://moblog.absgexp.net/openjtalk/)
    all_pass = ['-a', '0.5']
    post_filter = ['-b', '0.3']
    speed = ['-r', '1.0']

    out_wav = ['-ow', './open_jtalk.wav'] # wav file place setting
    out_log = ['-ot', './open_jtalk.log'] # log file place setting

    # including variable name
    cmd = open_jtalk+mech+htsvoice+speed+out_wav+out_log+all_pass+post_filter

    # execute in subprocess
    with subprocess.Popen(cmd, stdin=subprocess.PIPE) as execute:
        execute.stdin.write(speech_word.encode('utf-8'))
        execute.stdin.close()
        execute.wait()

    #replay [] not change
    playback_cmd = ['aplay', '-q', './open_jtalk.wav']
    subprocess.Popen(playback_cmd)

    # get play time
    wf = wave.open("./open_jtalk.wav" , "r" )
    play_time =  float(wf.getnframes()) / wf.getframerate()
    print("Time[s]:", str(play_time))

    rospy.sleep(play_time)
    return True

def openjtalk_srv(srv_req):
    result = open_jtalk(srv_req.text)
    return TextToSpeechResponse(result)

def main():
    rospy.init_node("tts_open_jtalk", anonymous=True)
    srv = rospy.Service("/speech_word", TextToSpeech, openjtalk_srv)
    rospy.loginfo("Ready to 'text to speech(Japanese)'.")
    rospy.spin()

if __name__ == "__main__":
    main()
