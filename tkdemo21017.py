from tkinter import *
from jieba.analyse import extract_tags
import threading
import time

class MyFrame(Frame):
    def __init__(self, master):
        # Frame(window)
        Frame.__init__(self, master)
        self.l1 = Label(self, text="來篇新聞吧")
        self.l1.pack()
        self.news = Text(self)
        self.news.pack()
        self.b1 = Button(self,
                         text="開始分析...",
                         command=self.analyse_thread)
        self.b1.pack()
        self.result = Label(self, text="按按鈕來分析")
        self.result.pack()

    def analyse_thread(self):
        t = threading.Thread(target=self.analyse)
        t.start()

    def analyse(self):
        self.b1["state"] = DISABLED
        time.sleep(5)
        news = self.news.get("1.0", "end")
        tags = extract_tags(news, 5)
        self.result["text"] = "/".join(list(tags))
        self.b1["state"] = ACTIVE

window = Tk()
window.geometry("500x500+250+250")
f1 = MyFrame(window)
f1.pack(expand=True, fill=BOTH,
        padx=20, pady=20)
mainloop()