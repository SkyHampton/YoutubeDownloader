from pytube import YouTube
from validators import url as validateURL
import os


# get input until user types exit or quit
while True:
    # video url
    url = input("Enter the link to the youtube video, or quit/exit to close the program:\n")
    if url.lower() == "exit" or url.lower() == "quit":
        break
    
    urlValid = validateURL(url)
    # ask if user wants an mp3 or an mp4 file
    while True:
        format = input("Enter mp4 or mp3 for the download format:\n").lower()
        if format == "mp4":
            mp4 = True
            break
        elif format == "mp3":
            mp4 = False
            break
        else:
            print("Incorrect format type.")

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
    print("Download successful, downloaded to + " + path + "\n")
        

