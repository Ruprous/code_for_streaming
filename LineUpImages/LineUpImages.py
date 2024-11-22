#©2024 Ruprous
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from PIL import Image, ImageOps

def get_image_files(directory):
    """ディレクトリ内の画像ファイルを取得"""
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")  # 対応する拡張子
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(valid_extensions)]

def arrange_images_with_margin(input_directory, output_path, fixed_width=3000):
    # ディレクトリ内の画像を取得
    image_paths = get_image_files(input_directory)
    if not image_paths:
        print("指定したディレクトリには画像ファイルがありません。")
        return
    
    # ユーザーから横の画像数（列数）を指定
    columns = int(input("横に並べたい画像の数（列数）を入力してください: "))
    
    # マージンを指定（0〜300の範囲チェック）
    while True:
        margin = int(input("画像と画像の間のマージン（px）を入力してください（0〜300の範囲）: "))
        if 0 <= margin <= 300:
            break
        print("マージンは0〜300の範囲内で指定してください。")
    
    # 画像を開く
    images = [Image.open(path) for path in image_paths]
    
    # 横幅を固定し、各画像のサイズを計算
    single_size = (fixed_width - (columns - 1) * margin) // columns
    resize_to = (single_size, single_size)
    
    # 全画像をリサイズ（指定の正方形サイズにする）
    resized_images = [ImageOps.pad(img, resize_to, method=Image.Resampling.LANCZOS) for img in images]
    
    # 総画像数
    total_images = len(resized_images)
    
    # 行数を計算
    rows = (total_images + columns - 1) // columns
    
    # キャンバスのサイズ計算
    canvas_width = fixed_width
    canvas_height = rows * single_size + (rows - 1) * margin
    
    # 新しいキャンバスを作成
    canvas = Image.new("RGB", (canvas_width, canvas_height), color="white")
    
    # キャンバスに画像を貼り付け
    for idx, img in enumerate(resized_images):
        row, col = divmod(idx, columns)
        x = col * (single_size + margin)
        y = row * (single_size + margin)
        canvas.paste(img, (x, y))
    
    # 保存（PNG形式で出力）
    canvas.save(output_path, format="PNG")
    print(f"画像を保存しました: {output_path}")

if __name__ == "__main__":
    # Tkinterを使ってディレクトリを選択
    Tk().withdraw()  # GUIウィンドウを非表示にする
    input_directory = askdirectory(title="画像が保存されているディレクトリを選択してください")
    if not input_directory:
        print("ディレクトリが選択されませんでした。")
    else:
        output_path = input("出力するファイル名（例: output.png）を入力してください: ").strip()
        arrange_images_with_margin(input_directory, output_path, fixed_width=3000)
