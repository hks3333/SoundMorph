import customtkinter as ctk
from tkinter.font import Font
import pyglet
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame
from CTkListbox import *
import time
from mutagen.mp3 import MP3
from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
from urllib.request import urlopen
import tkinter as tk

songs = []
org_song = []


def button_event():
    pass


def quitter(e):
    window.quit()
    window.destroy()


window = ctk.CTk()
window.title("SoundMorph")
ctk.set_default_color_theme("dark-blue")

y = 400
x = window.winfo_width()
window.geometry('1500x700')
window.resizable(False, False)
count = 0
menu = None
pygame.mixer.init()


def browseFiles():
    filename = ctk.filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("MP3 files", "*.mp3"),))

    if filename not in songs:
        songs.append(filename)
        org_song.append(filename)
    insert()

    # Change label contents


my_font = ctk.CTkFont(family="SF UI Display SemBd", size=12)
queue_font = ctk.CTkFont(family="SF Pro Display", size=26)
info_font = ctk.CTkFont(family="SF UI Display SemBd", size=20)
window.after(201, lambda: window.iconbitmap("./editor/soundmorph-logos.ico"))

bar = ctk.CTkFrame(master=window, width=1380, height=5, fg_color="#fc3c44", corner_radius=5)
bar.grid(row=0, column=0, ipady=1, ipadx=338)

#####################################
# SCREEN
screen = ctk.CTkFrame(window, height=457, width=1272, fg_color="#26282A")
screen.place(x=10, y=40)


#########################################
def about_us():
    #about = ctk.CTkLabel(screen, text="Hiyaa there !!\nthank you for choosing SoundMorph", text_color="#fc3c44",
                            #font=my_font)
    #about.place(x=400, y=200)
    #about.configure(font=("Gotham_Bold", 25))
    img = ctk.CTkImage(Image.open("./editor/Creative team-pana.png"), size=(420, 420))
    img_label=ctk.CTkLabel(screen,image=img,text="")
    img_label.place(x=340,y=-12)




def create_frame_file():
    global menu, count
    if count % 2 == 1:
        menu = ctk.CTkFrame(window, height=210, width=145, fg_color="#fc3c44")
        menu.place(x=5, y=35)
        open = ctk.CTkButton(menu, font=my_font, text="Open", text_color="black", hover_color="#f94c57",
                             fg_color="#fc3c44", anchor='w', corner_radius=0, command=browseFiles)
        open.pack(side=ctk.TOP, anchor=ctk.W)

        save = ctk.CTkButton(menu, font=my_font, text="Save", text_color="black", fg_color="#fc3c44",
                             hover_color="#f94c57", anchor='w', corner_radius=0)
        save.pack(side=ctk.TOP, anchor=ctk.W)

        save_as = ctk.CTkButton(menu, font=my_font, text="Save As", text_color="black", fg_color="#fc3c44",
                                hover_color="#f94c57", anchor='w', corner_radius=0)
        save_as.pack(side=ctk.TOP, anchor=ctk.W)
    else:
        destroy_frame()

    count += 1


def create_frame_edit():
    global menu, count
    if count % 2 == 1:
        menu = ctk.CTkFrame(window, height=210, width=145, fg_color="#fc3c44")
        menu.place(x=170, y=35)
        visual = ctk.CTkButton(menu, font=my_font, text="Visualiser", text_color="black", hover_color="#f94c57",
                               fg_color="#fc3c44", anchor='w', corner_radius=0)
        visual.pack(side=ctk.TOP, anchor=ctk.W)

        trim = ctk.CTkButton(menu, font=my_font, text="Trim", text_color="black", fg_color="#fc3c44",
                             hover_color="#f94c57", anchor='w', corner_radius=0)
        trim.pack(side=ctk.TOP, anchor=ctk.W)

        reverb = ctk.CTkButton(menu, font=my_font, text="Reverb", text_color="black", fg_color="#fc3c44",
                               hover_color="#f94c57", anchor='w', corner_radius=0)
        reverb.pack(side=ctk.TOP, anchor=ctk.W)
    else:
        destroy_frame()

    count += 1


def destroy_frame():
    global menu, count
    if menu:
        menu.destroy()
        menu = None

    count = 0


options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

file_button = ctk.CTkButton(master=bar, text="File", fg_color="#fc3c44", hover_color="#f94c57",
                            font=my_font, text_color="black", command=create_frame_file)
file_button.grid(row=0, column=0)

edit_button = ctk.CTkButton(master=bar, text="Edit", command=create_frame_edit, fg_color="#fc3c44",
                            hover_color="#f94c57",
                            font=my_font, text_color="black")
edit_button.grid(row=0, column=1, padx=30)

help_button = ctk.CTkButton(master=bar, text="Help", command=button_event, fg_color="#fc3c44", hover_color="#f94c57",
                            font=my_font, text_color="black")
help_button.grid(row=0, column=2, padx=30)

about_button = ctk.CTkButton(master=bar, text="About", command=about_us, fg_color="#fc3c44", hover_color="#f94c57",
                             font=my_font, text_color="black")
about_button.grid(row=0, column=3, padx=30)
print(x)
queue = ctk.CTkFrame(window, height=687, width=200)
qu_text = ctk.CTkLabel(queue, text="Playlist", font=queue_font, text_color="black", corner_radius=5, fg_color="#fc3c44",
                       width=200, height=10)
# qu_status = ctk.CTkListbox(queue,width=165)
# qu_status.place(x=5, y=50)
qu_text.place(x=0, y=0)
queue.place(x=1290, y=0)

SelectList = []
# user_image=ctk.CTkImage(Image.open('man.png'),size=(50,50))
# user_label=ctk.CTkLabel(window,image=user_image,text="",)
# user_label.place(x=10,y=40)
play_button_count = 0
listbox = CTkListbox(queue, width=170, font=my_font, hover_color="#f94c57", text_color="black", height=630, highlight_color="#f94c57", fg_color="#fc3c44", border_width=0, scrollbar_button_color="black", scrollbar_button_hover_color="white")
listbox.place(x=5, y=40)

pause_but = ctk.CTkImage(Image.open("./editor/pause_white.png"), size=(25, 30))
qu_label = ctk.CTkLabel(queue, text="Currently nothing in queue", font=my_font, text_color="black", bg_color="#fc3c44")
qu_label.place(x=25, y=160)

running = ""

song_length = 0

play = ""


def play_song():  # for loading song
    global play
    global running
    global play_button_count
    play = listbox.get()
    print(play_button_count)

    if play_button_count == 0 or running != play:

        print(play)
        play_button.configure(image=pause_but)
        running = play
        #load_image()

        pygame.mixer.music.load(running)
        pygame.mixer.music.play(start=int(slider.get()))

        play_time()
        play_button_count += 3

        print(running)

    elif play_button_count % 2 != 0:
        pause()

    else:
        unpause()


def slide(x):
    play = listbox.get()
    pygame.mixer.music.load(play)
    pygame.mixer.music.play(loops=0, start=int(slider.get()))


paused = False


def pause():
    global paused
    paused = True
    global play_button_count
    play_button.configure(image=play_button_img)
    pygame.mixer.music.pause()
    play_button_count += 1


def unpause():
    global paused
    global play_button_count
    play_button.configure(image=pause_but)
    pygame.mixer.music.unpause()
    play_button_count -= 1
    paused = False


def play_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_time = time.strftime('%M:%S', time.gmtime(current_time))
    current_running.configure(text=running[24:])
    song_mut = MP3(play)
    global song_length
    song_length = song_mut.info.length
    # slider_pos = int(song_length)

    # slider.set(current_time)
    # slider.configure(to=slider_pos)

    conv_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    current_time += 1

    if int(slider.get()) == int(song_length):
        status_bar.configure(text=converted_time)
    elif paused:
        pass

    elif int(slider.get()) == int(current_time):
        slider_pos = int(song_length)
        slider.configure(to=slider_pos)
        slider.set(int(current_time))
    else:
        slider_pos = int(song_length)
        slider.configure(to=slider_pos)
        slider.set(int(slider.get()))
        converted_time = time.strftime('%M:%S', time.gmtime(int(slider.get())))
        status_bar.configure(text=converted_time)
        next_time = int(slider.get() + 1)
        slider.set(next_time)

    total_time.configure(text=conv_song_length)
    status_bar.after(1000, play_time)


# Player
slider = ctk.CTkSlider(window, width=1000, progress_color="#fc3c44", button_color="#fc3c44",
                       button_hover_color="#f94c57", command=slide)
slider.set(0)
slider.place(x=70, y=510)
play_button_img = ctk.CTkImage(Image.open("./editor/play_white.png"), size=(25, 30))
play_button = ctk.CTkButton(window, image=play_button_img, text="", corner_radius=90, fg_color='transparent', width=70,
                            height=70, hover_color="#f94c57", command=play_song, border_color="#fc3c44", border_width=5)
play_button.place(x=500, y=540)
forward_button_img = ctk.CTkImage(Image.open("./editor/skipwhite.png"), size=(30, 30))
forward_button = ctk.CTkButton(window, image=forward_button_img, text="", corner_radius=30, fg_color='transparent',
                               width=50, height=40, hover_color="#f94c57")
forward_button.place(x=600, y=560)

backward_button_img = ctk.CTkImage(Image.open("./editor/back_white.png"), size=(30, 30))
backward_button = ctk.CTkButton(window, image=backward_button_img, text="", corner_radius=30, fg_color='transparent',
                                width=50, height=40, hover_color="#f94c57")
backward_button.place(x=420, y=560)
status_bar = ctk.CTkLabel(window, text="00:00", font=my_font)
status_bar.place(x=20, y=510)
total_time = ctk.CTkLabel(window, text="00:00", font=my_font)
total_time.place(x=1090, y=510)
current_running = ctk.CTkLabel(screen, text="", font=info_font, text_color="white")
current_running.place(x=10, y=420)


"""def load_image():
    url = "https://genius.com/search?q=weeknd"
    driver = webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    # print(soup)
    div = soup.find_all('div',
                        class_="user_avatar user_avatar--large clipped_background_image--background_fill clipped_background_image")
    img = div[0]
    img = str(img)
    print(img[194:len(img) - 1])
    link = ""
    for i in range(194, len(img)):
        if img[i] == '"':
            break
        else:
            link += img[i]
    print(link)

    u=urlopen(link)
    raw=u.read()
    u.close()
    img = ImageTk.PhotoImage(data=raw)
    artist_label = tk.Label(screen,image=img)
    artist_label.image=img
    artist_label.place(x=20, y=20)
    print(div)"""


def insert():
    global play_button_count
    j = 0
    for i in songs:
        listbox.insert(j, i)

        play_button_count = 0
        qu_label.destroy()
        j += 1
        print(play_button_count)


window.mainloop()
print(songs)
