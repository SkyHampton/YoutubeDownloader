from pytube import YouTube

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

