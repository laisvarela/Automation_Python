# all the links, emaisl and info used is from the bootcamp
import pyautogui
import time
import pandas as pd

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

# login with email and password
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# import products
table = pd.read_csv("products.csv")

for line in table.index:
    # click on code input field
    pyautogui.click(x=-1392, y=259)
    # adding values from products in the matchin inputs fields
    pyautogui.write(str(table.loc[line, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[line, "obs"]
    # checks if the obs is null
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(1)