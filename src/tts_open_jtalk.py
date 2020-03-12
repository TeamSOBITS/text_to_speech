#!/usr/bin/env python
#coding: utf-8
import subprocess
import rospy
import wave
from text_to_speech.srv import *
from std_msgs.msg import *

def open_jtalk(speech_word):
    rospy.loginfo("speech_word:[%s]"%speech_word)
    sobit_mini_head_status_publisher = rospy.Publisher("/sobit_mini_head/status", String, queue_size=10)
    
    # コマンドを変数に格納して、最後にまとめて実行する
    open_jtalk = ['open_jtalk'] # これはそのまま

    mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic'] # 辞書？

    htsvoice = ['-m', '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'] #声質のデータ
    #htsvoice = ['-m', '/path/to/hoge.htsvoice']


    # オプションの設定（http://moblog.absgexp.net/openjtalk/)
    all_pass = ['-a', '0.5']
    post_filter = ['-b', '0.3']
    speed = ['-r', '1.0']

    out_wav = ['-ow', './open_jtalk.wav'] # 音声ファイルの保存場所の設定
    out_log = ['-ot', './open_jtalk.log'] # ログの保存場所の設定

    # 変数をまとめる
    cmd = open_jtalk+mech+htsvoice+speed+out_wav+out_log+all_pass+post_filter

    # subprocessで実行する
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(speech_word)
    c.stdin.close()
    c.wait()

    #再生
    aplay = ['aplay', '-q', './open_jtalk.wav']
    sobit_mini_head_status_publisher.publish("speaking")
    wr = subprocess.Popen(aplay)

    #発話時間の表示
    wf = wave.open("./open_jtalk.wav" , "r" )
    play_time =  float(wf.getnframes()) / wf.getframerate()
    print "Time[s]:%s"%str(play_time)

    rospy.sleep(play_time)
    sobit_mini_head_status_publisher.publish("normal")

    return True

def openjtalk_srv(srv_req):
    result = open_jtalk(srv_req.text)
    if result == True:
        return TextToSpeechResponse(True)
    else:
        return TextToSpeechResponse(False)


def openjtalk_msg(sub_msg):
    pub = rospy.Publisher("tts_result", Bool, queue_size=1)
    result = open_jtalk(sub_msg.data)
    if result == True:
        pub.publish(True)
    else:
        pub.publish(False)

def main():
    rospy.init_node("tts_open_jtalk", anonymous=True)
    sub = rospy.Subscriber("/speech_word", String, openjtalk_msg)
    srv = rospy.Service("/speech_word", TextToSpeech, openjtalk_srv)
    rospy.loginfo("Ready to 'text to speech(Japanese)'.")
    rospy.spin()

if __name__ == "__main__":
    main()
