import random
import gui

password = ""
hint_list = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def reset_func():
    global password
    password = ""
    gui.generated_psw.config(text=password)

def copy_func():
    gui.root.clipboard_clear()
    gui.root.clipboard_append(password)

def hint_func():
    global hint_list
    hint_string = gui.hint_entry.get()
    for i in hint_string:
        if i.isalpha() == False:
            hint_string = hint_string.replace(i, "")
    hint_list = list(hint_string)
    print(hint_list)

def generate_func():
    global password
    print("Generating...")
    c = 0
    while c < random.randint(6, 15):
        # Add numbers
        password += str(random.choice(num_list))
        gui.generated_psw.config(text=password)
        
        hint_func()

        # Add letters
        password += random.choice(hint_list)
        gui.generated_psw.config(text=password)
        c += 1
    print("Generated!")
