import tkinter as tk
import random
import glob

# Function to get a list of image paths from a directory
def get_image_paths(directory):
    image_paths = glob.glob(directory + "/*.png")  # Change the extension if your images have a different format
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
    current_image_name = image_paths[image_index].split("/")[-1].split(".")[0]

    if user_answer.lower() == current_image_name.lower():
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

# Create the main window
window = tk.Tk()
window.title("Image Guessing Game")

# Get a list of image paths from a directory
image_paths = get_image_paths("../img")  # Replace with the actual directory path

# Variable to keep track of the current image index
image_index = 0

# Create and display the image label
label_image = tk.Label(window)
label_image.pack()

# Create and display the feedback label
label_feedback = tk.Label(window, text="")
label_feedback.pack()

# Create and display the text entry field
entry = tk.Entry(window)
entry.pack()

# Create and display the submit button
button_submit = tk.Button(window, text="Submit", command=check_answer)
button_submit.pack()

# Load and display the first image
load_image()

# Start the main event loop
window.mainloop()
