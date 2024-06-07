import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO
import locale
import subprocess
import sys
import threading

# List of required packages
required_packages = ['gtts', 'PIL', 'requests', 'customtkinter']

# Check if the required packages are installed, if not, install them
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"{package} is not installed. Installing now...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Check if gtts-cli is installed, if not, install it
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

# Function to read selected text
def read_selected_text():
    global is_paused
    selected_text = os.popen("xsel").read().strip()
    if selected_text:
        subprocess.run(f'echo "{selected_text}" | gtts-cli --nocheck -l {lang} - | mpg321 -', shell=True)

# Function to play audio
def play_audio():
    os.system("mpg321 selected_text.mp3")

# Function to stop reading
def stop_reading():
    os.system("pkill mpg321")

# Function to toggle pause
def toggle_pause():
    global is_paused
    if is_paused:
        os.system("pkill -CONT mpg321")
        is_paused = False
    else:
        os.system("pkill -STOP mpg321")
        is_paused = True

# Function to handle window closing
def on_closing():
    # Unbind <Configure> event from each button
    read_button.unbind('<Configure>')
    pause_button.unbind('<Configure>')
    stop_button.unbind('<Configure>')
    stop_reading()
    root.quit()  # Quit the mainloop
    os._exit(0)  # Exit the program

# Create the tkinter window
root = tk.Tk()
root.title("Parrot Reader")
""" root.configure(bg='#333333')"""
""" root.geometry('320x200')  """

# Load and display the logo
logo_url = "https://community.parrotsec.org/uploads/default/optimized/2X/4/48effee36b2b86615e4f4e4f865b61cbb0388a3f_2_460x333.png"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))
logo_image = logo_image.resize((100, 100))
logo_image = logo_image.convert("RGBA")

# Create a new image with the same size as the logo and white background
mask = Image.new('L', (100, 100), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, 100, 100), fill=255)

# Apply the mask to the logo
logo_image.putalpha(mask)

logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo, bg='#333333')
logo_label.pack(side=tk.TOP, padx=10, pady=10)

# Remove existing audio file if it exists
if os.path.exists("selected_text.mp3"):
    os.remove("selected_text.mp3")

# Create a new frame for the buttons
button_frame = tk.Frame(root, bg='#333333')
button_frame.pack()

# Function to create a button
def create_button(text, command, row, column):
    button = ctk.CTkButton(button_frame, text=text, command=lambda: threading.Thread(target=command).start(), corner_radius=10)
    button.grid(row=row, column=column, padx=5, pady=5)
    return button

# Create buttons
read_button = create_button(read_text, read_selected_text, 0, 0)
pause_button = create_button(pause_text, toggle_pause, 0, 1)
stop_button = create_button(stop_text, stop_reading, 1, 0)
exit_text = "Exit" if lang == 'en' else "Salir"
exit_button = create_button(exit_text, root.destroy, 1, 1)

# Handle window closing
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the tkinter main loop
root.mainloop()