#get link from user
#convert the video to mp4 audio
#download the mp4

from pytube import YouTube

def download_audio(video_link):
    #filter the available streams to audio only
    yt = YouTube(video_link)
    yt.streams.filter(only_audio=True).first().download()
    print("\n Your audio file is ready!")

def download_video(video_link, quality):
    yt = YouTube(video_link)
    if quality == 'h':
        #selects the first stream which is always the hightest quality stream
        yt.streams.first().download()
        print("\n Your video file is ready!")
    elif quality == 'l':
        #use filter to select a low resolution as per the user request
        yt.streams.filter(res="240p").first().download() #
        print("\n Your video file is ready!")
    elif quality == 'm':
        #use filter to select a medium resolution as per the user request
        yt.streams.filter(res="360p").first().download()


while True:
    print("\n")
    print("Welcome to YT Downloader \n")
    print("Selecter an option below: ")
    format = input("Enter 'V' for video, 'A' for audio only download or 'X' to exit: \n")
    if format.lower() == "v":
        #User link to download youtube video
        video_link = input("enter link: ")
        quality = input("Enter a letter to choose video quality 'M - medium', 'H - High' or 'L - low':")
        download_video(video_link, quality.lower())

    elif format.lower() == "a":
        #User link to download youtube video
        video_link = input("enter link: ")
        download_audio(video_link)
    elif format.lower() == "x":
        break
