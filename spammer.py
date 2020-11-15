import pyautogui
import time
import os

time.sleep (5)
fn = r"C:\Dev\py_learn\spam_index"
os.path.exists(fn)
f = open (fn, 'r')
for word in f :
    pyautogui.typewrite(word)
    pyautogui.press("enter")
os.system("pause")