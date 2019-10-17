from tkinter import *
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class MyFrame(Frame):
    def __init__(self, master, engine):
        Frame.__init__(self, master)
        self.l1 = Label(self, text="輸入學生姓名")
        self.l1.pack()
        self.e1 = Entry(self)
        self.e1.pack()
        self.b1 = Button(self, text="查詢", command=self.query)
        self.b1.pack()
        self.result = Label(self, text="按上面按鈕查詢")
        self.result.pack()
        self.engine = engine
        # session: 連線, 保持連線所有改動
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def query(self):
        self.result["text"] = "TEST"

# engine
fn = "data.sqlite"
dn = os.path.dirname(__file__)
# engine: process
engine = create_engine("sqlite:///" + os.path.join(dn, fn),
                        echo=True)

window = Tk()
f1 = MyFrame(window, engine)
f1.pack(padx=20, pady=20)
mainloop()
