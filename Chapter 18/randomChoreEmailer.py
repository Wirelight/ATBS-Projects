#! python3
#  randomChoreEmailer.py - Sends emails with a random chore for the week.
#  Requires https://pyinputplus.readthedocs.io/en/latest/ and https://ezgmail.readthedocs.io/en/latest/

import random, ezgmail, sys
import pyinputplus as pyip

#Get the names and emails of assignees
def getAssignees():
    numAssignees = 0
    while True:
        addNew = pyip.inputYesNo('Do you wish to add a new person? (y/n)\n')
        if addNew == 'yes':
            assigneeName = pyip.inputStr('What\'s their name?\n')
            assigneeEmail = pyip.inputEmail('What\'s their email?\n')
            assignees[assigneeName] = {'email': assigneeEmail, 'currentChore': '', 'lastChore': ''}
            numAssignees += 1
        elif addNew == 'no':
            if not numAssignees > 0:
                print('You must add at least one assignee')
                continue
            break

#Get a list of the chores
def getChores():
    numChores = 0
    while True:
        addNew = pyip.inputYesNo('Do you wish to add a new chore? (y/n)\n')
        if addNew == 'yes':
            choresMaster.append(pyip.inputStr('What\'s the chore?\n'))
            numChores += 1
        elif addNew == 'no':
            if not numChores >= len(assignees):
                print('You  must have a number of chores at least equal to the number of assignees.')
                print('Please add another ' + str(len(assignees)-numChores) + ' chores')
                continue
            break

#Assign the chores
def assignChores():
    if len(choresMaster) > 0:
        chores = list(choresMaster)
        for assignee in assignees:
            randomChore = random.choice(chores)
            assignees[assignee]['currentChore'] = randomChore
            chores.remove(randomChore)
        print('\nChores assigned:\n')
        for assignee in assignees:
            print('Name: %s    Chore: %s' % (assignee, assignees[assignee]['currentChore']))
    else:
        print('Cannot assign an empty list of chores. Please add a chore and try again.\n')

#Email assignees their assigned chores
def emailAssignedChores():
    print(assignees)
    print(len(assignees))
    print(choresMaster)
    print(len(choresMaster))
    if len(choresMaster) > 0 and len(assignees) > 0:
        for assignee in assignees:
            body = '%s, your chore for the week is %s.' % (assignee, assignees[assignee]['currentChore'])
            print('Sending email to %s...' % assignees[assignee]['email'])
            ezgmail.send('giorgio.python.testbed@gmail.com', '%s: Your Weekly Chore' % assignee, body)
    else:
        print('Emails could not be sent. Either the list of chores or list of people is empty.\n')

def mainMenu():
    while True:
        print('Welcome to ChoreMaster. What would you like to do?\n')
        menuChoice = pyip.inputMenu(taskList, numbered=True)
    
        if menuChoice == 'Add a person':
            print()
            getAssignees()
        elif menuChoice == 'Add a chore':
            print()
            getChores()
        elif menuChoice == 'Assign chores':
            print()
            assignChores()
        elif menuChoice == 'Email assignees':
            print()
            emailAssignedChores()
        elif menuChoice == 'Exit':
            print()
            print('Exiting ChoreMaster. See you again soon!')
            sys.exit()

taskList = ['Add a person', 'Add a chore', 'Assign chores', 'Email assignees', 'Exit']
assignees = {}
choresMaster = []

mainMenu()

"""
Opportunities to extend program:
    - Store currentChore data to be pulled back in at next open
    - Handle cases with fewer or more chores than the number of people
    - On reopen, move currentChore into lastChore and make sure the same chore as last week cannot be assigned.
    - Handle cases to prevent emails sending where chores/assignees have been created, but chores have not been assigned
"""