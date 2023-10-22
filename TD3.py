#!/usr/bin/env python
# coding: utf-8

# # Exercise 1 
# Create a graphical interface that asks the user  to enter his name, first name and date of birth, 
# and display  “last name first name was born on date of birth” 

# In[82]:


import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title("User Information")
window.geometry("600x400+50+50") #setting the window size
window.config(bg="DarkSeaGreen1")

#funtion to get the information from user
def background_info():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    date_of_birth = date_of_birth_entry.get()
    result_label.config(text=f"{last_name} {first_name} was born on {date_of_birth}", bg="DarkSeaGreen1")


frame1 = tk.Frame(window)
frame1.pack()
# Create and pack labels and entry widgets
last_name_label = tk.Label(frame1, text="Last Name:", fg="PaleGreen4", bg="DarkSeaGreen1")
last_name_label.pack(side="left")
last_name_entry = tk.Entry(frame1)
last_name_entry.pack(side="left")

frame2 = tk.Frame(window)
frame2.pack()
first_name_label = tk.Label(frame2, text="First Name:", fg="PaleGreen4", bg="DarkSeaGreen1")
first_name_label.pack(side="left")
first_name_entry = tk.Entry(frame2)
first_name_entry.pack(side="left")

frame3 = tk.Frame(window)
frame3.pack()
date_of_birth_label = tk.Label(frame3, text="Date of Birth:", fg="PaleGreen4", bg="DarkSeaGreen1")
date_of_birth_label.pack(side="left")
date_of_birth_entry = tk.Entry(frame3)
date_of_birth_entry.pack(side="left")

# Create and pack a button to display the result
display_button = tk.Button(window, text="Show", fg="green", bg="cyan", command=background_info)
display_button.pack()

# Create and pack a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()


# # Exercise 2 
# Create a graphical interface that displays the current time after clicking on the button 'current 
# time'  

# In[213]:


from datetime import datetime
import tkinter as tk

#funtion for time setting in the particular format
def Time_Fun():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text="Current Time: " + current_time)
    
base = tk.Tk()
base.title("Time")
base.geometry("600x400+50+50")
base.config(bg="SlateGray1")
#label for the time
time_label = tk.Label(base, anchor="center", text="Click the button to show the current time.")
time_label.pack(side = "bottom",anchor="center")
#buttion to display the current time
time_button = tk.Button(base,anchor="center", text="Current Time", fg="green", command=Time_Fun)
time_button.pack(side = "bottom",anchor="center")

base.mainloop()


# # Exercise 3 
# Build with tkinter a window containing a canvas and four buttons: - the button " Draw a circle " : displays in the canvas a circle of thickness 2 pixels whose 
# coordinates (between 50 and 250) of the center and the radius (between 10 and 40) are random; - the button " Change color " should randomly change the color of the paths. The different 
# possible colors are defined in the list: ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black'] ; - the [Clear] button should clear all circles already drawn. It should reset the color of the next 
# trace to 'blue'.

# In[77]:


import tkinter as tk
import random 
window = tk.Tk()
window.title("Drawing Circle")

#Funtion to draw the random circle in the window
def draw_circle():
    center_x= random.randint(50, 250)
    center_y= random.randint(50, 250)
    radius= random.randint(10, 40)
    color= current_color.get()
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline=color, width=2)

#Funtion to change the circle colors
def color_change():
    color_list= ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black']
    color= random.choice(color_list)
    current_color.set(color)
    
#Funtion to clear out the canvas
def clear_canvas():
    canvas.delete("all")
    current_color.set("blue")

canvas = tk.Canvas(window, width=300, height=300, bg='white')
canvas.pack()
Draw_circle = tk.Button(window, anchor="sw", text="draw circle", fg="green", command=draw_circle)
Draw_circle.pack(anchor="sw")
Change_color = tk.Button(window,anchor="s", text="change color", fg="green", command=color_change)
Change_color.pack(anchor="s")
Clear_canvas = tk.Button(window,anchor="se", text="Clear Canvas", fg="green", command= clear_canvas)
Clear_canvas.pack(anchor="se")


# tracking the current color
current_color = tk.StringVar()
current_color.set('blue')

window.mainloop()


# # Exercise 4 
# We want to build the graphical window below: 
# To do this, we will use a combox widget which associates an input field with a list box: - the user of this widget can enter into the system either one of the items in the proposed list (by 
# clicking on its name) or an unlisted item (by entering a new name in the entry field.  - Our combo widget will therefore combine three basic tkinter widgets into one entity: an entry 
# field, a listbox and a scrollbar. The listbox and its scrollbar will be closely associated, since the 
# scrollbar allows you to scroll through the list in its box. It is important to ensure that the scrollbar 
# is always the same height as the box, regardless of the size of the box. - When the user chooses a color from the list (he can also enter a color name directly in the 
# input field), this color automatically becomes the background color for the master window.  - The master window contains a label and a button, to show you how you can access the 
# previously made selection in the ComboBox itself (the button causes the name of the last chosen 
# color to be displayed). 
# Create this interface with tkinter.

# In[83]:


import tkinter as tk

base = tk.Tk()
frame = tk.Frame(base)
#Listing out the colors
color = ["aliceblue",
         "antiquewhite",
         "aqua",
         "aquamarine1",
         "azure1",
         "banana",
         "bisque1",
         "bisque4",
         "blue",
         "blueviolet",
         "brown",
         "burlywood",
         "cadetblue",
         "cadetblue3",
         "carrot",
         "chartreuse",
         "chartreuse1",
         "chartreuse3",
         "chartreuse4",
         "chocolate"]

base.geometry("400x750")

global my_entry
my_entry = tk.Entry(frame)
my_entry.pack()

my_scrollbar = tk.Scrollbar(frame)
my_scrollbar.pack(side='right', fill='both') #setting the scrollbar position and alignment with the listbox

my_listbox = tk.Listbox(frame, height=10,
                        width=15,
                        bg="grey",
                        activestyle='dotbox',
                        font="Helvetica",
                        fg="yellow")

#loop to select different colors in the color list
for i, item in enumerate(color):
    my_listbox.insert(i + 1, item)

my_listbox.pack(side="left")

my_listbox.config(yscrollcommand=my_scrollbar.set)

# setting scrollbar command parameter
my_scrollbar.config(command=my_listbox.yview)

frame.pack()
frame1 = tk.Frame(base)

#Funtion to get the color
def set_entry_color():
    for i in my_listbox.curselection():
        my_entry.delete(0, "end")
        my_entry.insert(0, my_listbox.get(i))

#Funtion to apply the color chosen and displayed in the entry field
def apply_color():
    color_set = my_entry.get()
    base.config(bg=color_set)


select_button = tk.Button(frame1, text="select the color", command=set_entry_color)
select_button.pack(side="bottom")
test_button = tk.Button(frame1, text="Apply color", command=apply_color)
test_button.pack(side="bottom")
frame1.pack()

base.mainloop()


# # Exercise 5 
# a) Create a short program that will draw the 10 Olympic rings in a white rectangle. A "Quit" 
# button should close the window.

# In[84]:


import tkinter as tk
import random

window = tk.Tk()
window.title("Olympic Ring")

#Funtion to create a single circle
def draw_circle(x, y, color):
    canvas.create_oval(x, y, x + 100, y + 100, outline=color, width=4)

#Funtion to invoke the funtion for single circle and draw multiple circle in different position along with different colors
def draw_ring():
    canvas.create_rectangle(10, 10, 390, 290, outline="black", width=2)
    draw_circle(70, 90, "blue")
    draw_circle(170, 90, "black")
    draw_circle(270, 90, "red")
    draw_circle(120, 140, "yellow")
    draw_circle(220, 140, "green")


def window_quit():
    window.destroy()


canvas = tk.Canvas(window, width=400, height=400, bg='white')
canvas.pack()
Draw_circle = tk.Button(window, text="draw circle", command=draw_ring)
Draw_circle.pack()
Quit_window = tk.Button(window, text="Close", command=window_quit)
Quit_window.pack()

window.mainloop()


# # Exercise 5 
# b) Modify the above program by adding 5 buttons. Each of these buttons will cause each of the 5 rings to be drawn.

# In[85]:


import tkinter as tk


window = tk.Tk()
window.title("Olympic Ring")


#Funtion to create a single circle
def draw_circle(x, y, color):
    canvas.create_oval(x, y, x + 120, y + 120, outline=color, width=6)


#Funtion to invoke the funtion of single circle to draw different color circle
def draw_blue_ring():
    canvas.create_rectangle(10, 10, 400, 300, outline="black", width=4)
    draw_circle(70, 90, "blue")

#Funtion to invoke the funtion of single circle to draw different color circle
def draw_black_ring():
    draw_circle(170, 90, "black")

#Funtion to invoke the funtion of single circle to draw different color circle
def draw_red_ring():
    draw_circle(270, 90, "red")

#Funtion to invoke the funtion of single circle to draw different color circle
def draw_yellow_ring():
    draw_circle(120, 140, "yellow")

#Funtion to invoke the funtion of single circle to draw different color circle
def draw_green_ring():
    draw_circle(220, 140, "green")

#Funtion to invoke the funtion of single circle to draw different color circle
def window_quit():
    window.destroy()


canvas = tk.Canvas(window, width=500, height=450, bg='white')
canvas.pack()
#Button for drawing different color Circles
blue = tk.Button(window, text="draw blue circle", command=draw_blue_ring)
blue.pack()
black = tk.Button(window, text="draw black circle", command=draw_black_ring)
black.pack()
red = tk.Button(window, text="draw red circle", command=draw_red_ring)
red.pack()
yellow = tk.Button(window, text="draw yellow circle", command=draw_yellow_ring)
yellow.pack()
green = tk.Button(window, text="draw green circle", command=draw_green_ring)
green.pack()

Quit_window = tk.Button(window, text="Close", command=window_quit)
Quit_window.pack()

window.mainloop()


# # Exercise 6 
# Write a program that makes a window with a canvas appear. In this canvas, we will see two 
# circles (of different size and color), which are supposed to represent two stars. Buttons should 
# allow you to move both of them at will in any direction. Below the canvas, the program should 
# display permanently: 
# a) the distance between the two stars ; 
# b) the gravitational force they exert on each other (remember to display the masses chosen for 
# each of them at the top of the window, as well as the distance scale). 
# In this exercise, you will obviously use Newton's law of universal gravitation

# In[229]:


import math

# Gravitational constant 
G = 6.67430e-11

# Mass of stars
mass_star1 = 6.67e16 
mass_star2 = 5.05e16  

# Initial positions of stars
x1, y1 = 20, 20
x2, y2 = 50, 170

STAR1_RADIUS = 20
STAR2_RADIUS = 15

star1_speed = 10
star2_speed = 10

# Function to update the canvas with the current positions of stars
def update_canvas():
    canvas.delete("stars")
    canvas.create_oval(x1 - 10, y1 - 10, x1 + 10, y1 + 10, fill="yellow", tags="stars")
    canvas.create_oval(x2 - 15, y2 - 15, x2 + 15, y2 + 15, fill="red", tags="stars")

# Function to calculate the distance between stars
def calculate_distance():
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Function to calculate the gravitational force
def calculate_gravitational_force():
    distance = calculate_distance()
    force = (G * mass_star1 * mass_star2) / (distance ** 2)
    return force

# Function to update the labels with distance and gravitational force
def update_labels():
    distance = calculate_distance()
    force = calculate_gravitational_force()
    distance_label.config(text=f"Distance: {distance:.2f} meters")
    force_label.config(text=f"Gravitational Force: {force:.2e} N")

# Function for movement in right direction
def move_star(dx, dy, star):
    global x1, y1, x2, y2
    if star == 1:
        x1 += dx
        y1 += dy
    else:
        x2 += dx
        y2 += dy
    update_canvas()
    update_labels()
    
#function for movement in left direction
def move_star1(dx, dy, star):
    global x1, y1, x2, y2
    if star == 1:
        x1 -= dx
        y1 -= dy
    else:
        x2 -= dx
        y2 -= dy
    update_canvas()
    update_labels()

def move_star_up(dx, dy, star):
    global x1, y1, x2, y2
    if star == 1:
        y1 -= star1_speed
        move_star_up_down(x1, y1, star)
    else:
        y2 -= star2_speed
        move_star_up_down(x2, y2, star)
    update_canvas()
    update_labels()
        
def move_star_down(dx, dy, star):
    global x1, y1, x2, y2
    if star == 1:
        y1 += star1_speed
        move_star_up_down(x1, y1, star)
    else:
        y2 += star2_speed
        move_star_up_down(x2, y2, star)
    update_canvas()
    update_labels()
        
def move_star_up_down(dx, dy, star):
    canvas.coords(star, dx - STAR1_RADIUS, dy - STAR1_RADIUS, dx + STAR1_RADIUS, dy + STAR1_RADIUS)
    
root = tk.Tk()
root.title("Two Stars and Gravitational Force")

# Create and place widgets
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

update_canvas()

distance_label = tk.Label(root, text="Distance: 0.0 meters")
distance_label.pack()

force_label = tk.Label(root, text="Gravitational Force: 0.0 N")
force_label.pack()
#Create button for the left and right movement of the stars
move_star1_button = tk.Button(root, text="Star 1 right", command=lambda: move_star(10, 0, 1))
move_star1_button.pack(side="right")

move_star2_button = tk.Button(root, text="Star 2 right", command=lambda: move_star(10, 0, 2))
move_star2_button.pack(side="right")

move_star3_button = tk.Button(root, text="Star 1 left", command=lambda: move_star1(10, 0, 1))
move_star3_button.pack(side="left")

move_star4_button = tk.Button(root, text="Star 2 left", command=lambda: move_star1(10, 0, 2))
move_star4_button.pack(side="left")

move_star3_button = tk.Button(root, text="Star 1 up", command=lambda: move_star_up(10, 0, 1))
move_star3_button.pack(side="left")
move_star3_button = tk.Button(root, text="Star 2 up", command=lambda: move_star_up(10, 0, 2))
move_star3_button.pack(side="left")
move_star3_button = tk.Button(root, text="Star 1 down", command=lambda: move_star_down(10, 0, 1))
move_star3_button.pack(side="right")
move_star3_button = tk.Button(root, text="Star 2 down", command=lambda: move_star_down(10, 0, 2))
move_star3_button.pack(side="right")

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()


# # Exercise 7
# Program a simple calculator in python with tkinter. 
# This calculator will be able to perform the following operations: addition, subtraction, multiplication, division and square root. 
# Include a clear button 
# 

# In[211]:


from math import sqrt

# Function to get the input for button click
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")  # Clear the input
    elif text == "CE":
        current_expression = screen.get()
        if current_expression:
            current_expression = current_expression[:-1]
            screen.set(current_expression)  # remove the last entry
    elif text == "sqrt":
        try:
            num = float(screen.get())
            result = sqrt(num)
            screen.set(result)  # Calculating the squareroot and display it
        except:
            screen.set("Error")
    else:
        screen.set(screen.get() + text)  # Append the button's text to the input

root = tk.Tk()
root.geometry("400x500")
root.config(bg="lightcyan4")
root.title("Calculator")

# Variable to store the input on the display
screen = tk.StringVar()

# Create an entry widget for the display
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

# Define the text for the calculator buttons
button_texts = [
    "7", "8", "9", "CE", "C",
    "4", "5", "6", "/", "*",
    "1", "2", "3", "-", "+",
    "0", ".", "=", "sqrt"
]

row, col = 1, 0

# Creating buttons
for text in button_texts:
    button = tk.Button(frame, text=text, font="lucida 15 bold", padx=20, pady=20, fg="cyan")
    if text == "=":
        button.config(bg="lightgoldenrod1", fg="black")
    elif text == "CE":
        button.config(bg="lightsteelblue2", fg="black")
    elif text == "C":
        button.config(bg="orchid1", fg="black")
    elif text == "+":
        button.config(bg="seashell3", fg="black")

    else:
        button.config(bg="white")  
    button.grid(row=row, column=col, sticky="nsew")
    button.bind("<Button-1>", click)  
    col += 1
    if col > 4:
        col = 0
        row += 1

frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

button = tk.Button(frame, text="+", font="lucida 15 bold", padx=20, pady=50)
button.config(bg="cyan")
button.grid(row=3, column=4, rowspan=2, sticky="nsew")
button.bind("<Button-1>", click)
root.mainloop()


# In[ ]:




