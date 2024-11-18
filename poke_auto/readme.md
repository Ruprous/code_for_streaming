
# ポケポケ（Pokemon TCG Pocket）自動情報取得ツール

このPythonスクリプトは、Androidエミュレータ（BlueStacksやNOXPlayerなど）でポケポケをフルスクリーンでプレイ中に以下の情報を取得します：

- **相手の名前**（手動で取得：`P`キーを押す）
- **試合の進行状況**（自分と相手の点数(信号機ってcode内では書いてます)）
- **自分と相手の持ち時間**（自動で取得）

## 必要な環境

- Python 3.6以上
- 以下のPythonライブラリをインストール
  ```bash
  pip install pytesseract pillow keyboard
  ```
- Tesseract OCR（[公式ページ](https://github.com/tesseract-ocr/tesseract)からインストール）
  - Tesseractのパスをスクリプト内で設定してください（例: `C:/Program Files/Tesseract-OCR/tesseract.exe`）。

## 使用方法

1. 必要なライブラリをインストール。
2. スクリプトをエディタにコピーし、保存します（例: `poke_auto.py`）。
3. 以下の設定を確認してください。
   - **エリアの座標（`self_time_area`や`opponent_time_area`など）**を自分の画面解像度に合わせて調整。
   - **Tesseractのパス（`pytesseract.pytesseract_cmd`）**を正しく設定。
4. スクリプトを実行します。
   ```bash
   python poke_auto.py
   ```
5. エミュレータでポケポケをフルスクリーンで起動します。
6. 以下の操作が可能です。
   - **`P`キー**: 相手の名前を取得して保存します。
   - **自動処理**: 持ち時間や信号機状態を取得し、テキストファイルに保存します。

## 出力ファイル

スクリプトは以下のテキストファイルを生成します：

- `player_info.txt`: 自分の名前と持ち時間を記録。
- `opponent_info.txt`: 相手の名前と持ち時間を記録。
- `self_signal_status.txt`: 自分の信号機状態を記録。
- `opponent_signal_status.txt`: 相手の信号機状態を記録。

## スクリプト概要

### 主な機能

1. **OCRを使用してテキスト取得**
   - `pytesseract`を利用して特定のエリアからテキストを読み取ります。
2. **名前と時間の取得**
   - 相手の名前：`P`キー押下時に取得。
   - 持ち時間：特定エリアをOCRで読み取ります。
3. **信号機の状態を確認**
   - 特定の座標で色を判定し、状態を記録。
4. **マルチスレッドでの処理**
   - 信号機状態の更新は別スレッドで1秒ごとに実行。

### キー機能

#### OCR処理
```python
def capture_text_from_area(bbox, lang='tessdata/eng'):
    img = ImageGrab.grab(bbox)
    img = img.resize((img.width * 3, img.height * 3), Image.BILINEAR)
    img = preprocess_image(img)
    text = pytesseract.image_to_string(img, config='--psm 7', lang=lang)
    return text.strip()
```
- 指定したエリア（`bbox`）をOCRで読み取り、文字列を返します。

#### 色判定
```python
def is_color_match(color1, color2, tolerance=150):
    return math.sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(color1, color2))) < tolerance
```
- ピクセルの色が指定の色に近いかどうかを判定します。

#### ファイル出力
```python
with open("./player_info.txt", "w", encoding="utf-8") as f:
    f.write(f"{self_name}\n")
    f.write(f"{self_time}")
```

### 注意点

- エミュレータの解像度に合わせて座標を調整してください。
- OCRの精度向上のため、画像処理の設定をカスタマイズ可能。
- このスクリプトはWindows環境で動作を想定しています。

---

## 問題が発生した場合

1. **OCRが正しく動作しない場合**：
   - Tesseractのパスが正しいか確認してください。
   - 解像度やエリア座標が適切か確認してください。

2. **テキストファイルが生成されない場合**：
   - スクリプトの書き込み権限を確認してください。

3. **色判定が誤動作する場合**：
   - `target_color`や`tolerance`の値を調整してください。

---
