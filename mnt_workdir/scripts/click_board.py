from tkinter import Tk, Canvas
from PIL import Image, ImageTk

# 画像ファイルのパス
image_path = "/mnt/imgs/nobiru.jpg"

def on_pixel_click(event):
    # クリックされたピクセルの座標を取得
    w, h = event.x, event.y
    target_w = max_size / max_width * w
    target_h = max_size / max_height * h
    # target_x = 
    print(f"Clicked at pixel coordinates: ({target_w}, {target_h}) {max_size}")

# 画像の読み込み
image = Image.open(image_path)

# 画像のリサイズ
max_width = 800  # 表示する画像の最大幅
max_height= 800  # 表示する画像の最大高さ

origin_width = image.width
origin_height = image.height
max_size = max(origin_width, origin_height)

image.thumbnail((max_width, max_height))

# 画像の表示サイズ
canvas_width = image.width
canvas_height = image.height

# ウィンドウの作成
window = Tk()
window.title("Image Viewer")

# キャンバスの作成
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# 画像の表示
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=image_tk)

# クリックイベントのバインディング
canvas.bind("<Button-1>", on_pixel_click)

# イベントループの開始
window.mainloop()