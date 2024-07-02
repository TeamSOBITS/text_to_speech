<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]


# text_to_speech
<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#セットアップ">セットアップ</a>
      <ul>
        <li><a href="#環境条件">環境条件</a></li>
        <li><a href="#インストール方法">インストール方法</a></li>
      </ul>
    </li>
    <li><a href="#実行・操作方法">実行・操作方法</a></li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <li><a href="#変更履歴">変更履歴</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#参考文献">参考文献</a></li>
  </ol>
</details>

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

## 概要

文章や文字を発話する音声機能です．


<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- セットアップ -->
## セットアップ

ここで，本レポジトリのセットアップ方法について説明します．

### 環境条件

まず，以下の環境を整えてから，次のインストール段階に進んでください．

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| Python | 3.8 |

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


## インストール方法
１．'src'フォルダに移動します．
```sh
$ cd ~/catkin_ws/src
```

２．本レポジトリをcloneします．
```sh
$ git clone https://github.com/TeamSOBITS/text_to_speech.git
```


３．レポジトリの中へ移動します．
```sh
$ cd text_to_speech/
```


４．依存パッケージをインストールします．
```sh 
$ bash install.sh
```

５．パッケージをコンパイルします．
```sh
$ cd ../../ && catkin_make
```
<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


## 実行・操作方法

#### launchファイルの種類
本レポジトリには２つのlaunchファイルがあります．
launchを実行したときに以下のプログラムが起動します．
- english.launch
    - tts_pico.py
- japanese.launch
    - tts_open_jtalk.py
<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


#### launchファイルの起動方法

- 英語
```sh
$ roslaunch text_to_speech english.launch
```

- 日本語
```sh
$ roslaunch text_to_speech japanese.launch
```
<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

#### Example Code
</details>
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
    message = '文字を入れて下さい'
    send_message = tts_service(message)
    rospy.loginfo(message)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

```
</details>

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

#### Service List
    /speech_word (sobits_msgs/TextToSpeech)

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


## open_jtalkの声質の変え方 
**text_to_speech/launch/japanese.launch**の５行目で声質のデータを読み込んでいます（~.htsvoice)．
その部分を別のhtsvoiceデータに書き換えてください．
htsvoiceデータは、**text_to_speech/open_jtalk_voice_data**の中にあります．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- マイルストーン -->
## マイルストーン

- [x] OSS
    - [x] ドキュメンテーションの英語化
    - [x] ライセンスの追加


現時点のバッグや新規機能の依頼を確認するために[Issueページ](https://github.com/TeamSOBITS/text_to_speech/issues) をご覧ください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

## 変更履歴
 - 

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- 参考文献 -->
## 参考文献

* []()

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

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
[license-url]: LICENSE
