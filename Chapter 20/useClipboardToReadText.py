#! python3
#  useClipboardToReadText.py - Copy text from Notepad to use elsewhere.

import pyautogui, pyperclip

fw = pyautogui.getWindowsWithTitle('Notepad')[0]
fw.activate()
pyautogui.click(fw.left + 100, fw.top + 100)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
text = pyperclip.paste()
print(text)