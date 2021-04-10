try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e :
    print( " Some Modules are missing {}".format(e))

#url = "https://www.youtube.com/watch?v=U0fk5L1ifbo"
url = "https://www.youtube.com/watch?v=kXo-6y21UG4"

ytd = YouTube(url)
for x in ytd.streams.filter( file_extension = "mp4" ).order_by('resolution').desc():# if y want specific res = "720p" ...
    print(x)

#print('Number of views: ',ytd.views)
#print("Description: ",ytd.description)
#print("Ratings: ",ytd.rating)


ytd.streams[7].download("D:\img")

#print(ytd)





#
# #Main Screen
# master = Tk()
# master.title("youtube video downloader...")
#
#
# #Labels
# Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
# Label(master, text="Please enter the link to your video below:", font=("Calibri", 10)).grid(sticky=N, pady=10, row=1)
# notif = Label(master, font=("Calibri",12))
# notif.grid(sticky=N, pady=1, row=4)
# #Entry
# url = StringVar()
# Entry(master, width=45,textvar=url).grid(sticky=N,row=2)
# Button(master,width=20, text="Download",font=("Calibri",12),command=download).grid(sticky=N, row=3, pady=15 )
#
# master.mainloop()
#
