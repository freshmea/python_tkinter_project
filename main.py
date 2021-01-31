import tkinter

window=tkinter.Tk()

window.title("최수길-아스키코드 변환 프로그램")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="글자를 입력해주세요.문자를 아스키코드로 숫자로 바꾸어줍니다.")
label.config(font=("Courier", 10))
label.pack()

lable2=tkinter.Label(window, text="여기에 결과를 출력합니다.")
lable2.config(font=("Courier", 20))
lable2.pack()

def calc(event):
    aa = entry.get()
    bb=[]
    for i in aa:
        bb.append(ord(i))

    lable2.config(text="입력한 값은:  "+str(entry.get())+"\n결과는:  "+str(bb))
    entry.delete(0, "end")

entry=tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.config(font=("Courier", 20))
entry.pack()


window.mainloop()
