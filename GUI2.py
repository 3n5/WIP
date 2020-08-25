
import tkinter as tk
#まずは対話型の環境で窓を一つ作ってみましょう：

root = tk.Tk()                # 窓を作る
root.title("Tkinterの練習")   # 窓のタイトルを設定
root.geometry("640x480")      # 窓の大きさを設定
#この中にラベル（テキスト）を書き込んでみます：

label = tk.Label(root, text="テスト")  # ラベルを作成
label.pack()                           # 実際に表示する
#ボタンも作ってみます：

button = tk.Button()                        # ボタンを作成
button["text"] = "クリック！"         # ボタンにラベルを設定
button["command"] = lambda: print("ほげ！") # ボタンの動作を設定
button.pack()                               # 実際に表示する
#ここで lambda: は無名関数を作るための命令です。もっと複雑なコマンドをボタンに設定するには，関数を定義し，その関数名を button["command"] に代入します。

#対話型環境では，このように部品を一つずつ追加して確認できますが，一つのスクリプトにすると，すぐに終了してしまいます。そこで，プログラムの最後に

root.mainloop()  # ループ（対話型環境では不要）