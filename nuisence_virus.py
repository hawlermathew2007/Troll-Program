from tkinter import *
from tkinter import messagebox
import pyautogui
import random

screen_w, screen_h = pyautogui.size()

def virus():
	i = 0
	window.destroy()
	while i < 1000:
		x = random.randint(0, screen_w)
		y = random.randint(0, screen_h)
		pyautogui.moveTo(x,y)
		i += 1

window = Tk()

button = Button(window, text= "click me", command= virus)
button.pack()

window.mainloop()
	
# import qrcode

# img = qrcode.make("https://scontent.fsgn2-6.fna.fbcdn.net/v/t1.15752-9/339400582_949366809581735_8355925515051834832_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=ae9488&_nc_ohc=U7eWc8ShI1sAX-v5NwG&_nc_ht=scontent.fsgn2-6.fna&oh=03_AdQR-sMtqynzee0syy6Uh7AIaLn5opGgG-8kLTW3VsOOMQ&oe=6453A95A")
# img.save("lmao.png")
# img.show()