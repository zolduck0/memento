import os.path
import sys
import tkinter as tk
from PIL import Image, ImageTk
from datetime import date, timedelta, datetime
import pytz

# assets location
def getAssetPath(rel_path):
    if getattr(sys,'frozen', False):
        basePath = sys._MEIPASS
    else:
        basePath = os.path.dirname(__file__)
    return os.path.join(basePath,rel_path)

# window
root = tk.Tk()
root.title("memento")
root.geometry("600x400")
root.resizable(False,False)

iconPath = getAssetPath("assets/icon.png")

icon = ImageTk.PhotoImage(file=iconPath)
root.tk.call('wm','iconphoto',root._w,icon)

welcomeFont = ("Arial", 20)
font = ("Arial Narrow", 20)
daysLeftFont = ("Arial",35)

# welcome
welcomeLabel = tk.Label(root,text="Welcome",font=welcomeFont)
welcomeLabel.grid(row=0,column=1,padx = 45,pady=70)

# logo
logo = Image.open(getAssetPath("assets/logos.png"))
# logo = logo.resize((175,47),Image.Resampling.LANCZOS)

logoTk = ImageTk.PhotoImage(logo)

logoLabel = tk.Label(root,image=logoTk)
logoLabel.place(relx=0, rely= 0.0, anchor="nw")

#time
time = datetime.now()
timeFormat = time.strftime("%H:%M:%S")

def timeUpdate():
    time = datetime.now()
    timeFormat = time.strftime("%H:%M:%S")
    timeLabel.config(text=timeFormat)
    root.after(1000,timeUpdate)

timeLabel = tk.Label(root,font=font)
timeLabel.place(relx=1,rely=0.0,anchor="ne")

#today date
todayDate = date.today()
todayDateFormat = todayDate.strftime("%d %B %Y")

todayDateLabel = tk.Label(root,text=todayDateFormat,font=font)
todayDateLabel.grid(row=1,column=0,padx=10)

#arrow
arrow = Image.open(getAssetPath("assets/arrow.png"))
arrowTk = ImageTk.PhotoImage(arrow)

arrowLabel = tk.Label(root,image=arrowTk)
arrowLabel.grid(row=1,column=1)

#desired date
year = date.today().year
desiredDate = date(year,12,25)

desiredDateFormat = desiredDate.strftime("%d %B %Y")

desiredDateLabel = tk.Label(root,text=desiredDateFormat,font=font)
desiredDateLabel.grid(row=1,column=2)

#days left
daysLeft = desiredDate - todayDate
daysLeftString = " days left."
daysLeftLabel = tk.Label(root,text=str(daysLeft.days) + daysLeftString,font=daysLeftFont,anchor="w")
daysLeftLabel.grid(row=2,column=0,columnspan=3,sticky="w",padx=155,pady=80)

root.after_idle(timeUpdate)
root.mainloop()