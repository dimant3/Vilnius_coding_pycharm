from pytube import YouTube
from sys import argv
    # from the module sys, import the function or parameter argv
    # the sys module contains all kinds of system-related functions and constants.

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)      # prints YT video title

print("View: ", yt.views)       # prints YT video views count

yd = yt.streams.get_highest_resolution()        # downloads highest quality of video. You can choose any quality

yd.download("C:/Users/manty/OneDrive/Desktop/yt_downloads")

# videos are found and showing title and views but
# download not working, something wrong with pytube recent version


