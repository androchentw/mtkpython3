from tkinter import *

def bmi():
    global e1, e2, result
    height = float(e1.get())
    weight = float(e2.get())
    bmi = weight / (height / 100) ** 2
    result["text"] = "你的BMI是:" + str(bmi)

# Step1. 創造元件(父親元件)
# Step2. 元件.pack() 元件.grid()
window = Tk()
window.geometry("500x500+250+250")


f1 = Frame(window)
f1.pack()
l1 = Label(f1, text="請輸入你的身高:")
l1.pack()
e1 = Entry(f1)
e1.pack()
l2 = Label(f1, text="請輸入你的體重:")
l2.pack()
e2 = Entry(f1)
e2.pack()
b1 = Button(f1, text="計算BMI", command=bmi)
b1.pack()
result = Label(f1, text="點擊按鈕來計算")
result.pack()

mainloop()