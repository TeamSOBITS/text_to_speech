#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import rclpy
from rclpy.action import ActionClient
from sobits_interfaces.action import TextToSpeech  # sobits_msgs/action/TextToSpeech.action

def tts_action(node, text):
    """
    アクションクライアントを使ってサーバーにテキストを送信し,結果を取得します.
    """
    # アクションクライアントの生成
    action_client = ActionClient(node, TextToSpeech, '/speech_word')

    # サーバーが準備できるまで待機
    node.get_logger().info('アクションサーバーを待機中...')
    action_client.wait_for_server()

    # ゴールメッセージの作成
    goal_msg = TextToSpeech.Goal()
    goal_msg.text = text

    # ゴールを送信し、結果を待機
    node.get_logger().info(f'ゴールを送信中: "{text}"')
    future = action_client.send_goal_async(goal_msg)
    rclpy.spin_until_future_complete(node, future)

    # ゴールが受け入れられたかチェック
    goal_handle = future.result()
    if not goal_handle.accepted:
        node.get_logger().error('ゴールが拒否されました.')
        return

    # 結果を待機
    result_future = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_future)
    result = result_future.result().result

    # 結果を表示
    if result.success:
        node.get_logger().info('音声合成が成功しました！')
    else:
        node.get_logger().error('音声合成に失敗しました.')


def main():
    try:
        while True:
            # ユーザーからの入力を取得
            input_text = input('音声合成するテキストを入力してください ("EXIT"で終了): ')
            
            # プログラム終了判定
            if input_text.strip() == 'EXIT':
                print('プログラムを終了します.')
                break
            
            # 空白文字や空の入力の場合は再入力を促す
            if not input_text.strip():
                print('テキストが空です.再入力してください.')
                continue

            # TTS アクションを呼び出す
            tts_action(node, input_text)

    except KeyboardInterrupt:
        print('\nプログラムが中断されました.')



if __name__ == '__main__':
    try:
        rclpy.init()
        node = rclpy.create_node('text_to_speech_client')
        main()
    except rclpy.exceptions.ROSInterruptException:
        pass
