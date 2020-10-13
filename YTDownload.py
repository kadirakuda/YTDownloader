#get link from user
#convert the video to mp4 audio
#download the mp4
import re
from pytube import YouTube
from pytube import Playlist

def download_audio(video_link):
    #filter the available streams to audio only
    yt = YouTube(video_link)
    yt.streams.filter(only_audio=True).first().download('/Users/kudakadira/Music/')
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

#download an audio youtube playlist
def download_playlist(video_link):
    pl = Playlist(video_link)
    pl._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print("This playlist contains ",len(pl.video_urls), " songs.")

    # physically downloading the audio track
    for video in pl.videos:
        audioStream = video.streams.get_by_itag(140).download()

    print("Your download is done.")


while True:
    print("\n")
    print("Welcome to YT Downloader \n")
    print("Selecter an option below: ")
    format = input("Enter 'V' for video, 'A' for audio only download, 'P - Playlist' or 'X' to exit: \n")
    if format.lower() == "v":
        #User link to download youtube video
        video_link = input("enter link: ")
        quality = input("Enter a letter to choose video quality 'M - medium', 'H - High' or 'L - low':")
        download_video(video_link, quality.lower())

    elif format.lower() == "a":
        #User link to download youtube video
        video_link = input("enter link: ")
        download_audio(video_link)

    elif format.lower() == "p":
        video_link = input("enter playlist link: ")
        download_playlist(video_link)

    elif format.lower() == "x":
        break
