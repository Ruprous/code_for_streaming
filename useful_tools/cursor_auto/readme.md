
# マウス座標キャプチャツール

このPythonスクリプトは、マウスカーソルの現在位置（x, y座標）をリアルタイムで表示するツールです。`Ctrl+C`を押すことで終了できます。

## 使用方法

1. 必要なPythonモジュールをインストールします。
   ```bash
   pip install pyautogui
   ```

2. 以下のコードをPythonファイル（例: `mouse_capture.py`）に保存します。

   ```python
   # Copyright (c) 2024 Ruprous

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
   ```

3. スクリプトを実行します。
   ```bash
   python mouse_capture.py
   ```

4. コンソールにリアルタイムでマウス座標が表示されます。
   ```
   現在の位置: x=100, y=200
   現在の位置: x=120, y=210
   ...
   ```

5. 必要な座標を確認したら、`Ctrl+C`を押してスクリプトを終了します。

---

## コードの詳細

### 1. 必要なライブラリ
```python
import pyautogui
import time
```
- **`pyautogui`**: マウスやキーボード操作を行うライブラリ。
- **`time`**: 実行間隔を調整するために使用。

### 2. スクリプト開始メッセージ
```python
print("マウスをキャプチャしたい場所に移動してください。Ctrl+Cで停止します。")
```
- ユーザーに操作の準備を促すメッセージを表示。

### 3. マウス座標の取得と表示
```python
while True:
    x, y = pyautogui.position()  # 現在のマウス座標を取得
    print(f"現在の位置: x={x}, y={y}")
    time.sleep(1)
```
- **`pyautogui.position()`**: 現在のマウスカーソルの座標を取得。
- **`time.sleep(1)`**: 1秒ごとに座標を更新。

### 4. スクリプトの終了処理
```python
except KeyboardInterrupt:
    print("\n座標の確認を終了しました。")
```
- `Ctrl+C`による中断をキャッチし、終了メッセージを表示。

---

## 注意事項

- このスクリプトを実行するには、Pythonと`pyautogui`ライブラリが必要です。
- **環境によっては`pyautogui`が正常に動作しない場合があるため、ドキュメントを参照してください。**
  - [PyAutoGUI公式ドキュメント](https://pyautogui.readthedocs.io/)

---
