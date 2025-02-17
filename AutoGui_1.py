import tkinter
import time
import pyautogui
runs = 54
runs_10 = 5
runs1= 3
runs2= 3
runs3= 4
runs4= 3
runs5= 2





print(pyautogui.position())
pyautogui.moveTo(1872, 118, duration=0.1)
pyautogui.leftClick()
pyautogui.moveTo(406, 163, duration=0.1)
time.sleep(1)
pyautogui.dragRel(30, 0, duration=0.3)
runs += 1
pyautogui.typewrite(str(runs))


if runs % 10 == 0 and not runs >= 100:
    runs_10 += 1
    pyautogui.moveRel(-5, 15, duration=0.3)
    pyautogui.dragRel(30, 00, duration=0.3)
    pyautogui.typewrite(str(runs_10))

    pyautogui.moveRel(0, 23 * runs_10 - 23, duration=0.3)
    pyautogui.leftClick()
    pyautogui.press("enter")
    pyautogui.typewrite('runs'+ str(runs_10)+'= 0')

if runs % 3 == 0 and not runs <= 10:
    pyautogui.moveTo(406, 163, duration=0.3)
    pyautogui.dragRel(10, 0, duration=0.3)
    pyautogui.hotkey("ctrl", "c")
    clipboard_content = tkinter.Tk().clipboard_get()
    print(clipboard_content)





    if int(clipboard_content) == 1:
        pyautogui.moveTo(405, 207, duration=0.3)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(runs1))
        runs1 += 1
    if int(clipboard_content) == 2:
        pyautogui.moveTo(405, 230, duration=0.3)
        pyautogui.doubleClick()
        runs2 += 1
        pyautogui.typewrite(str(runs2))
    if int(clipboard_content) == 3:
        pyautogui.moveTo(405, 252, duration=0.3)
        pyautogui.doubleClick()
        runs3 += 1
        pyautogui.typewrite(str(runs3))
    if int(clipboard_content) == 4:
        runs4 += 1
        pyautogui.moveTo(405, 274, duration=0.3)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(runs4))
    if int(clipboard_content) == 5:
        runs5 += 1
        pyautogui.moveTo(405, 296, duration=0.3)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(runs5))
    if int(clipboard_content) == 6:
        pyautogui.moveTo(405, 318, duration=0.3)
        pyautogui.doubleClick()
        runs6 += 1
        pyautogui.typewrite(str(runs6))
    if int(clipboard_content) == 7:
        runs7 += 1
        pyautogui.moveTo(405, 340, duration=0.3)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(runs7))
    if int(clipboard_content) == 8:
        runs8 += 1
        pyautogui.moveTo(405, 362, duration=0.3)
        pyautogui.doubleClick()
        pyautogui.typewrite(str(runs8))
    if int(clipboard_content) == 9:
        pyautogui.moveTo(405, 384, duration=0.3)
        pyautogui.doubleClick()
        runs9 += 1
        pyautogui.typewrite(str(runs9))


"""
pyautogui.alert(text='Warning! Malware Detected!', title='Windows Malware Protection', button='OK', )
pyautogui.confirm(text='PRESS OK', title='V1RU5', buttons=['OK', 'OK'])
pyautogui.password(text='TYPE YOUR PASSWORD', title='V1RU5', default='', mask='*')
pyautogui.password(text='CONFIRM YOUR PASSWORD', title='V1RU5', default='', mask='*')
pyautogui.alert(text='THANK YOU FOR YOUR COOPERATION', title='V1RU5', button='delete Systen69', )
"""


