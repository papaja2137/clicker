import tkinter as tk

root = tk.Tk() #TWORZENIE OKNA

root.title("Bomb Clicker")
root.geometry("800x600")
root.iconbitmap("piggy-bank.ico")
root.resizable(False, False)

bomb = 100
score = 0
pres_return = True

label = tk.Label(root, text="Press [enter] to start the game", font=("Comic Sans MS", 22))
label.pack()

fuse_label = tk.Label(root, text=f"Timer: {str(bomb)}", font=("Comic Sans MS", 15))
fuse_label.pack()

score_label = tk.Label(root, text=f"Score: {str(bomb)}", font=("Comic Sans MS", 15))
score_label.pack()

img_1 = tk.PhotoImage(file="img_1.png").subsample(2, 2)
img_2 = tk.PhotoImage(file="img_2.png").subsample(2, 2)
img_3 = tk.PhotoImage(file="img_3.png").subsample(2, 2)
img_4 = tk.PhotoImage(file="img_4.png").subsample(2, 2)

bomb_label = tk.Label(image = img_1)
bomb_label.pack()

def update_display():
    pass

def is_alive():
    pass

def update_bomb():
    pass

def update_score():
    pass

def start():
    pass

def click(event):
    global press_return
    if not press_return:
        pass
    else:
        update_bomb()
        update_score()
        update_display()
        label.config(text="")
        press_return = False
    

click_button = tk.Button(root, text="Click me", bg="black", fg="cyan", font=("Comic sans MS", 20), width=23, command=click)
click_button.pack()

root.mainloop()