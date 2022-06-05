import tkinter, tkinter.messagebox

root = tkinter.Tk()
#タイトル
root.title(u"てんぷら")
#サイズ
root.geometry('250x250')

#テキストボックス(カッコの中にレイアウトを書いたり(ここは横幅))
txtbox = tkinter.Entry(width=20)
#テキストボックスの設置場所
txtbox.place(x=60, y=70)
#ウィンドウ内に文字を設置する
lbl = tkinter.Label(text='ここ')
#文字の設置場所
lbl.place(x=30, y=70)

#ボタンを押したときの動作
def fac():
    a = txtbox.get()
    tkinter.messagebox.showinfo('結果', a)

#ボタンの設定・設置位置
calc_button = tkinter.Button(text='CLICK！',command=fac,width=16,height=3)
calc_button.place(x=60,y=130)

root.mainloop()
