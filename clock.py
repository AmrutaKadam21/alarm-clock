import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import time
import threading
import pygame

pygame.mixer.init()

# Alarm functions
def play_alarm_sound():
    pygame.mixer.music.load(alarm_file.get())
    pygame.mixer.music.play(-1)

def stop_alarm_sound():
    pygame.mixer.music.stop()
    alarm_window.destroy()

def check_alarm():
    set_time = alarm_time.get().strip()
    if not set_time:
        messagebox.showerror("Error", "Please enter time in HH:MM format")
        return
    def run_alarm_check():
        while True:
            now = time.strftime("%H:%M")
            if now == set_time:
                show_alarm_window()
                break
            time.sleep(1)
    threading.Thread(target=run_alarm_check, daemon=True).start()

# Alarm popup window
def show_alarm_window():
    global alarm_window
    alarm_window = tk.Toplevel(root)
    alarm_window.title("⏰ Wake Up!")

    # Set size
    win_w = 500
    win_h = 300
    alarm_window.geometry(f"{win_w}x{win_h}")

    # Background image for alarm
    bg_alarm = Image.open("img1.jpg")
    bg_alarm = bg_alarm.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

    bg_alarm_img = ImageTk.PhotoImage(bg_alarm)
    label_bg = tk.Label(alarm_window, image=bg_alarm_img)
    label_bg.image = bg_alarm_img
    label_bg.place(x=0, y=0, relwidth=1, relheight=1)

    label = tk.Label(alarm_window, text="⏰ Wake Up! ⏰", font=("Arial", 20, "bold"), bg="white", fg="red")
    label.pack(pady=20)

    stop_btn = tk.Button(alarm_window, text="Stop", font=("Arial", 14), bg="red", fg="white", command=stop_alarm_sound)
    stop_btn.pack(pady=10)

    play_alarm_sound()

# Music selection
def choose_music():
    file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if file:
        alarm_file.set(file)

# Update current time
def update_clock():
    now = time.strftime("%I:%M:%S %p")
    current_time_label.config(text="Current Time: " + now)
    root.after(1000, update_clock)

# Main window setup
root = tk.Tk()
root.title("Alarm Clock")

# Get screen size for full background
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Background image for main window
bg_img = Image.open("back.png")
bg_img = bg_img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variables
alarm_time = tk.StringVar()
alarm_file = tk.StringVar()

# UI elements
current_time_label = tk.Label(root, text="", font=("Arial", 16), bg="white")
current_time_label.pack(pady=10)

tk.Label(root, text="Set Alarm Time (HH:MM):", font=("Arial", 14), bg="white").pack(pady=5)
alarm_entry = tk.Entry(root, textvariable=alarm_time, font=("Arial", 14))
alarm_entry.pack(pady=5)

tk.Button(root, text="Choose Ringtone", font=("Arial", 12), command=choose_music, bg="#007bff", fg="white").pack(pady=10)

tk.Button(root, text="Set Alarm", font=("Arial", 14), command=check_alarm, bg="green", fg="white").pack(pady=10)

update_clock()
root.mainloop()


