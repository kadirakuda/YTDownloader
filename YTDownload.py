#get link from user
#convert the video to mp4 audio
#download the mp4

from pytube import YouTube

def download_audio(video_link):
    #filter the available streams to audio only
    yt = YouTube(video_link)
    yt.streams.filter(only_audio=True).first().download()
    print("\n Your audio file is ready!")

def download_video(video_link):
    #filter the available streams to audio only
    yt = get_ytlink()
    yt.streams.first().download()
    print("\n Your video file is ready!")

while True:
    print("\n")
    print("Welcome to YT Downloader \n")
    print("Selecter an option below: ")
    format = input("Enter 'V' for video, 'A' for audio only download or 'X' to exit: \n")
    format.lower()
    if format == "v":
        #User link to download youtube video
        video_link = input("enter link: ")
        download_video(video_link)
    elif format == "a":
        #User link to download youtube video
        video_link = input("enter link: ")
        download_audio(video_link)
    elif format == "x":
        break
