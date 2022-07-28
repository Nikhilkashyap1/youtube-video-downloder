import tkinter as tk
from pytube import YouTube

def Download_Video():
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    tk.Label(window, text = 'Your Video is downloaded!/n thank you', font = 'arial 15',fg="White",bg="#F3A49B").place(x= 10 , y = 140)
window = tk.Tk()
window.geometry("400*700")
window.config(bg="#F3A49B")
window.resizable(width=False, height=False)
window.title('YouTube Video Downloaders')

link = tk.StringVar()

tk.Label(window, text='                   Youtube Video Downloader                    ', font='arial 20 bold',
         fg="#97483F", bg="#F9D1CC").pack()
tk.Label(window, text='Paste Your YouTube Link Here:', font='arial 20 bold', fg="Black", bg="#F7C5BF").place(x=5, y=60)

link_enter = tk.Entry(window, width=53, textvariable=link, font='arial 15 bold', bg="orange").place(x=5, y=100)

tk.Button(window, text='DOWNLOAD VIDEO', font='arial 15 bold', fg="white", bg='lightblue', padx=2,
          command=Download_Video).place(x=385, y=140)
window.mainloop()