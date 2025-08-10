
import tkinter as tk
win = tk.Tk()
y = 0


def sayHi():
    global y
    y += 1
    print(y)


win.geometry("200*100")
b =tk.Button(
    win,
    text='Suprise me',
    command=sayHi
)
b.pack()
win.mainloop()