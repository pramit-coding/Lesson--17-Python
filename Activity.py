from tkinter import *

window = Tk()

window.title("Activity 1")
window.geometry("500x500")

welcome = Label(text = "Hi this is the Tkinder Window", fg='orange',bg='blue')
button= Button(text="Click", bg='black',fg='blue')
entry = Entry(fg='yellow',bg='blue',width=50)
welcome.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=4)
frame.pack()
label=Label(master=frame, text='Frame')
label.pack()
textbox =Text(fg='blue',bg='orange')
textbox.pack()

window.mainloop()