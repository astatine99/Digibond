import pyautogui
import webbrowser
import time

number_to_call = input("Enter the number you want to call: ")
webbrowser.open_new("https://meet.google.com/calling")
# pyautogui.moveTo(1000, 1550)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.typewrite("chrome")
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.typewrite("meet.google.com/calling")
# time.sleep(1)
# pyautogui.press('enter')
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press(' ')
pyautogui.press('x')
pyautogui.keyUp('alt')
# pyautogui.press('f11')
time.sleep(4)
call_button_location = pyautogui.locateCenterOnScreen("start_call.png")
if call_button_location:
    pyautogui.click(call_button_location)
else:
    print("Join button not found!")
time.sleep(2)
pyautogui.typewrite(number_to_call)

video_call_button_location = pyautogui.locateCenterOnScreen("video_call_button.png")
if video_call_button_location:
    pyautogui.click(video_call_button_location)
else:
    print("Video call button not found!")
