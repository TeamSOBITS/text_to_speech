<a name="readme-top"></a>

[JP](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
<!-- [![MIT License][license-shield]][license-url] -->


# text_to_speech
<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#環境構築">環境構築</a>
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
$ sh install.sh
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

#### Subscribed Topics
    /speech_word (std_msgs/String)

#### Service List
    /speech_word (text_to_speech/TextToSpeech)

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


## open_jtalkの声質の変え方 
**text_to_speech/launch/japanese.launch**の５行目で声質のデータを読み込んでいます（~.htsvoice)．
その部分を別のhtsvoiceデータに書き換えてください．
htsvoiceデータは、**text_to_speech/open_jtalk_voice_data**の中にあります．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- マイルストーン -->
## マイルストーン

- [ ] OSS
    - [ ] ドキュメンテーションの英語化
    - [ ] ライセンスの追加


現時点のバッグや新規機能の依頼を確認するために[Issueページ](https://github.com/github_username/repo_name/issues) をご覧ください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

## 変更履歴
 - 

<!-- 参考文献 -->
## 参考文献

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[license-url]: LICENSE