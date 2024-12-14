import rclpy
from sobits_interfaces.srv import TextToSpeech
from rclpy.node import Node

import subprocess
import codecs
import os
import soundfile as sf
import wave
import time

SAVE_PATH = "/home/sobits/colcon_ws/src/text_to_speech/voice/speech_word.wav"
class TTS(Node):
    def __init__(self):
        super().__init__("text_to_speech")

        # Declare parameters
        self.declare_parameter('voice_data', '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice')
        self.declare_parameter('language', 'ja')

        # Get parameters
        self.voice_data_ = self.get_parameter('voice_data').get_parameter_value().string_value
        self.language_ = self.get_parameter('language').get_parameter_value().string_value

        self.srv = self.create_service(
            TextToSpeech, "speech_word", self.tts_server
        )
        self.get_logger().info("Ready to 'text to speech'.")
    
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
        if os.path.exists(SAVE_PATH):
            cmd = "rm %s" % SAVE_PATH
            subprocess.call(cmd, shell=True)

        # create wav file
        cmd = "pico2wave -w %s '%s' " % (SAVE_PATH, speech_text)
        subprocess.call(cmd, shell=True)

        # get play time
        f = sf.SoundFile(SAVE_PATH)
        play_time = float(len(f)) / float(f.samplerate)
        self.get_logger().info(f'Time[s]: {str(play_time)}')

        # play wav file and sleep
        cmd = "aplay %s" % SAVE_PATH
        subprocess.Popen(cmd, shell=True)
        time.sleep(play_time)
        return True

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
        self.get_logger().info(f"Time[s]: {str(play_time)}")
        time.sleep(play_time)
        return True

    def tts_server(self, request, response):
        if self.language_ == "en":
            responce = self.tts_en(request.text)
        elif self.language_ == "ja":
            responce = self.tts_ja(request.text)
        return response

# メイン
def main(args=None):
    rclpy.init(args=args)

    server = TTS()

    rclpy.spin(server)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
