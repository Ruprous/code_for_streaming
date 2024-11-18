#Copyright (c) 2024 Ruprous
import pytesseract
from PIL import ImageGrab, Image, ImageEnhance, ImageOps
import time
import math
import threading
import re
import keyboard  # キー入力を監視するためのライブラリ

# Tesseractのパス設定
pytesseract.pytesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# 各座標設定
self_signal_positions = {
    "Signal 1": (936, 1063), 
    "Signal 2": (969, 1059),
}
opponent_signal_positions = {
    "Signal 1": (934, 58), 
    "Signal 2": (967, 59),
}

# 相手の名前エリアの通常範囲と大きな範囲
opponent_name_area_large = (819, 577, 1101, 616)  # 大きな表示エリアに更新
self_time_area = (716, 1044, 774, 1069)           # 自分の持ち時間エリア
opponent_time_area = (1167, 36, 1218, 65)         # 相手の持ち時間エリア

target_color = (255, 213, 30)  # 判定する色（#FFD51E）

# 名前を保持する変数
stored_opponent_name = ""  # 初期状態で相手の名前を保持する

def preprocess_image(img):
    """画像を前処理してOCR精度を向上"""
    img = ImageOps.grayscale(img)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # コントラスト強調
    img = img.point(lambda x: 0 if x < 128 else 255, '1')  # 二値化
    return img

def capture_text_from_area(bbox, lang='tessdata/eng'):
    """指定エリアのテキストをOCRで読み取る"""
    img = ImageGrab.grab(bbox)
    
    # 画像を3倍に拡大してバイリニア補完
    img = img.resize((img.width * 3, img.height * 3), Image.BILINEAR)
    
    img = preprocess_image(img)  # 前処理を追加
    text = pytesseract.image_to_string(img, config='--psm 7', lang=lang)
    return text.strip()

def remove_spaces(text):
    """名前からスペースや空白を削除"""
    return re.sub(r'\s+', '', text)

def filter_time_text(text):
    """時間テキストから数字と「:」のみを残す"""
    return re.sub(r'[^0-9:]', '', text)

def is_color_match(color1, color2, tolerance=150):
    """指定色がターゲットカラーに近いかを判定"""
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2))) < tolerance

def check_signal_state(signal_positions, screenshot):
    """各信号機のピクセル色をチェックして状態を取得"""
    states = []
    for signal_name, position in signal_positions.items():
        pixel_color = screenshot.getpixel(position)
        if is_color_match(pixel_color, target_color):
            if signal_name == "Signal 1":
                states.append("●")
            elif signal_name == "Signal 2":
                states.append("●")
    return "".join(states) if states else " "

def update_signal_state():
    """信号機の状態を3秒ごとに更新"""
    global self_signal_text, opponent_signal_text
    while True:
        screenshot = ImageGrab.grab()
        # 自分の信号機状態
        self_signal_text = check_signal_state(self_signal_positions, screenshot)
        # 相手の信号機状態
        opponent_signal_text = check_signal_state(opponent_signal_positions, screenshot)

        # 自分用の信号状態を保存するファイルに書き出し
        with open("./self_signal_status.txt", "w", encoding="utf-8") as f:
            f.write(f"{self_signal_text}\n")
        
        # 相手用の信号状態を保存するファイルに書き出し
        with open("./opponent_signal_status.txt", "w", encoding="utf-8") as f:
            f.write(f"{opponent_signal_text}\n")
        
        time.sleep(1)

# スレッドを使って信号機の状態を3秒ごとに更新
signal_thread = threading.Thread(target=update_signal_state)
signal_thread.daemon = True
signal_thread.start()

# 自分の名前は固定
self_name = "Ruprous"
self_signal_text = ""
opponent_signal_text = ""

# `p`キーが押されたときに相手の名前を更新するイベントリスナー
def on_p_key_event(e):
    global stored_opponent_name
    opponent_name_raw = capture_text_from_area(opponent_name_area_large, lang='tessdata/jpn+tessdata/eng')
    stored_opponent_name = remove_spaces(opponent_name_raw)  # 名前を更新

# `p`キーが押された時のイベントを登録
keyboard.on_press_key('p', on_p_key_event)

while True:
    # 名前と時間情報を使用
    opponent_name = stored_opponent_name  # 変数を保持して使用
    self_time = filter_time_text(capture_text_from_area(self_time_area, lang='tessdata/eng'))
    opponent_time = filter_time_text(capture_text_from_area(opponent_time_area, lang='tessdata/eng'))
    
    # player_info.txtに自分の情報を書き出し
    with open("./player_info.txt", "w", encoding="utf-8") as f:
        f.write(f"{self_name}\n")
        f.write(f"{self_time}")
    
    # opponent_info.txtに相手の情報を書き出し
    with open("./opponent_info.txt", "w", encoding="utf-8") as f:
        f.write(f"{opponent_name}\n")
        f.write(f"{opponent_time}")
    
    time.sleep(0.5)
