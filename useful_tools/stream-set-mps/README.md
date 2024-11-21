
# stream-set-mps.bat

## 概要
`stream-set-mps.bat` は、配信に関連する以下のソフトウェアを一括で起動し、必要に応じて一括で終了させることができるバッチファイルです。

- OBS Studio
- わんコメ
- VOICEVOX
- 棒読みちゃん

このバッチファイルを使うことで、複数のソフトを効率的に管理することができます。

---

## ファイル構成
- **stream-set-mps.bat**  
  実行用のバッチファイル。
- **README.md**  
  このファイル（説明書）。

---

## 使い方
1. **ファイルの編集**  
   `stream-set-mps.bat` 内の以下の箇所を、実行したいソフトのインストールパスに応じて編集してください。

   - **OBS Studio**
     ```bat
     start "OBS" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
     ```

   - **わんコメ**
     ```bat
     start "わんコメ" "C:\Program Files\OneComme\わんコメ - OneComme.exe"
     ```

   - **VOICEVOX**
     ```bat
     start "VOICEVOX" "C:\Program Files\VOICEVOX\VOICEVOX.exe"
     ```

   - **棒読みちゃん**
     ```bat
     start "棒読みちゃん" "C:\Program Files\BouyomiChan\BouyomiChan.exe"
     ```

2. **バッチファイルの実行**  
   ファイルをダブルクリックで実行します。

3. **終了方法**  
   実行中にコンソールウィンドウで「`end`」と入力してEnterキーを押すと、起動したすべてのソフトが一括で終了します。

---

## 仕組み
- **順番に実行**
  1. OBS Studioを起動
  2. わんコメを起動
  3. VOICEVOXを起動
  4. 棒読みちゃんを起動

- **終了方法**
  バッチファイル内で「`end`」と入力することで、指定したプロセス（OBS Studio、わんコメ、VOICEVOX、棒読みちゃん）をすべて終了します。

---

## 注意点
1. **ソフトのインストールパス**
   インストール先がデフォルトと異なる場合は、各ソフトのパスを正確に指定してください。

2. **プロセス名**
   `taskkill` コマンドで終了する際、指定されたプロセス名が一致していないと終了できません。

3. **動作確認**
   初回実行時は、各ソフトが正しく起動・終了するか確認してください。

---

## 更新履歴
- **v1.0** 初期リリース  
  - OBS Studio、わんコメ、VOICEVOX、棒読みちゃんの一括起動・終了に対応。

