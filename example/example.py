#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rospy
from text_to_speech.srv import TextToSpeech

def tts_service(msg):
    rospy.wait_for_service('speech_word')
    try:
        first_con = rospy.ServiceProxy('speech_word',TextToSpeech)
        responce = first_con(msg)
        return responce.result
    except rospy.ServiceException as e:
        print("could not call: %s",e)

def main():
    rospy.init_node('text_to_speech',anonymous=True)
    rospy.sleep(0.1)

    # Please insert the text within ''
    message = 'メッセージを入れて下さい'
    send_message = tts_service(message)
    rospy.loginfo(message)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass