import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import locale
import subprocess
import sys
import threading  # Import threading module

# List of required packages
required_packages = ['gtts', 'PIL', 'requests']

for package in required_packages:
    try:
        # Try to import the package
        __import__(package)
    except ImportError:
        # If the package is not installed, install it
        print(f"{package} is not installed. Installing now...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check if gtts-cli is installed
try:
    subprocess.check_output(['gtts-cli', '--version'])
except subprocess.CalledProcessError:
    print("gtts-cli is not installed. Installing now...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gTTS'])

# Global variable to track whether audio is paused
is_paused = False

# Detect system language
system_lang = locale.getlocale()[0]
if system_lang and system_lang.startswith('es'):
    lang = 'es'
    read_text = "🔊 Leer texto seleccionado"
    pause_text = "⏸️ Pausar/Reanudar"
    stop_text = "⏹️ Detener lectura"
else:
    lang = 'en'
    read_text = "🔊 Read Selected Text"
    pause_text = "⏸️ Pause/Resume"
    stop_text = "⏹️ Stop Reading"

def read_selected_text():
    global is_paused
    selected_text = os.popen("xsel").read().strip()
    if selected_text:
        # Use gtts-cli to convert text to speech and play it with mpg321
        subprocess.run(f'echo "{selected_text}" | gtts-cli --nocheck -l {lang} - | mpg321 -', shell=True)

def play_audio():
    os.system("mpg321 selected_text.mp3")

def stop_reading():
    os.system("pkill mpg321")  # Stop the audio playback

def toggle_pause():
    global is_paused
    if is_paused:
        os.system("pkill -CONT mpg321")  # Resume playback
        is_paused = False
    else:
        os.system("pkill -STOP mpg321")  # Pause playback
        is_paused = True

def on_closing():
    stop_reading()
    root.destroy()

# Create the tkinter window
root = tk.Tk()
root.title("Parrot Reader")
root.configure(bg='#333333')
root.geometry('400x400')  # Set the window size to a 500x500 square

# Load and display the logo
logo_url = "https://community.parrotsec.org/uploads/default/optimized/2X/4/48effee36b2b86615e4f4e4f865b61cbb0388a3f_2_460x333.png"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))
logo_image = logo_image.resize((100, 100))  # Resize the logo
logo_image = logo_image.convert("RGBA")  # Convert the image to RGBA

# Create a new image with the same size as the logo and white background
mask = Image.new('L', (100, 100), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 100, 100), fill=255)  # Draw a white circle

# Apply the mask to the logo
logo_image.putalpha(mask)

logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(side=tk.TOP, padx=10, pady=10)

# Display the title
style = ttk.Style()
style.configure("Title.TLabel", background="#333333", foreground="white", font=("Helvetica", 24))

title = ttk.Label(root, text="Parrot Reader", style="Title.TLabel")
title.pack(side=tk.TOP, padx=10, pady=10)

# Prevent multiple instances
if os.path.exists("selected_text.mp3"):
    os.remove("selected_text.mp3")

# Set up buttons with hover effect
def create_button(text, command, bg_color):
    button = tk.Button(root, text=text, command=lambda: threading.Thread(target=command).start(), bg=bg_color, fg='black')

    def on_enter(event):
        button['fg'] = 'white'

    def on_leave(event):
        button['fg'] = 'black'

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack(side=tk.TOP, padx=10, pady=10)
    return button

read_button = create_button(read_text, read_selected_text, 'lightgreen')
pause_button = create_button(pause_text, toggle_pause, 'lightyellow')
stop_button = create_button(stop_text, stop_reading, 'lightcoral')
exit_text = "Exit" if lang == 'en' else "Salir"
exit_button = tk.Button(root, text=exit_text, command=root.destroy, bg='lightcoral', fg='black')
exit_button.pack(side=tk.TOP, padx=10, pady=10)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()