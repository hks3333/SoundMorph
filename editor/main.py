import customtkinter as ctk
from tkinter.font import Font
import pyglet
from tkinter import filedialog
from PIL import Image
import pygame
from CTkListbox import *

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


my_font = ctk.CTkFont(family="Gotham-Medium", size=12)
queue_font = ctk.CTkFont(family="Gotham-Medium", size=26)
window.after(201,
             lambda: window.iconbitmap("soundmorph-logos.ico"))

bar = ctk.CTkFrame(master=window, width=1400, height=5, fg_color="#E79215", corner_radius=5)
bar.grid(row=0, column=0, ipady=1, ipadx=338)

#####################################
# SCREEN
screen = ctk.CTkFrame(window, height=457, width=1272)
screen.place(x=10, y=40)


#########################################
def about_us():
    about = ctk.CTkLabel(screen, text="Hiyaa there !!\nthank you for choosing SoundMorph", text_color="#E79215",
                         font=my_font)
    about.place(x=400, y=200)
    about.configure(font=("Gotham_Bold", 25))


def create_frame_file():
    global menu, count
    if count % 2 == 1:
        menu = ctk.CTkFrame(window, height=210, width=145, fg_color="#E79215")
        menu.place(x=5, y=35)
        open = ctk.CTkButton(menu, font=my_font, text="Open", text_color="black", hover_color="#DAA520",
                             fg_color="#E79215", anchor='w', corner_radius=0, command=browseFiles)
        open.pack(side=ctk.TOP, anchor=ctk.W)

        save = ctk.CTkButton(menu, font=my_font, text="Save", text_color="black", fg_color="#E79215",
                             hover_color="#DAA520", anchor='w', corner_radius=0)
        save.pack(side=ctk.TOP, anchor=ctk.W)

        save_as = ctk.CTkButton(menu, font=my_font, text="Save As", text_color="black", fg_color="#E79215",
                                hover_color="#DAA520", anchor='w', corner_radius=0)
        save_as.pack(side=ctk.TOP, anchor=ctk.W)
    else:
        destroy_frame()

    count += 1


def create_frame_edit():
    global menu, count
    if count % 2 == 1:
        menu = ctk.CTkFrame(window, height=210, width=145, fg_color="#E79215")
        menu.place(x=170, y=35)
        visual = ctk.CTkButton(menu, font=my_font, text="Visualiser", text_color="black", hover_color="#DAA520",
                               fg_color="#E79215", anchor='w', corner_radius=0)
        visual.pack(side=ctk.TOP, anchor=ctk.W)

        trim = ctk.CTkButton(menu, font=my_font, text="Trim", text_color="black", fg_color="#E79215",
                             hover_color="#DAA520", anchor='w', corner_radius=0)
        trim.pack(side=ctk.TOP, anchor=ctk.W)

        reverb = ctk.CTkButton(menu, font=my_font, text="Reverb", text_color="black", fg_color="#E79215",
                               hover_color="#DAA520", anchor='w', corner_radius=0)
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

file_button = ctk.CTkButton(master=bar, text="File", fg_color="#E79215", hover_color="#DAA520",
                            font=my_font, text_color="black", command=create_frame_file)
file_button.grid(row=0, column=0)

edit_button = ctk.CTkButton(master=bar, text="Edit", command=create_frame_edit, fg_color="#E79215",
                            hover_color="#DAA520",
                            font=my_font, text_color="black")
edit_button.grid(row=0, column=1, padx=30)

help_button = ctk.CTkButton(master=bar, text="Help", command=button_event, fg_color="#E79215", hover_color="#DAA520",
                            font=my_font, text_color="black")
help_button.grid(row=0, column=2, padx=30)

about_button = ctk.CTkButton(master=bar, text="About", command=about_us, fg_color="#E79215", hover_color="#DAA520",
                             font=my_font, text_color="black")
about_button.grid(row=0, column=3, padx=30)
print(x)
queue = ctk.CTkFrame(window, height=687, width=200)
qu_text = ctk.CTkLabel(queue, text="Queue", font=queue_font, text_color="black", corner_radius=5, fg_color="#E79215",
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
listbox=CTkListbox(queue,width=160,font=my_font,hover_color="#FFAA33",text_color="black",height=630,highlight_color="#FFAA33",fg_color="#E79215",border_color="black",scrollbar_button_color="black",scrollbar_button_hover_color="grey")
listbox.place(x=5, y=40)

pause_but = ctk.CTkImage(Image.open("pause.png"), size=(50, 50))
qu_label=ctk.CTkLabel(queue,text="Currently nothing in queue",font=my_font,text_color="black",bg_color="#E79215")
qu_label.place(x=15,y=160)


def play_song():#for loading song

    global play_button_count
    if play_button_count==0:
        play=listbox.get()
        print(play)
        play_button.configure(image=pause_but)
        pygame.mixer.music.load(play)
        pygame.mixer.music.play()
        play_button_count += 1
        print(play_button_count)
    elif play_button_count%2!=0:
        pause()

    else :
        unpause()

def pause():
    global play_button_count
    play_button.configure(image=play_button_img)
    pygame.mixer.music.pause()
    play_button_count+=1
def unpause():
    global play_button_count
    play_button.configure(image=pause_but)
    pygame.mixer.music.unpause()
    play_button_count-=1






# Player
slider = ctk.CTkSlider(window, width=1000, progress_color="#E79215", button_color="#E79215",
                       button_hover_color="#DAA520")
slider.place(x=50, y=600)
play_button_img = ctk.CTkImage(Image.open("play.png"), size=(50, 50))
play_button = ctk.CTkButton(window, image=play_button_img, text="", corner_radius=30, fg_color='#E79215', width=50,
                            height=40, hover_color="#DAA520",command=play_song)
play_button.place(x=500, y=510)
forward_button_img = ctk.CTkImage(Image.open("fast-forward.png"), size=(30, 30))
forward_button = ctk.CTkButton(window, image=forward_button_img, text="", corner_radius=30, fg_color='#E79215',
                               width=50, height=40, hover_color="#DAA520")
forward_button.place(x=600, y=520)

backward_button_img = ctk.CTkImage(Image.open("fast-forward (1).png"), size=(30, 30))
backward_button = ctk.CTkButton(window, image=backward_button_img, text="", corner_radius=30, fg_color='#E79215',
                                width=50, height=40, hover_color="#DAA520")
backward_button.place(x=420, y=520)
load_img=play_button_img
load_img.configure(size=(5,5))

def insert():

    global play_button_count
    j=0
    for i in songs:
        listbox.insert(j,i)
        j+=1
        play_button_count=0
        qu_label.destroy()
        load = ctk.CTkButton(queue,image=load_img,text="",width=5)
        load.place(y=43,x=0)


window.mainloop()
print(songs)
