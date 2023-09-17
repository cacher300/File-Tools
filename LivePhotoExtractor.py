import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to move files
def move_files():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_files = 0

    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            shutil.move(source_file, destination_file)
            moved_files += 1

    status_label.config(text=f"Successfully moved {moved_files} files.")

# Function to browse for source folder
def browse_source_folder():
    folder_path = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, folder_path)

# Function to browse for destination folder
def browse_destination_folder():
    folder_path = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, folder_path)

# Create the main window
window = tk.Tk()
window.title("Move JPEG/JPG/PNG Files")
window.geometry("400x200")

# Create and place widgets
source_label = tk.Label(window, text="Source Folder:")
source_label.pack()

source_folder_entry = tk.Entry(window, width=40)
source_folder_entry.pack()

source_browse_button = tk.Button(window, text="Browse", command=browse_source_folder)
source_browse_button.pack()

destination_label = tk.Label(window, text="Destination Folder:")
destination_label.pack()

destination_folder_entry = tk.Entry(window, width=40)
destination_folder_entry.pack()

destination_browse_button = tk.Button(window, text="Browse", command=browse_destination_folder)
destination_browse_button.pack()

move_button = tk.Button(window, text="Move Files", command=move_files)
move_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
