import pyautogui
import time
import tkinter as tk
from tkinter import Label


def show_caller_name(caller_name):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background='black')
    label = Label(root, text=caller_name, font=('Arial', 50), fg='white', bg='black')
    label.pack(expand=True)
    root.after(5000, root.destroy)
    root.mainloop()


def accept_call():
    accept_button_x, accept_button_y = 3899, 2666 #2929, 2003
    # print("In accept_call function")
    # button_location = pyautogui.locateOnScreen('video_call_button.png', confidence=0.9)
    # try:
    #     if button_location:
    #         pyautogui.click(button_location)
    #     else:
    #         print("Button not found!")
    # except pyautogui.ImageNotFoundException:
    #     print("Button no no")
    pyautogui.click(accept_button_x, accept_button_y)


def monitor_incoming_calls():
    while True:
        try:
            call_notification = pyautogui.locateOnScreen('Athul_call_notification_2.png', confidence=0.9)
            if call_notification:
                caller_name = "Athul"
                show_caller_name(caller_name)
                accept_call()
                time.sleep(10)
        except pyautogui.ImageNotFoundException:
            print('Waiting for call....')
        time.sleep(1)


if __name__ == "__main__":
    monitor_incoming_calls()
