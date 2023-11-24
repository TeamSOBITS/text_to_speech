#!/usr/bin/env python3
#coding: utf-8
import subprocess
import rospy
import wave
from text_to_speech.srv import *
from std_msgs.msg import *

def open_jtalk(speech_word):
    rospy.loginfo("speech_word:[%s]"%speech_word)
    
    # コマンドを変数に格納して、最後にまとめて実行する
    open_jtalk = ['open_jtalk'] # これはそのまま

    mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic'] # 辞書？

    # 声質のデータ
    htsvoice = ['-m', rospy.get_param("voice_data")] #声質のデータ
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
    with subprocess.Popen(cmd, stdin=subprocess.PIPE) as execute:
        execute.stdin.write(speech_word.encode('utf-8'))
        execute.stdin.close()
        execute.wait()

    #再生 []内の内容は変更NG
    playback_cmd = ['aplay', '-q', './open_jtalk.wav']
    subprocess.Popen(playback_cmd)

    #発話時間の表示
    wf = wave.open("./open_jtalk.wav" , "r" )
    play_time =  float(wf.getnframes()) / wf.getframerate()
    print("Time[s]:", str(play_time))

    rospy.sleep(play_time)
    return True

def openjtalk_srv(srv_req):
    result = open_jtalk(srv_req.text)
    return TextToSpeechResponse(result)

def openjtalk_msg(sub_msg):
    pub = rospy.Publisher("tts_result", Bool, queue_size=1)
    result = open_jtalk(sub_msg.data)
    pub.publish(result)

def main():
    rospy.init_node("tts_open_jtalk", anonymous=True)
    sub = rospy.Subscriber("/speech_word", String, openjtalk_msg)
    srv = rospy.Service("/speech_word", TextToSpeech, openjtalk_srv)
    rospy.loginfo("Ready to 'text to speech(Japanese)'.")
    rospy.spin()

if __name__ == "__main__":
    main()
