<a name="readme-top"></a>

[JP](readme.md) | [EN](template_readme_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
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
    <li><a href="#issues">Issues</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#references">References</a></li>
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- setup -->

## Overview
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
$ sh install.sh
```

5. Compile the package.
```sh
$ cd ../../ && catkin_make
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to Use
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

#### Subscribed Topics
    /speech_word (std_msgs/String)

#### Service List
    /speech_word (text_to_speech/TextToSpeech)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MILESTONE -->
## Milestone

- [ ] OSS
    - [ ] Translate documentation into English
    - [ ] Adding License

See the [open issues][license-url] for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## How to change the voice in _open jtalk_ 
In **text_to_speech/launch/japanese.launch**, the voice quality data（~.htsvoice) is loaded on line 5.  
Replace that part with another htsvoice data. 
htsvoice data can be found in **text_to_speech/open_jtalk_voice_data**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## References


<p align="right">(<a href="#readme-top">back to top</a>)</p>
