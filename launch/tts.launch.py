import os
from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='text_to_speech',
            executable='tts',
            name='text_to_speech',
            output='screen',
            parameters=[
                {
                    'voice_data': '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice',
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "cmu_us_arctic_slt.htsvoice"),
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "mei_angry.htsvoice"),
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "mei_bashful.htsvoice"),
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "mei_happy.htsvoice"),
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "mei_normal.htsvoice"),
                    # 'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "mei_sad.htsvoice"),
                    'language': 'en',
                    # 'language': 'ja',
                },
            ]
        ),
    ])
