import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to split files into subfolders
def split_files(input_folder, output_folder, files_per_subfolder=10):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize variables
    subfolder_count = 0
    file_count = 0

    # Loop through files in the input folder
    for filename in os.listdir(input_folder):
        source_file = os.path.join(input_folder, filename)

        # Create a new subfolder if the current subfolder is full
        if file_count == 0:
            current_subfolder = os.path.join(output_folder, f"subfolder_{subfolder_count}")
            os.makedirs(current_subfolder, exist_ok=True)

        destination_file = os.path.join(current_subfolder, filename)

        # Move the file to the current subfolder
        shutil.move(source_file, destination_file)
        file_count += 1

        # Check if the subfolder is full
        if file_count == files_per_subfolder:
            subfolder_count += 1
            file_count = 0

# Function to browse for input folder
def browse_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_path)

# Function to browse for output folder
def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

# Function to split files when the "Split Files" button is clicked
def split_files_button():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    files_per_subfolder = int(files_per_subfolder_var.get())  # Get the selected value
    split_files(input_folder, output_folder, files_per_subfolder)
    status_label.config(text="Files split into subfolders successfully.")

# Create the main window
window = tk.Tk()
window.title("File Splitter")
window.geometry("400x250")  # Slightly taller window

# Create and place widgets
input_label = tk.Label(window, text="Input Folder:")
input_label.pack()

input_folder_entry = tk.Entry(window, width=40)
input_folder_entry.pack()

input_browse_button = tk.Button(window, text="Browse", command=browse_input_folder)
input_browse_button.pack()

output_label = tk.Label(window, text="Output Folder:")
output_label.pack()

output_folder_entry = tk.Entry(window, width=40)
output_folder_entry.pack()

output_browse_button = tk.Button(window, text="Browse", command=browse_output_folder)
output_browse_button.pack()

files_per_subfolder_label = tk.Label(window, text="Files Per Subfolder:")
files_per_subfolder_label.pack()

# Create a Spinbox for selecting the number of files per subfolder
files_per_subfolder_var = tk.StringVar()
files_per_subfolder_var.set("10")  # Default value
files_per_subfolder_spinbox = tk.Spinbox(window, from_=1, to=100, textvariable=files_per_subfolder_var)
files_per_subfolder_spinbox.pack()

split_button = tk.Button(window, text="Split Files", command=split_files_button)
split_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
