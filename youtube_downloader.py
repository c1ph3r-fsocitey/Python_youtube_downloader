from pytube import YouTube

link = input("enter the link: ")
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)
yd = yt.streams.get_highest_resolution()
print("downloading...")
yd.download('C:/Users/rahul/Downloads/yt downloads')
print("Downloaded")