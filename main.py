from pytube import YouTube
import os

# get input until user types exit or quit
while True:
    # video url
    url = input("Enter the link to the youtube video, or quit/exit to close the program:\n")
    if url.lower() == "exit" or url.lower() == "quit":
        break

    # get mp4/mp3 from user, keeps asking until they enter mp3 or mp4
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
        # order by resolution and get mp4 videos with both video and audio components
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.get_audio_only()
    
    path = os.getcwd() + "\\Downloads"
    file = video.download(output_path = path)
    if not mp4:
        name, ext = os.path.splitext(file)
        newFileName = name + ".mp3"
        os.rename(file, newFileName)
    print("Download successful, downloaded to + " + path + "\n")
        

