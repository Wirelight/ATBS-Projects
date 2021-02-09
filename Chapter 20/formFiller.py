#! python3
#  formFiller.py - Automatically fills in the form at https://autbor.com/form

import pyautogui, time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the \
                break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. \
                Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active the form is loaded!')
submitAnotherLink = (876,280)

for person in formData:
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t','\t'])
    pyautogui.write(person['name'] + '\t')
    pyautogui.write(person['fear'] + '\t')
    
    if person['source'] == 'wand':
        pyautogui.write(['down', 'space', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'space', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'space', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'space', '\t'], 0.5)

    if person['robocop'] == 1:
        pyautogui.write(['space', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)
    
    pyautogui.write(person['comments'] + '\t')
    time.sleep(0.5)
    pyautogui.press('enter')

    print('Submitted form')
    time.sleep(5)

    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])