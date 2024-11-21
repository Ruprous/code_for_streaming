
# multiple_start.bat

## 概要
`multiple_start.bat` は、複数のソフトウェアやスクリプトを順番に実行し、特定の条件で終了させるためのバッチファイルです。  
特に、Pythonスクリプトを **他のPythonプロセスに影響を与えず** に終了する仕組みを備えています。

---

## ファイル構成
- **multiple_start.bat**  
  実行用のバッチファイル。
- **README.md**  
  このファイル（説明書）。

---

## 使い方
1. **ファイルの編集**  
   `multiple_start.bat` 内の以下の箇所を、実行したいソフトやスクリプトに応じて編集します。

   - **OBSの実行パス**
     ```bat
     start "" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
     ```
     OBS Studioがインストールされているパスを指定してください。

   - **Pythonスクリプトのパス**
     ```bat
     start "MyPythonScript" python "C:\path\to\your_script.py"
     ```
     実行したいPythonスクリプトのパスを指定してください。

2. **バッチファイルの実行**  
   バッチファイルをダブルクリックして実行します。

3. **終了方法**  
   実行中に「`end`」と入力してEnterキーを押すと、以下のプロセスが終了します。
   - 起動したOBS Studio
   - 起動した特定のPythonスクリプト（`MyPythonScript`）

---

## 仕組み
- **順番に実行**
  - まずOBSを起動し、その後指定されたPythonスクリプトを起動します。
- **終了条件**
  - バッチファイル内で「`end`」と入力するまで、プロセスは動き続けます。
  - 特定のウィンドウタイトル（`MyPythonScript`）を指定して終了させるため、他のPythonプロセスに影響を与えません。

---

## 注意点
1. **Pythonのパスが環境変数に登録されていない場合**  
   以下のようにPythonのフルパスを指定してください。
   ```bat
   start "MyPythonScript" "C:\Python39\python.exe" "C:\path\to\your_script.py"
   ```

2. **OBSがインストールされているディレクトリ**  
   OBS Studioのインストールパスを正確に指定してください。

3. **他のPythonプロセスへの影響**
   このバッチファイルは、タイトル付きで起動したPythonスクリプトのみを終了対象とするため、他のプロセスに影響を与えません。

---

## 更新履歴
- **v1.0** 初期リリース  
  - OBSの起動
  - 特定Pythonスクリプトの起動と安全な終了

