from tkinter import *
from tkinter.filedialog import askopenfilename #Idk why I need these if I import all above but w/e
from tkinter import messagebox #Idk why I need these if I import all above but w/e
import subprocess

theme = ""

def select_file():
    global theme
    theme = askopenfilename()
    if(theme.endswith(".bin" or theme.endswith(".hex"))):
        select_label.config(text = theme)
        load_theme.config(state=NORMAL)
    else:
        load_theme.config(state=DISABLED)

def execute():
    messagebox.showinfo("Alert", "After you hit ok, press Fn + B for a couple seconds until it turns off")
    subprocess.run(["mdloader_windows.exe", "--first", "--download", theme, "--restart"])


window = Tk()
window.geometry("400x200")
    
window.configure(bg="#2a2a2e")
window.title("Theme Loader")

select_theme = Button(window, text="Select Theme", command = select_file)
select_theme.pack(ipady=4, pady=(10, 10))

select_label = Label(window, fg="white", bg="#2a2a2e")
select_label.pack(pady=(0, 50))

load_theme = Button(window, text="Change Theme", command = execute, state=DISABLED)
load_theme.pack(ipady=4)

window.mainloop()