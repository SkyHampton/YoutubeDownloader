# made by Sky Hampton

from statistics import quantiles
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from matplotlib.pyplot import text
from pytube import YouTube
from validators import url as validateURL
import os

def getVideo(url, mp4):
    # get youtube video
    yt = YouTube(url)
    
    if mp4:
        # get highest resolution mp4 video
        video = yt.streams.get_highest_resolution()
    else:
        # get highest bitrate audio-only stream as an mp4
        video = yt.streams.get_audio_only()
    
    # get current working directory and append \Downloads folder
    path = os.getcwd() + "\\Downloads"
    # create \Downloads folder if it does not exsits and download video to that folder
    file = video.download(output_path = path)
    # if a mp3 was requested, the file is changed to mp3 format
    if not mp4:
        name, ext = os.path.splitext(file)
        newFileName = name + ".mp3"
        os.rename(file, newFileName)
    showinfo(title="Downloaded", message="Download successful, downloaded to " + path + "\n")

gui = Tk()
gui.wm_title("Youtube Downloader")

main = ttk.Frame(gui, padding = "20 20 20 20")
main.grid(column=0, row=0, sticky=(N,W,E,S))

instructions = ttk.Label(main, text="Enter the youtube video URL into the text box and select from the available file types.").grid(row=1, column=1)
urlVariable = StringVar()
ytUrlField = ttk.Entry(main, width = 24, textvariable=urlVariable).grid(row = 2, column= 1)
mp4 = BooleanVar()
r1 = ttk.Radiobutton(main, text="mp4", value=True, variable=mp4).grid(row=3, column=1)
r2 = ttk.Radiobutton(main, text="mp3", value=False, variable=mp4).grid(row=4, column=1)

confirm = ttk.Button(main, text="Download", command=lambda:getVideo(urlVariable.get(), mp4.get())).grid(row=5, column=1)

for child in main.winfo_children():
        child.grid_configure(padx=5, pady=5)

gui.mainloop()