# Importing the required module
import pyautogui as pg
import time
from selenium import webdriver

# Giving Dealy to run program
print("program will run after 5 second")
time.sleep(5)
print("running")

# For loop
for i in range(5):
    # # Find the connect button and assiging it to button
    button = find("connect")
    time.sleep(0.5)
    # Click the connect button
    button.click()