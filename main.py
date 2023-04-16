import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import dataclasses
import pickle


sweets_dict = {
    'Caramel': 15,
    'Chocolate': 10,
    'Strawberry': 5,
    'Orange': 3
}

users = {}

def view_sweets():
    global my_label
    r = tk.Toplevel()
    r.title("Sweet Menu")


    my_img1 = ImageTk.PhotoImage(Image.open("/Users/emlynphoenix/Downloads/Images/random.jpeg"))
    my_img2 = ImageTk.PhotoImage(Image.open("/Users/emlynphoenix/Downloads/Images/cast.png"))
    my_img3= ImageTk.PhotoImage(Image.open("/Users/emlynphoenix/Downloads//Images/Casty.png"))

    image_list = [my_img1, my_img2, my_img3]

    status = tk.Label(r, text="Image 1 of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)


    my_label = tk.Label(r, image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)

    def forward(image_number):
        global my_label
        global button_forward
        global button_back
    
        my_label.grid_forget()
        my_label = tk.Label(r, image=image_list[image_number-1])
        button_forward = tk.Button(r, text=">>", command=lambda: forward(image_number+1))
        button_back = tk.Button(r, text="<<", command=lambda: back(image_number-1))
        
        if image_number == 3:
            button_forward = tk.Button(r, text=">>", state=tk.DISABLED)
        
        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = tk.Label(r, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)
        status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


    def back(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = tk.Label(r, image=image_list[image_number-1])
        button_forward = tk.Button(r, text=">>", command=lambda: forward(image_number+1))
        button_back = tk.Button(r, text="<<", command=lambda: back(image_number-1))

        if image_number == 1:
            button_back = tk.Button(r, text="<<", state=tk.DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = tk.Label(r, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=tk.SUNKEN, anchor=tk.E)
        status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)


    button_back = tk.Button(r, text="<<", command=back, state=tk.DISABLED)
    button_forward  = tk.Button(r, text=">>", command=lambda: forward(2))
    button_quit = tk.Button(r, text=f"Exit Program", command=r.quit)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2, pady=10)
    button_quit.grid(row=1, column=1)
    status.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E)

    


def choose_sweets():
    m = tk.Tk()
    m.title("Basket")

    sweet_label = tk.Label(m, text='Select a Sweet:')
    sweet_label.grid(row=0, column=1)

    sweets = tk.StringVar(m)
    sweets.set('Caramel')
    sweets_dropdown = tk.OptionMenu(m, sweets, *sweets_dict.keys())
    sweets_dropdown.grid(row=1, column=1)


    quantity_label = tk.Label(m, text='Enter Quantity: NOTE - must be in increments of 200g')
    quantity_label.grid(row=3, column=1)

    quantity_entry = tk.Entry(m)
    quantity_entry.grid(row=4, column=1)

    choice_more = tk.Button(m, text="Click to choose more than 1 type of sweet", command=choose_more)
    choice_more.grid(row=5, column=1)


def choose_more():
    choice = tk.Tk()
    choice.title("More Options")

    sweets = tk.StringVar(choice)
    sweets.set('Caramel')
    sweets_dropdown = tk.OptionMenu(choice, sweets, *sweets_dict.keys())
    sweets_dropdown.grid(row=1, column=1)


    more_label = tk.Label(choice, text='Enter Quantity: NOTE - must be in increments of 200g')
    more_label.grid(row=3, column=1)

    more_entry = tk.Entry(choice)
    more_entry.grid(row=4, column=1)

def user_sign_up():
    global username_entry
    global password_entry
    sign_up = tk.Tk()
    sign_up.title("Create a New Account")


    username_label = tk.Label(sign_up, text="Username:")
    username_label.pack()

    # Add an entry field for the username
    username_entry = tk.Entry(sign_up)
    username_entry.pack()

    # Add a label for the password field
    password_label = tk.Label(sign_up, text="Password:")
    password_label.pack()

    # Add an entry field for the password
    password_entry = tk.Entry(sign_up, show="*")
    password_entry.pack()

    submit_button = tk.Button(sign_up, text="Sign Up", command=save_info)
    submit_button.pack()

    if not username or not password:
        # Display an error message box if either field is empty
        tk.messagebox.showerror(title="Error", message="Please fill in both fields.")
    
    close_button = tk.Button(sign_up, text="Close", command=sign_up.destroy)
    close_button.pack()

    
def user_log_in():
    global result_label
    global username_entry2
    global password_entry2

    login_window = tk.Tk()
    login_window.title('Log In')

    # Create the username label and entry widget
    username_label = tk.Label(login_window, text='Username:')
    username_label.pack()
    username_entry2 = tk.Entry(login_window)
    username_entry2.pack()

    # Create the password label and entry widget
    password_label = tk.Label(login_window, text='Password:')
    password_label.pack()
    password_entry2 = tk.Entry(login_window, show='*')
    password_entry2.pack()

    # Create the log-in button
    login_button = tk.Button(login_window, text='Log In', command=fetch_data)
    login_button.pack()

    # Create the result label
    result_label = tk.Label(login_window, text='')
    result_label.pack()

def save_info():
    global username
    global password
    
    username = username_entry.get()
    password = password_entry.get()


    users[username] = password

    # Save the user_info dictionary to a file using pickle.dump
    with open('user_info.data', 'wb') as f:
        pickle.dump(users, f)

    # Clear the input fields
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

def fetch_data():
        # Get the username and password from the entry widgets
    username = username_entry2.get()
    password = password_entry2.get()
    
    # Load the dictionary from the file using pickle.load
    with open('user_info.data', 'rb') as f:
        users = pickle.load(f)
    
    # Check if the username and password are in the dictionary
    if username in users and users[username] == password:
        result_label.config(text='Log-in successful!')
    else:
        result_label.config(text='Incorrect Log-in Details')
    
    # Clear the entry widgets
    username_entry2.delete(0, tk.END)
    password_entry2.delete(0, tk.END)














