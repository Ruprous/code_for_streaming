from googleapiclient.discovery import build
from flask import Flask, render_template
import threading
import time

# Google APIキーを設定
API_KEY = "YOUR_API_KEY"  # ここに取得したAPIキーを入力
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Flaskアプリケーションのセットアップ
app = Flask(__name__)
comments = []  # コメントを保持するリスト

@app.route('/')
def display_comments():
    global comments
    # コメントをテンプレートに渡して表示
    return render_template("index.html", comments=comments[-10:])  # 最新10件のみ表示

def get_live_chat_id(video_id):
    # YouTube APIを使ってライブチャットIDを取得
    response = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    ).execute()
    live_chat_id = response['items'][0]['liveStreamingDetails']['activeLiveChatId']
    return live_chat_id

def fetch_comments(live_chat_id):
    global comments
    while True:
        # ライブチャットのコメントを取得
        response = youtube.liveChatMessages().list(
            liveChatId=live_chat_id,
            part="snippet"
        ).execute()
        for item in response['items']:
            message = item['snippet']['displayMessage']
            comments.append(message)
        time.sleep(2)  # コメント取得の間隔を2秒に設定

def start_flask():
    # Flaskサーバーをポート5000で起動
    app.run(port=5000)

if __name__ == "__main__":
    video_id = input("ライブ配信の動画IDを入力してください: ")
    live_chat_id = get_live_chat_id(video_id)

    # Flaskを別スレッドで実行
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # コメント取得を開始
    fetch_comments(live_chat_id)
