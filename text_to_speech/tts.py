import rclpy
from rclpy.node import Node
import pygame
# from sobits_interfaces.srv import TextToSpeech
from sobits_interfaces.action import TextToSpeech

from ament_index_python.packages import get_package_share_directory
from rclpy.action import ActionServer, GoalResponse, CancelResponse

import subprocess
import codecs
import os
import soundfile as sf
import wave
import time

# SAVE_PATH = "/home/sobits/colcon_ws/src/text_to_speech/voice/speech_word.wav"
class TTS(Node):
    def __init__(self):
        super().__init__("text_to_speech")

        # Declare parameters
        self.declare_parameter('voice_data', '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice')
        self.declare_parameter('language', 'ja')

        # Get parameters
        self.voice_data_ = self.get_parameter('voice_data').get_parameter_value().string_value
        self.language_ = self.get_parameter('language').get_parameter_value().string_value

        self.filename = os.path.join(get_package_share_directory('text_to_speech'), 'sounds', 'output')

        # self.srv = self.create_service(
        #     TextToSpeech, "speech_word", self.tts_server
        # )
        self.action_server = ActionServer(
            self, TextToSpeech, 'speech_word',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback)

        self.get_logger().info("Ready to 'text to speech'.")

    def goal_callback(self, goal_request):
        self.get_logger().info("Received goal request")
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info("Received cancel request")
        return CancelResponse.ACCEPT

    def tts_en(self, text):
        # decode
        speech_text = codecs.decode(str(text).encode('utf-8'))
        
        # Blank check
        if not speech_text or not speech_text.strip():
            self.get_logger().error("Input text is empty or blank.")
            return False
        
        # Unicode error check
        try:
            self.get_logger().info("Input text [" + str(speech_text) + " ] ")
        except Exception as e:
            self.get_logger().error(e)
            return False

        # remove old file
        if os.path.exists(self.filename + ".wav"):
            cmd = "rm %s" % (self.filename + ".wav")
            subprocess.call(cmd, shell=True)

        # create wav file
        cmd = "pico2wave -w %s '%s' " % ((self.filename + ".wav"), speech_text)
        subprocess.call(cmd, shell=True)

        # get play time
        f = sf.SoundFile(self.filename + ".wav")
        play_time = float(len(f)) / float(f.samplerate)
        self.get_logger().info(f'Time[s]: {str(play_time)}')

        # play wav file and sleep
        # cmd = "aplay %s" % (self.filename + ".wav")
        # subprocess.Popen(cmd, shell=True)
        # time.sleep(play_time)
        # return True
        return play_time

    def tts_ja(self, speech_word):
        self.get_logger().info(f"speech_word: {speech_word}")
        
        # Storing commands in variables and executing them collectively at the end.
        open_jtalk = ['open_jtalk'] 

        mech = ['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic'] # dictionary

        # voice_data
        htsvoice = ['-m', self.voice_data_] 
        #htsvoice = ['-m', '/path/to/hoge.htsvoice']


        # option setting（http://moblog.absgexp.net/openjtalk/)
        all_pass = ['-a', '0.5']
        post_filter = ['-b', '0.3']
        speed = ['-r', '1.0']

        out_wav = ['-ow', self.filename + ".wav"] # wav file place setting
        out_log = ['-ot', self.filename + ".log"] # log file place setting

        # including variable name
        cmd = open_jtalk+mech+htsvoice+speed+out_wav+out_log+all_pass+post_filter

        # execute in subprocess
        with subprocess.Popen(cmd, stdin=subprocess.PIPE) as execute:
            execute.stdin.write(speech_word.encode('utf-8'))
            execute.stdin.close()
            execute.wait()

        # get play time
        wf = wave.open(self.filename + ".wav" , "r" )
        play_time =  float(wf.getnframes()) / wf.getframerate()
        self.get_logger().info(f"Time[s]: {str(play_time)}")

        #replay [] not change
        # playback_cmd = ['aplay', '-q', self.filename + ".wav"]
        # subprocess.Popen(playback_cmd)

        # time.sleep(play_time)
        # return True
        return play_time

    # def tts_server(self, request, response):
    #     if self.language_ == "en":
    #         responce = self.tts_en(request.text)
    #     elif self.language_ == "ja":
    #         responce = self.tts_ja(request.text)
    #     return response
    
    def execute_callback(self, goal_handle):
        thread_node = Node("execute_callback_textt_to_speech")
        feedback = TextToSpeech.Feedback()
        response = TextToSpeech.Result()

        text = goal_handle.request.text
        self.get_logger().info(f"Processing TTS request: {codecs.decode(str(text).encode('utf-8'))}")

        response.success = False
        response.total_time = 0.0

        play_time = 0
        if self.language_ == "en":
            play_time = self.tts_en(text)
        elif self.language_ == "ja":
            play_time = self.tts_ja(text)

        pygame.mixer.init()
        pygame.mixer.music.load(self.filename + ".wav")
        pygame.mixer.music.play()

        if (play_time != 0):
            interval = 0.1
            feedback.remaining_time = play_time
            # time.sleep(play_time)
            while rclpy.ok():
                if goal_handle.is_cancel_requested:
                    self.get_logger().info('Goal canceled')
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    goal_handle.canceled()
                    thread_node.destroy_node()
                    del thread_node
                    return response

                rclpy.spin_once(thread_node, timeout_sec=0.1)
                response.total_time += interval
                feedback.remaining_time -= interval

                if (feedback.remaining_time <= 0.0):
                    break
                else:
                    goal_handle.publish_feedback(feedback)

            feedback.remaining_time = 0.0
            goal_handle.publish_feedback(feedback)
            self.get_logger().info("TTS processing and playback completed.")

            response.success = True
            goal_handle.succeed()

        thread_node.destroy_node()
        del thread_node
        return response

# メイン
def main(args=None):
    rclpy.init(args=args)

    server = TTS()

    rclpy.spin(server)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
