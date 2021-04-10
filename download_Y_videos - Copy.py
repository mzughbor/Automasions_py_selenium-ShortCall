# try:
#
#     from pytube import YouTube
#     from pytube import Playlist
#
# except Exception as e :
#     print( " Some Modules are missing {}".format(e))
#
# url = "https://www.youtube.com/watch?v=9X4_Gfaasn8&feature=share&fbclid=IwAR1N2Hg-Fye1brBN1iIoFht5xvZkUJAY_QnQbfBRiR1n41HPa5qyO-KyNJs"
# ytd = YouTube(url).streams.first().download()
# print(ytd)
#

from tkinter import *
import pytube

#functions

def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        #video   = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        video   = youtube.streams.first() #get_highest_resolution().download()
        video.download("C:/Users/hp/Desktop/Videoes")
        notif.config(fg="green",text= "Downloaded")
        print(e)

        stream = video.streams.all()
        for i in stream:
            print(i)

    except Exception as e :
        notif.config(fg="red",text= "video could not be downloaded")


#Main Screen
master = Tk()
master.title("youtube video downloader...")


#Labels
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Please enter the link to your video below:", font=("Calibri", 10)).grid(sticky=N, pady=10, row=1)
notif = Label(master, font=("Calibri",12))
notif.grid(sticky=N, pady=1, row=4)
#Entry
url = StringVar()
Entry(master, width=45,textvar=url).grid(sticky=N,row=2)
Button(master,width=20, text="Download",font=("Calibri",12),command=download).grid(sticky=N, row=3, pady=15 )

master.mainloop()

