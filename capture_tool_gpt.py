import datetime
from PIL import ImageGrab
import easygui
import os

def capture_screen():
    # 現在の画面をキャプチャ
    image = ImageGrab.grab()
    # ファイル名を年月日時分秒の形式で生成
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S.png")
    title = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # 画像をPNGフォーマットで保存
    image.save(filename)
    return filename, title

def ask_for_title():
    # ユーザーに画像のタイトルを入力させる
    title = easygui.enterbox("Enter the title for the image:")
    return title

def append_to_markdown(filename, title):
    # Markdownファイルにリンクを追記
    with open("manual.md", "a") as file:
        file.write(f"![{title}]({filename})\n")

def main():
    # 画面をキャプチャしてファイルに保存
    filename, title = capture_screen()
    # 画像タイトルをユーザーに尋ねる
    # title = ask_for_title()
    # マークダウンファイルにリンクを追記
    append_to_markdown(filename, title)
    print("The image and its markdown link have been saved.")
    # スクリプトの最後に追加
    # input("Press enter to continue...")

if __name__ == "__main__":
    main()
