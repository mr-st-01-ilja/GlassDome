import tkinter
import time
import pyautogui as pya
print(pya.position())
pya.moveTo(1872, 118, duration=0.3)
pya.click()
pya.moveTo(616, 161, duration=0.3)
pya.dragTo(616, 365, duration=0.3)
pya.hotkey("ctrl", "c")
pya.moveTo(616, 161, duration=0.3)
pya.click()
pya.hotkey("ctrl", "v")




pya.moveTo(1535, 25, duration=0.3)
time.sleep(1)
pya.click()





