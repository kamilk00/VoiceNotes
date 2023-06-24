import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
import threading

def start_action():

    global stop_listening
    start_button.config(state = tk.DISABLED)
    stop_button.config(state = tk.NORMAL)
    save_button.config(state = tk.DISABLED)
    text_entry.config(state = tk.NORMAL)
    text_entry.delete('1.0', tk.END)
    stop_listening = recognizer.listen_in_background(sr.Microphone(), record)


def stop_action():

    global stop_listening
    stop_listening(wait_for_stop = False)
    start_button.config(state = tk.NORMAL)
    stop_button.config(state = tk.DISABLED)
    save_button.config(state = tk.NORMAL)

def save_action():

    file_path = filedialog.asksaveasfilename(defaultextension = '.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_entry.get('1.0', tk.END))

def record(recognizer, audio):

    try:
        text = recognizer.recognize_google(audio, language = 'en-US')
        text_entry.insert(tk.END, text + '\n')

    except Exception:
        pass

window = tk.Tk()
window.configure(bg = '#567299')
window.title("Voice Notes")
window.geometry("600x400")

recognizer = sr.Recognizer()
stop_listening = None

text_entry = tk.Text(window, height = 20, width = 70, state = tk.DISABLED, wrap="word")
text_entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

start_button = tk.Button(window, text = "START", command = start_action, bg = "#4CAF50", fg = "white")
start_button.grid(row = 1, column = 0, padx = 5, pady = 5)

stop_button = tk.Button(window, text = "STOP", command = stop_action, state = tk.DISABLED, bg = "#F44336", fg = "white")
stop_button.grid(row = 1, column = 1, padx = 5, pady = 5)

save_button = tk.Button(window, text = "SAVE", command = save_action, bg = "#2196F3", fg = "white", state = tk.DISABLED)
save_button.grid(row = 1, column = 2, padx = 5, pady = 5)

window.mainloop()