from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Music Player")
root.geometry("900x550")
root.configure(bg="#191414")  # Spotify Dark Background
root.resizable(False, False)

mixer.init()

# ---------------- Functions ---------------- #
def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        playlist.delete(0, END)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    song = playlist.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    music.config(text=song[0:-4])

def stop_song():
    mixer.music.stop()

def pause_song():
    mixer.music.pause()

def resume_song():
    mixer.music.unpause()

# ---------------- Images ---------------- #
logo_img = ImageTk.PhotoImage(Image.open("logo.png").resize((120, 120)))
play_img = ImageTk.PhotoImage(Image.open("play.png").resize((50, 50)))
stop_img = ImageTk.PhotoImage(Image.open("stop.png").resize((40, 40)))
resume_img = ImageTk.PhotoImage(Image.open("resume.png").resize((40, 40)))
pause_img = ImageTk.PhotoImage(Image.open("pause.png").resize((40, 40)))

# ---------------- Left Side ---------------- #
left_frame = Frame(root, bg="#191414")
left_frame.place(x=50, y=50, width=300, height=450)

Label(left_frame, image=logo_img, bg="#191414").pack(pady=10)

music = Label(left_frame, text="No song playing", font=("arial", 13), fg="#FFFFFF", bg="#191414")
music.pack(pady=10)

# Control Buttons
Button(left_frame, image=play_img, bg="#191414", bd=0, command=play_song).pack(pady=10)

btn_row = Frame(left_frame, bg="#191414")
btn_row.pack(pady=5)

Button(btn_row, image=stop_img, bg="#191414", bd=0, command=stop_song).pack(side=LEFT, padx=10)
Button(btn_row, image=resume_img, bg="#191414", bd=0, command=resume_song).pack(side=LEFT, padx=10)
Button(btn_row, image=pause_img, bg="#191414", bd=0, command=pause_song).pack(side=LEFT, padx=10)

# ---------------- Right Side ---------------- #
right_frame = Frame(root, bg="#191414")
right_frame.place(x=400, y=50, width=470, height=450)

Button(right_frame, text="Open Folder", font=("arial", 10, "bold"),
       bg="#1DB954", fg="black", command=open_folder).pack(pady=10)

music_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="#121212")
music_frame.pack(pady=10, fill=BOTH, expand=True)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, font=("arial", 10), bg="#121212", fg="#FFFFFF",
                   selectbackground="#1DB954", yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH, expand=True)

root.mainloop()
