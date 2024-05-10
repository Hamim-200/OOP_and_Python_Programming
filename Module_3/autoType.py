import pyautogui


screenWidth, screenHeight = pyautogui.size()
pyautogui.write('Hello world!', interval=0.25)
