import tkinter as tk
import pygame
import keyboard
import threading

def add_crow():
    global crow_counter
    crow_counter += 1
    crow_text.config(text=f'\ncounted {crow_counter} crows')
    sound()

def sound():
    pygame.mixer.music.play()

def start_listener():
    keyboard.add_hotkey('F8', add_crow)

file = 'crow.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

root = tk.Tk()
crow_counter = 0

main_text = tk.Label(text='Crow counter\n', font=('Times', 14))
main_text.pack()

button_crow = tk.Button(text='ADD CROW\nPress F8', command=add_crow, bg='green')
button_crow.pack()

crow_text = tk.Label(text=f'\ncounted {crow_counter} crows')
crow_text.pack()

# Запускаем обработчик нажатий клавиш в отдельном потоке
thread = threading.Thread(target=start_listener)
thread.start()

root.geometry('200x150')
root.mainloop()
