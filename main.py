from tkinter import *
from generator import Generator
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- ACCOUNT FINDER ------------------------------- #
def search_account():
    try:
        with open("data_file.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="You have no accounts saved at the moment!", icon="error")
    else:
        try:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]['email']}\n\nPassword: {data[website_entry.get()]['password']}")
        except KeyError:
            messagebox.showinfo(title=website_entry.get(), message=f"You have no account saved for this site", icon="error")
            

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = Generator().final_password
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please make sure all fields are completed!")
    else:
        try:
            with open("data_file.json", "r") as data_file:
                # Read data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data_file.json", "w") as data_file:
                # Save new data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data_file.json", "w") as data_file:
                # Save new data
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ENTRIES

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_entry = Entry(width=50)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(END, "silviu13bak@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3,column=1)

# BUTTONS

generate_butt = Button(text="Generate Password", command= generate_password)
generate_butt.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search_account)
search_button.grid(column=2, row=1)

window.mainloop()