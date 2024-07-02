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
$ cd ~/catkin_ws/src
```

2. Clone this repository.
```sh
$ git clone https://github.com/TeamSOBITS/text_to_speech.git
```

3. Navigate tp the repository.
```sh
$ cd text_to_speech/  
```

4. Install dependencies.
```sh
$ bash install.sh
```

5. Compile the package.
```sh
$ cd ../../ && catkin_make
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Launch and Usage
#### Types of Launch Files
There are two launch files in this repository. When you execute the launch, the following programs will start.
- english.launch
    - tts_pico.py
- japanese.launch
    - tts_open_jtalk.py
<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Launching Files

- English
```sh
$ roslaunch text_to_speech english.launch
```

- japanese
```sh
$ roslaunch text_to_speech japanese.launch
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Example Code
<details>
<summary>Python</summary>

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rospy
from sobits_msgs.srv import TextToSpeech

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
    message = 'please in the text'
    send_message = tts_service(message)
    rospy.loginfo(message)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

```
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### Service List
    /speech_word (sobits_msgs/TextToSpeech)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to change the voice in _open jtalk_ 
In **text_to_speech/launch/japanese.launch**, the voice quality data（~.htsvoice) is loaded on line 5.  
Replace that part with another htsvoice data. 
htsvoice data can be found in **text_to_speech/open_jtalk_voice_data**.

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
