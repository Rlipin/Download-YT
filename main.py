import pytube 
pytube.request.default_range_size = 1048576    # this is for chunck size, 1MB size
from pytube import YouTube
from tkinter import *
from tkinter import filedialog, messagebox, ttk




## criando janela

app = Tk()
app.title('Download Vídeo')
app.geometry("400x160")

progress_bar = DoubleVar()
progress_bar.set(0)
pb = ttk.Progressbar(app, variable=progress_bar,maximum=100)
pb.place(x=10,y=130,width=320,height=20)



def interface():

    # PARTE DE CIMA

    Label(app, text="Insira a URL do video que deseja fazer o donwload", bg="#fff", fg="#000",anchor=W).place(x=10, y=10, width=345,height=20)
    Label(app, text='URL:   ', bg="#fff", fg="#000", anchor=W).place(x=10, y=40, width=40,height=20)
    v_link = Entry(app,textvariable=video_URL, bg="#fff", fg="#000")
    v_link.place(x=50,y=40,width=310,height=20)

    # PARTE DE BAIXO

    Label(app, text='Destiny:   ', bg="#fff", fg="#000", anchor=W).place(x=10, y=70, width=65,height=20)
    v_directory = Entry(app,textvariable=browser_directory)
    v_directory.place(x=70,y=70,width=220,height=20)
    Button(app,text='Browser',command=browser).place(x=290,y=70,width=70,height=20)
    Button(app,text='Download',command=download).place(x=150,y=100,width=75,height=20)

def browser():

    path_distiny = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    browser_directory.set(path_distiny)

def download():

    download_folder = browser_directory.get()
    video = YouTube(video_URL.get())
    video.register_on_progress_callback(progress_callback)
    video.register_on_complete_callback(complete_callback)
    video.streams.get_by_resolution("720p").download(download_folder)

def progress_callback(video,chunk, bytes_remaining):
    size = video.filesize
    progress = int(((size - bytes_remaining)/size)*100)
    progress_bar.set(progress)
    app.update()

def complete_callback(video, file_handle):
    print("Download finished")
    Label(app,text="100%").place(x=350,y=130,width=35,height=20)

 
video_URL = StringVar()
browser_directory = StringVar()
    

interface()

app.mainloop()