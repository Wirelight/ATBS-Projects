#! python3
#  messengerBot.py - Finds and messages friends on Messenger.com with a notification message.

import pyautogui, time, pyinputplus

messageData = ''
nameData = []

searchCoords = (48,207)
messageCoords = (593,872)
pyautogui.PAUSE = 0.5

print('Welcome to Messenger Bot!')
messageData = pyinputplus.inputStr('Please enter the notification message you wish to send:\n')
while True:
    nameData.append(pyinputplus.inputStr('Please enter the full name of your notification recipient, as it appears on Facebook:\n'))
    k = pyinputplus.inputYesNo('Do you wish to add another recipient? (y/n)\n')
    if k == 'yes':
        continue
    elif k == 'no':
        if not len(nameData) > 0:
            print('You must provide at least one recipient.')
            continue
        break

print('Ensure that the messenger window is fullscreen, loaded and active!')
input('Press Enter when you are ready to begin.')

for i in range(len(nameData)):
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)
    print('Sending message to %s...' % (nameData[i]))
    #Locate search box, type name, select
    pyautogui.click(searchCoords[0], searchCoords[1])
    time.sleep(1)
    pyautogui.write(nameData[i], 0.25)
    time.sleep(1)
    pyautogui.write(['down', 'enter'], 0.5)
    time.sleep(1)
    #Locate the message box, type the message, send
    pyautogui.click(messageCoords[0], messageCoords[1])
    time.sleep(1)
    pyautogui.write(messageData, 0.25)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)

print('Program Complete. Notifications sent.')