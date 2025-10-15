import pyautogui

# pyautogui.sleep(2)
# p = pyautogui.position()
# print(p)

# pyautogui.sleep(2)
# pyautogui.moveTo(1758, 95, duration=2)  #천천히 이동
# pyautogui.click(1758, 95, duration=2)

# pyautogui.mouseInfo()

# pyautogui.sleep(2)
# pyautogui.moveTo(41, 39, duration=0.5)
# pyautogui.move(100, 100, duration=0.5)
# pyautogui.move(100, 100, duration=0.5)

pyautogui.sleep(3)
manage = pyautogui.locateOnScreen('data/manage.png')
print(manage)
pyautogui.click(manage)

# p = pyautogui.position()
# pyautogui.click(p.x, p.y)

# pyautogui.moveTo(p.x, p.y, duration=0.5)
# pyautogui.dragTo(100, 100, duration=0.5)