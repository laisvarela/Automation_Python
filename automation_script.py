# all the links, emaisl and info used is from the bootcamp
import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# opening the browser
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(3)

# searching for the link
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

# this mouse position is from auxiliar.py
pyautogui.click(x=-1314, y=370)

# writing email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")

# writing password
pyautogui.write("123456")

# pressing enter on login button
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

