import customtkinter as ctk
from tkinter.font import Font
import pyglet
from tkinter import filedialog


def button_event():
    pass


def quitter(e):
    window.quit()
    window.destroy()


window = ctk.CTk()
window.title("SoundMorph")

y = 400
x = window.winfo_width()
window.geometry('1500x700')
window.resizable(False, False)
count = 0
menu = None


def move_app(event):
    window.geometry(f"+{event.x_root - offset_x}+{event.y_root - offset_y}")


def browseFiles():
    filename = ctk.filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents


my_font = ctk.CTkFont(family="Gotham-Medium", size=12)
queue_font = ctk.CTkFont(family="Gotham-Medium", size=26)
window.after(201,
             lambda: window.iconbitmap("soundmorph-logos.ico"))

bar = ctk.CTkFrame(master=window, width=1400, height=5, fg_color="#E79215", corner_radius=5)
bar.grid(row=0, column=0, ipady=1,ipadx=338)

#####################################
#SCREEN
screen=ctk.CTkFrame(window,height=457,width=1272)
screen.place(x=10,y=40)
#########################################
def about_us():
    about=ctk.CTkLabel(screen,text="Hiyaa there !!\nthank you for choosing SoundMorph",text_color="#E79215",font=my_font)
    about.place(x=400,y=200)
    about.configure(font=("Gotham_Bold",25))

def create_frame_file():
    global menu,count
    if count % 2 == 1  :
        menu = ctk.CTkFrame(window, height=210, width=145,fg_color="#E79215")
        menu.place(x=5, y=35)
        open=ctk.CTkButton(menu,font=my_font,text="Open",text_color="black",hover_color="#DAA520",fg_color="#E79215",anchor='w',corner_radius=0,command=browseFiles)
        open.pack(side=ctk.TOP,anchor=ctk.W)

        save = ctk.CTkButton(menu, font=my_font, text="Save", text_color="black",fg_color="#E79215",
                             hover_color="#DAA520",anchor='w',corner_radius=0)
        save.pack(side=ctk.TOP,anchor=ctk.W)

        save_as = ctk.CTkButton(menu, font=my_font, text="Save As", text_color="black",fg_color="#E79215",
                             hover_color="#DAA520",anchor='w',corner_radius=0)
        save_as.pack(side=ctk.TOP,anchor=ctk.W)
    else:
        destroy_frame()

    count += 1

def create_frame_edit():
    global menu,count
    if count % 2 == 1  :
        menu = ctk.CTkFrame(window, height=210, width=145,fg_color="#E79215")
        menu.place(x=170, y=35)
        visual=ctk.CTkButton(menu,font=my_font,text="Visualiser",text_color="black",hover_color="#DAA520",fg_color="#E79215",anchor='w',corner_radius=0)
        visual.pack(side=ctk.TOP,anchor=ctk.W)

        trim = ctk.CTkButton(menu, font=my_font, text="Trim", text_color="black",fg_color="#E79215",
                             hover_color="#DAA520",anchor='w',corner_radius=0)
        trim.pack(side=ctk.TOP,anchor=ctk.W)

        reverb = ctk.CTkButton(menu, font=my_font, text="Reverb", text_color="black",fg_color="#E79215",
                             hover_color="#DAA520",anchor='w',corner_radius=0)
        reverb.pack(side=ctk.TOP,anchor=ctk.W)
    else:
        destroy_frame()

    count += 1



def destroy_frame():
    global menu,count
    if menu:
        menu.destroy()
        menu=None

    count = 0




options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

file_button = ctk.CTkButton(master=bar, text="File", fg_color="#E79215", hover_color="#DAA520",
                            font=my_font, text_color="black", command=create_frame_file)
file_button.grid(row=0, column=0)

edit_button = ctk.CTkButton(master=bar, text="Edit", command=create_frame_edit, fg_color="#E79215", hover_color="#DAA520",
                            font=my_font, text_color="black")
edit_button.grid(row=0, column=1, padx=30)

help_button = ctk.CTkButton(master=bar, text="Help", command=button_event, fg_color="#E79215", hover_color="#DAA520",
                            font=my_font, text_color="black")
help_button.grid(row=0, column=2, padx=30)

about_button = ctk.CTkButton(master=bar, text="About", command=about_us, fg_color="#E79215", hover_color="#DAA520",
                             font=my_font, text_color="black")
about_button.grid(row=0, column=3, padx=30)
print(x)
queue=ctk.CTkFrame(window,height=687,width=200)
qu_text=ctk.CTkLabel(queue,text="Queue",font=queue_font,text_color="black",corner_radius=5,fg_color="#E79215",width=200,height=10)
qu_status=ctk.CTkLabel(queue,text="Currently,nothing in the\n queue",font=my_font,text_color="#E79215")
qu_status.place(x=36,y=240)
qu_text.place(x=0,y=0)
queue.place(x=1290,y=0)



window.mainloop()
