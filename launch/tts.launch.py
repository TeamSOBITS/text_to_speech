import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='text_to_speech',
            executable='tts',
            name='text_to_speech',
            output='screen',
            parameters=[
                {'voice_data': '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'},
                {'language': 'en'},
            ]
        ),
    ])
