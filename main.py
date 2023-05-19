from tkinter import *
from tkinter import messagebox
from passgen import password_generator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_maker():
    gen_pass = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(END, gen_pass)
    pyperclip.copy(gen_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email_userid = email_entry.get()
    gen_pass = password_entry.get()
    new_data = {
        website_name:{
            'email': email_userid,
            'password': gen_pass,
        }
    }

    if len(website_name) == 0 or len(gen_pass) == 0:
        messagebox.showerror("password or website fields can not be empty")
    else:
        is_ok = messagebox.askyesno("are you sure?")
        if is_ok:
            # with open('data.json', mode='w') as output:
            #     json.dump(new_data, output, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            try:
                with open('data1.json', mode='r') as data_file:
                    pass
            except FileNotFoundError:
                with open('data1.json', mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open('data1.json', mode='r') as data_file:
                    json_data = json.load(data_file)
                    print(json_data)
                    json_data.update(new_data)
                    print(json_data)
                with open('data1.json', mode='w') as data_file :
                    json.dump(json_data, data_file, indent=4)
                    print(type(json_data))
                    print(json_data)


def search_pass():
    website = website_entry.get()

    try:
        data_file = open('data1.json', mode='r')
    except FileNotFoundError:
        messagebox.showerror(title='DataFileError', message='No DataFile found')
        data_file.close()
    else:
        data = json.load(data_file)
        data_file.close()
        try:
            site_data = data[website]
        except KeyError:
            messagebox.showerror(title='Invalid Website', message='Website information are not available in the data '
                                                                  'file.')
        else:
            password = site_data['password']
            email = site_data['email']
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(END, email)
            password_entry.insert(END, password)


def delete_website():
    website = website_entry.get()
    try:
        data_file = open('data1.json', mode='r')
    except FileNotFoundError:
        messagebox.showerror(title='Data File Error', message='No File found')
        data_file.close()
    else:
        data = json.load(data_file)
        data_file.close()
    data.pop(website)
    with open('data1.json', mode='w') as data_file:
        json.dump(data, data_file, indent=4)
    messagebox.showinf#
    o(title='Delete', message='item is deleted')




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PasswordManager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'hojjat.mahdavian@gmail.com')

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

pass_gen_button = Button(text='Generate Password', width=14, command=password_maker)
pass_gen_button.grid(row=3, column=3)

add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', width=14, command=search_pass)
search_button.grid(row=1, column=3)

delete_button = Button(text='Delete', width=14, command=delete_website)
delete_button.grid(row=2, column=3)












window.mainloop()