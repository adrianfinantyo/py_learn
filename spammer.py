import pyautogui
import time
import os

time.sleep (5)
fn = "C:\\Dev\\py_learn\\spam_index.txt"
os.path.exists(fn)
f = open (fn, 'r')
for word in f :
    pyautogui.typewrite(word)
    pyautogui.press("enter")
os.system("pause")