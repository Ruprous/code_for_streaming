#Copyright (c) 2024 Ruprous

import pyautogui
import time

print("マウスをキャプチャしたい場所に移動してください。Ctrl+Cで停止します。")
try:
    while True:
        x, y = pyautogui.position()  # 現在のマウス座標を取得
        print(f"現在の位置: x={x}, y={y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n座標の確認を終了しました。")
