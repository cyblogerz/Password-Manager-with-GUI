from tkinter import*
import random
import string
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

def generate():
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(website,email,password):
    if website == '' or password =='':
        messagebox.showwarning("oops","Can't leave website and password empty")
    else:
        dtext = f'{website}|{email}|{password}\n'
        data = open('data.txt','a')
        data.write(dtext)
        data.close()
        site_entry.delete(0,END)
        pass_entry.delete(0,END)

        
   
# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.config(padx=20,pady=20)
root.title("Password Manager")

#logo
canvas = Canvas(width=200 , height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column = 1 , row=0)

#site label
site_label = Label(text = "Website:")
site_label.grid(column = 0, row=1)
#site entry
site_entry = Entry(width=35)
site_entry.focus()
site_entry.grid(row=1, column=1,columnspan=2 ,sticky="EW")

#email label
mail_label = Label(text="Email/Username:")
mail_label.grid(row=2,column =0)

#email entry
mail_entry = Entry(width=35)
mail_entry.insert(0, 'pranavajay2002@gmail.com')
mail_entry.grid(row=2,column=1,columnspan=2,sticky="EW")

#pass label
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#password entry
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3,sticky="EW")

#generate password button
generate_button = Button(text="Generate Password",command=generate)
generate_button.grid(column=2,row=3,sticky="EW")

#add button
add_button = Button(text="Add",width=35,command=lambda:save(site_entry.get(),mail_entry.get(),pass_entry.get()))
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")

root.mainloop()