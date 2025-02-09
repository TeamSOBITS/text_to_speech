<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
<!-- [![MIT License][license-shield]][license-url] -->


# Text_To_Speech
<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#setup">Setup</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#launch-and-usage">Launch and Usage</a></li>
    <li><a href="#milestone">Milestone</a></li>
    <li><a href="#change-log">Change Log</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#references">References</a></li>
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- setup -->

## Introduction
This is a speech functionality that vocalizes text and characters.

## Setup
Here, we will explain the setup process for this repository.

### Prerequisites

First, set up the following environment before proceeding to the installation stage.
| System  | Version |
| ------------- | ------------- |
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| Python | 3.8 |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation
#### Install this Repository

1. Move to the 'src' folder.
```sh
$ cd ~/colcon_ws/src
```

2. Clone this repository.
```sh
$ git clone https://github.com/TeamSOBITS/text_to_speech.git
```

3. Navigate tp the repository.
```sh
$ cd text_to_speech/  
```

4. Switch to the appropriate branch:
```sh
$ git checkout humble-devel
```

5. Install dependencies.
```sh
$ bash install.sh
```

6. Compile the package.
```sh
$ cd ../../ && colcon build
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Launch and Usage

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Launching Files

```sh
$ ros2 launch text_to_speech tts.launch.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Example Code
<details>
<summary>Python</summary>

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rclpy
from rclpy.action import ActionClient
from sobits_interfaces.action import TextToSpeech  # sobits_msgs/action/TextToSpeech.action

def tts_action(node, text):
    """
    Sends text to the server using an ActionClient and retrieves the result.
    """
    # Create an ActionClient
    action_client = ActionClient(node, TextToSpeech, '/speech_word')

    # Wait for the server to be ready
    node.get_logger().info('Waiting for the action server...')
    action_client.wait_for_server()

    # Create a goal message
    goal_msg = TextToSpeech.Goal()
    goal_msg.text = text

    # Send the goal and wait for the result
    node.get_logger().info(f'Sending goal: "{text}"')
    future = action_client.send_goal_async(goal_msg)
    rclpy.spin_until_future_complete(node, future)

    # Check if the goal was accepted
    goal_handle = future.result()
    if not goal_handle.accepted:
        node.get_logger().error('Goal was rejected.')
        return

    # Wait for the result
    result_future = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)
    result = result_future.result().result

    # Display the result
    if result.success:
        node.get_logger().info('Text-to-speech succeeded!')
    else:
        node.get_logger().error('Text-to-speech failed.')

def main():
    try:
        while True:
            # Get input from the user
            input_text = input('Enter text for speech synthesis ("exit" to quit): ')

            # Check if the user wants to exit
            if input_text.strip().lower() == 'exit':
                print('Exiting the program.')
                break

            # Prompt for re-entry if the input is empty
            if not input_text.strip():
                print('Text is empty. Please enter again.')
                continue

            # Call the TTS Action
            tts_action(node, input_text)

    except KeyboardInterrupt:
        print('\nProgram interrupted.')


if __name__ == '__main__':
    try:
        # Initialize ROS 2
        rclpy.init()
        node = rclpy.create_node('text_to_speech_client')
        main()
    except rclpy.exceptions.ROSInterruptException:
        pass

```
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Action List
/speech_word (sobits_msgs/action/TextToSpeech.action)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to change the voice in _open jtalk_ 


In **text_to_speech/launch/tts.launch.py**, modify the voice_data parameter to specify the path to the desired .htsvoice file.
#### Default Male Voice
```
'voice_data': '/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice',
```
#### Change to a Female Voice Model
```
'voice_data': os.path.join(get_package_share_directory("text_to_speech"), "open_jtalk_voice_data", "cmu_us_arctic_slt.htsvoice"),
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MILESTONE -->
## Milestone

- [x] OSS
    - [x] Translate documentation into English
    - [x] Adding License

See the [open issues](https://github.com/TeamSOBITS/text_to_speech/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Change Log
 -

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## References
 -

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TeamSOBITS/text_to_speech.svg?style=for-the-badge
[contributors-url]: https://github.com/TeamSOBITS/text_to_speech/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TeamSOBITS/text_to_speech.svg?style=for-the-badge
[forks-url]: https://github.com/TeamSOBITS/text_to_speech/network/members
[stars-shield]: https://img.shields.io/github/stars/TeamSOBITS/text_to_speech.svg?style=for-the-badge
[stars-url]: https://github.com/TeamSOBITS/text_to_speech/stargazers
[issues-shield]: https://img.shields.io/github/issues/TeamSOBITS/text_to_speech.svg?style=for-the-badge
[issues-url]: https://github.com/TeamSOBITS/text_to_speech/issues
[license-shield]: https://img.shields.io/github/license/TeamSOBITS/text_to_speech.svg?style=for-the-badge
[license-url]: https://github.com/TeamSOBITS/text_to_speech/blob/feature/oss/LICENSE
<!-- [license-url]: LICENSE -->
