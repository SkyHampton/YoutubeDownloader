from pytube import YouTube
import os

while True:
    url = input("Enter the link to the youtube video, or quit/exit to close the program:\n")
    if url.lower() == "exit" or url.lower() == "quit":
        break
    
    while True:
        format = input("Enter mp4 or mp3 for the download format:\n").lower()
        if format == "mp4":
            mp4 = True
            break
        elif format == "mp3":
            mp3 = True
            break
        else:
            print("Incorrect format type.")


    yt = YouTube(url)
    
    if mp4:
        ordered = yt.streams.order_by('resolution')
        filtered = ordered.filter(progressive=True, file_extension="mp4")
    else:
        filtered = ordered.filter(only_audio=True)
    
    sorted = filtered.desc()
    first = sorted.first()
    path = os.getcwd() + "\\Downloads"
    file = first.download(output_path = path)
    if not mp4:
        name, ext = os.path.splitext(file)
        newFileName = name + ".mp3"
        os.rename(file, newFileName)
    print("Download successful, downloaded to + " + path + "\n")
        

