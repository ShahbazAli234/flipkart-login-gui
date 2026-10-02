from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os


# ---------------- LOGIN FUNCTION ----------------

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'shahbazali234@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


# ---------------- MAIN WINDOW ----------------

root = Tk()

root.title('Login Form')
root.geometry('350x500')
root.configure(background='#0096DC')


# ---------------- IMAGE PATH ----------------

# Get the folder where this Python file is located
current_folder = os.path.dirname(os.path.abspath(__file__))

# Path of flipkart.jpg
image_path = os.path.join(current_folder, 'flipkart.jpg')


# ---------------- WINDOW ICON ----------------

icon_image = Image.open(image_path)
icon_image = icon_image.resize((32, 32))
icon = ImageTk.PhotoImage(icon_image)

root.iconphoto(True, icon)


# ---------------- FLIPKART LOGO ----------------

img = Image.open(image_path)
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(
    root,
    image=img,
    bg='#0096DC'
)

img_label.pack(pady=(10, 10))


# ---------------- TITLE ----------------

text_label = Label(
    root,
    text='Flipkart',
    fg='white',
    bg='#0096DC'
)

text_label.pack()

text_label.config(
    font=('Verdana', 24)
)


# ---------------- EMAIL LABEL ----------------

email_label = Label(
    root,
    text='Enter Email',
    fg='white',
    bg='#0096DC'
)

email_label.pack(pady=(20, 5))

email_label.config(
    font=('Verdana', 12)
)


# ---------------- EMAIL INPUT ----------------

email_input = Entry(
    root,
    width=50
)

email_input.pack(
    ipady=6,
    pady=(1, 15)
)


# ---------------- PASSWORD LABEL ----------------

password_label = Label(
    root,
    text='Enter Password',
    fg='white',
    bg='#0096DC'
)

password_label.pack(pady=(20, 5))

password_label.config(
    font=('Verdana', 12)
)


# ---------------- PASSWORD INPUT ----------------

password_input = Entry(
    root,
    width=50,
    show='*'
)

password_input.pack(
    ipady=6,
    pady=(1, 15)
)


# ---------------- LOGIN BUTTON ----------------

login_btn = Button(
    root,
    text='Login Here',
    bg='white',
    fg='black',
    width=20,
    height=2,
    command=handle_login
)

login_btn.pack(
    pady=(10, 20)
)

login_btn.config(
    font=('Verdana', 10)
)


# ---------------- RUN APPLICATION ----------------

root.mainloop()
