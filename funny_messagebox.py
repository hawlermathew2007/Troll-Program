from tkinter import *
from tkinter import messagebox

def devi():		#will update this to many nuisense
	window.destroy()
	while True:
		messagebox.showwarning(title="HAHAHAHAHAHA", message= "YOU GET A VIRUS!")

def fun():

	window.destroy()

	name = input("Enter your name: ")

	if name == "":
		while True:
			messagebox.showinfo(title= "Bruh...", message= "There is no way that you have no name")
			messagebox.showwarning(title= "Retry please!", message= "Enter your name again my dude")
			name = input("Enter your name: ")
			if name != "":
				break

	messagebox.showinfo(title="WOW", message=name + "! " + "What a cool name!")

	run = True
	while run:
		if messagebox.askyesno(title="So...", message= "Wanna continue?"):
			run = False

	run = True
	text = "nothing"
	times = 0
	while run:
		while times < 10:
			if not messagebox.askyesno(title="Hmmm...", message= "Do you have a lover?", icon= 'warning'):
				times = 10
				text = "good job"
			else:
				times += 1

		if times >= 10:
			if text == "good job":
				run = False
			else:
				messagebox.showwarning(title="Fuck you", message="Shut the fuck up and click no")
				times = 0

	messagebox.showwarning(title= "Damn", message= "Wow, me too!")

	messagebox.showwarning(title= "Confession", message= f"Hey, {name}! I love you :<!")


	run = True
	text = "nothing"
	times = 0
	while run:
		while times < 5:
			if messagebox.askyesno(title="Muah muah", message= "Do you love me :<?", icon= 'warning'):
				times = 5
				text = "good job"
			else:
				times += 1

		if times >= 5:
			if text == "good job":
				run = False
			else:
				messagebox.showerror(title="SOBS!", message="Fuck you, I dont give a fuck")
				messagebox.showwarning(title="IM ANGRY", message="CLICK THE FUCKING YES BUTTON MDF")
				times = 0

	messagebox.showinfo(title= "Awwwwww", message= "Ehe :33")
	messagebox.showwarning(title= ":<", message= "Im so happy :<!")
	messagebox.showwarning(title= "Love luv", message="I will love you forever :<!")

	times = 0
	while times < 10:
		messagebox.showwarning(title= "Cium", message= "Muah! MUAH!")
		times += 1

window = Tk()
window.title("Funny Messagebox")
window.geometry("280x40")

frame = Frame(window)
frame.pack()

button1 = Button(frame, text="click me!", command= fun)
button1.pack(side=LEFT)

label = Label(frame, text=" or ")
label.pack(side=LEFT)

button2 = Button(frame, text="click me?", command= devi)
button2.pack(side=LEFT)

window.mainloop()