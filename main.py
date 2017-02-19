import tkinter
import ctypes
import os
import sys
import threading
import keyboard
import pyperclip

def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)


def handle_paste():
    text = pyperclip.paste()
    newtext = text.replace('\r\n','')
    pyperclip.copy(newtext)

root = tkinter.Tk()

root.title("PDF Paste")
width, height = 300, 300
root.geometry('%dx%d+%d+%d' % (width,height,(root.winfo_screenwidth() - width ) / 2,\
                                            (root.winfo_screenheight() - height) / 2))
root.maxsize(300,300)
root.iconbitmap("icon.ico")

label1 = tkinter.Label(root, text="在 PDF 中复制文本后 \n\n 点击按钮或以下快捷键对文本进行处理\nCtrl + Alt + Z\n\n 最后 Ctrl + V 粘帖", justify="center")
label1.pack()

img = tkinter.PhotoImage(file=resource_path('image.gif'))

button = tkinter.Button(root, text='click', image=img, command=handle_paste)
button.pack()

root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)



keyboard.add_hotkey('ctrl+alt+z', handle_paste)
thread = threading.Thread(target=keyboard.wait)
thread.setDaemon(True)
thread.start()

root.mainloop()



