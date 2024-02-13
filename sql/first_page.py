import customtkinter as ctk
from CTkMessagebox import CTkMessagebox as messagebox
import sqlite3
from main import *

connection = sqlite3.connect('./sql/soundmorph.db')
cursor = connection.cursor()


def show_users():
    query = "SELECT * FROM login_details;"
    cursor.execute(query)

    details = []
    for row in cursor.fetchall():
        details.append(row)
    return details


def register_check(username):
    users = show_users()
    for user in users:
        if user[1] == username:
            return False
    return True


def login_check(username, password):
    users = show_users()
    for user in users:
        if user[1] == username and user[2] == password:
            return True
    return False


def add_user(username, password, usermail):
    users = show_users()
    userid = 10001 + len(users)
    print(userid, username, password, usermail)
    query = "INSERT INTO login_details (user_id, username, password, email) VALUES (?, ?, ?, ?);"
    cursor.execute(query, (userid, username, password, usermail))
    connection.commit()
    print("User added")


def show_login_page():
    register_frame.pack_forget()
    login_frame.pack()


def show_register_page():
    login_frame.pack_forget()
    register_frame.pack()


def login():
    entered_username = login_username_entry.get()
    entered_password = login_password_entry.get()

    if login_check(entered_username, entered_password) and entered_username != "" and entered_password != "":
        msg = messagebox(title="Login Successful",
                         message=f"Welcome, {entered_username}", icon="check", option_focus="Continue")
        response = msg.get()
        if response == "Continue":
            root.destroy()
            exec(open("./editor/main.py").read())

    elif entered_username == "" or entered_password == "":
        messagebox(title="Login Failed", message="Please enter both username and password",
                   icon="question", options=["Retry", "Cancel"])
    else:
        messagebox(title="Login Failed", icon="cancel",
                   message="Username does not exist or password is wrong", option_1="Retry", option_2="Cancel")


def register():
    entered_username = register_username_entry.get()
    entered_password = register_password_entry.get()
    entered_usermail = register_usermail_entry.get()

    if register_check(entered_username) and entered_username != "" and entered_password != "" and entered_usermail != "":
        if add_user(entered_username, entered_password, entered_usermail):
            messagebox(title="Registration Successful",
                       message=f"Account created for {entered_username}", icon="check", option_focus="Continue")
            show_login_page()
        else:
            messagebox(title="Registration Failed", message="Account creation failed",
                       icon="cancel", option_focus="Try Again")
    elif entered_username == "" or entered_password == "" or entered_usermail == "":
        messagebox(title="Registration Failed", message="Please enter all fields",
                   icon="warning", option_focus="Continue")
    else:
        messagebox(title="Registration Failed", message="Username already exists",
                   icon="cancel", option_focus="Continue")


root = ctk.CTk()
root.title("SoundMorph")
root.geometry('500x500')
root.resizable(False, False)
ctk.set_default_color_theme("dark-blue")

my_font = ctk.CTkFont(family="SF UI Display SemBd", size=12)

screen = ctk.CTkFrame(root, height=500, width=500, background_corner_colors=["#E79215", "#E79215", "#E79215", "#E79215"], fg_color="#fc3c44", corner_radius=5)
screen.place(x=0, y=0)

login_frame = ctk.CTkFrame(root, height=250, width=150, fg_color="#fc3c44", corner_radius=5)
register_frame = ctk.CTkFrame(root, height=250, width=150, fg_color="#fc3c44", corner_radius=5)

login_username_label = ctk.CTkLabel(login_frame, text="Username:", text_color="black", font=my_font, fg_color="#E79215")
login_username_label.pack(pady=10)
login_username_entry = ctk.CTkEntry(login_frame)
login_username_entry.pack(pady=20)

login_password_label = ctk.CTkLabel(login_frame, text="Password:", text_color="black", font=my_font, fg_color="#E79215")
login_password_label.pack(pady=10)
login_password_entry = ctk.CTkEntry(login_frame, show="*")
login_password_entry.pack(pady=10)

login_button = ctk.CTkButton(login_frame, text="Login", command=login, fg_color="#E79215", hover_color="#DAA520", font=my_font, text_color="black")
login_button.pack(pady=10)

register_button = ctk.CTkButton(login_frame, text="Register", command=show_register_page, text_color="black", font=my_font, fg_color="#E79215")
register_button.pack(pady=20)

register_username_label = ctk.CTkLabel(register_frame, text="Username:", text_color="black", font=my_font, fg_color="#E79215")
register_username_label.pack(pady=10)
register_username_entry = ctk.CTkEntry(register_frame)
register_username_entry.pack(pady=10)

register_password_label = ctk.CTkLabel(register_frame, text="Password:", text_color="black", font=my_font, fg_color="#E79215")
register_password_label.pack(pady=10)
register_password_entry = ctk.CTkEntry(register_frame, show="*")
register_password_entry.pack(pady=10)

register_usermail_label = ctk.CTkLabel(register_frame, text="Mail:", text_color="black", font=my_font, fg_color="#E79215")
register_usermail_label.pack(pady=10)
register_usermail_entry = ctk.CTkEntry(register_frame, show="*")
register_usermail_entry.pack(pady=10)

register_button = ctk.CTkButton(register_frame, text="Register", command=register, fg_color="#E79215", hover_color="#DAA520", font=my_font, text_color="black")
register_button.pack(pady=10)

back_button = ctk.CTkButton(register_frame, text="Back to Login", command=show_login_page, text_color="black", font=my_font, fg_color="#E79215")
back_button.pack(pady=20)

show_login_page()

root.mainloop()
