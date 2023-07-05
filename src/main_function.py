import tkinter as tk
import random
import os

# Function to get a list of image paths from a directory
def get_image_paths(directory):
    if directory[-1] != '/':
        directory += '/'
    files = os.listdir(directory)
    image_paths = []
    for file in files:
        if '.png' in file:
            image_paths.append(directory + file)
    # shuffle the list into a random order
    random.shuffle(image_paths)
    return image_paths

# Function to load and display the current image
def load_image():
    current_image_path = image_paths[image_index]
    image = tk.PhotoImage(file=current_image_path)
    label_image.config(image=image)
    label_image.image = image

# Function to check the user's answer
def check_answer():
    user_answer = entry.get().strip()
    current_image_name = image_paths[image_index].split("/")[-1]
    corresponding_name = corresponding_names[current_image_name]

    if user_answer.lower() == corresponding_name.lower():
        label_feedback.config(text="Correct!")
        # Move to the next image
        next_image()
    else:
        label_feedback.config(text="Wrong. Try again.")

    # Clear the entry field
    entry.delete(0, tk.END)

# Function to move to the next image
def next_image():
    global image_index
    image_index = (image_index + 1) % len(image_paths)
    load_image()

# Function to handle the 'Enter' key press event
def handle_enter(event):
    check_answer()

# manually choose names corresponding to images
corresponding_names = {
    'solsleutel_lage_fa.png': 'fa',
    'solsleutel_lage_mi.png': 'mi',
}

# Create the main window
window = tk.Tk()
window.title("Note reading practice")

# Get a list of image paths from a directory
image_paths = get_image_paths("./img")

# Variable to keep track of the current image index
image_index = 0

# Create and display the image label
label_image = tk.Label(window)
label_image.pack() # This geometry manager organizes widgets in blocks before placing them in the parent widget.

# Create and display the feedback label
label_feedback = tk.Label(window, text="")
label_feedback.pack()

# Create and display the text entry field
entry = tk.Entry(window)
entry.pack()

# Bind the 'Enter' key press event to the handle_enter() function
entry.bind("<Return>", handle_enter)

# Create and display the submit button
button_submit = tk.Button(window, text="Submit", command=check_answer)
button_submit.pack()

# Load and display the first image
load_image()

# Start the main event loop
window.mainloop()
