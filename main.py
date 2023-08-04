import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
import threading


#start recording
def start_action():

    global stop_listening
    start_button.config(state = tk.DISABLED)
    stop_button.config(state = tk.NORMAL)
    save_button.config(state = tk.DISABLED)
    text_entry.config(state = tk.NORMAL)
    text_entry.delete('1.0', tk.END)
    stop_listening = recognizer.listen_in_background(sr.Microphone(), record)


#stop recording
def stop_action():

    global stop_listening
    stop_listening(wait_for_stop = False)
    start_button.config(state = tk.NORMAL)
    stop_button.config(state = tk.DISABLED)
    save_button.config(state = tk.NORMAL)


#save as .txt file
def save_action():

    filetypes = [('Text files (*.txt)', '*.txt')]
    file_path = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = filetypes)
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_entry.get('1.0', tk.END))


#try to recognize audio
def record(recognizer, audio):

    try:
        text = recognizer.recognize_google(audio, language = selected_language_code)
        text_entry.insert(tk.END, text + '\n')

    except Exception:
        pass


#choose language (polish, english, german or spanish)
def choose_language(language):

    global selected_language_code
    selected_language_code = language_codes.get(language)


#declaration of variables
recognizer = sr.Recognizer()
stop_listening = None
languages = ['POLSKI', 'ENGLISH (US)', 'ENGLISH (UK)', 'DEUTSCH', 'ESPANOL']
language_codes = {
    'POLSKI': 'pl-PL',
    'ENGLISH (US)': 'en-US',
    'ENGLISH (UK)': 'en-GB',
    'DEUTSCH': 'de-DE',
    'ESPANOL': 'es-ES'
}
windowWidth = 600
windowHeight = 420

#prepare a window, place the window in the centre of the screen and declare controls
window = tk.Tk()
window.configure(bg = '#567299')
window.title("Voice Notes")
window.resizable(False, False)

positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))

text_entry = tk.Text(window, height = 20, width = 70, state = tk.DISABLED, wrap="word")
text_entry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

start_button = tk.Button(window, text = "START", command = start_action, bg = "#4CAF50", fg = "white")
start_button.grid(row = 1, column = 0, padx = 5, pady = 5)

stop_button = tk.Button(window, text = "STOP", command = stop_action, state = tk.DISABLED, bg = "#F44336", fg = "white")
stop_button.grid(row = 1, column = 1, padx = 5, pady = 5)

save_button = tk.Button(window, text = "SAVE", command = save_action, bg = "#2196F3", fg = "white", state = tk.DISABLED)
save_button.grid(row = 1, column = 2, padx = 5, pady = 5)

selected_language = tk.StringVar(window)
selected_language.set(languages[0])

selected_language_code = language_codes.get(languages[0])

language_menu = tk.OptionMenu(window, selected_language, *languages, command = choose_language)
language_menu.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)

window.mainloop()