# importing necessary libraries
import pywebio.output as pout
import pywebio.input as pimp
import csv

open('events.csv', 'a')  # initialize the output file


class Event:  # Event class

    def __init__(default, name, date, info):  # constructor
        default.name = name
        default.date = date
        default.info = info

    # setter methods
    def setDate(default, date):
        default.date = date

    def setInfo(default, info):  # short one line info
        default.info = info

    # getter methods
    def getName(default):
        return default.name

    def getDate(default):
        return default.date

    def getInfo(default):  # short one line info
        return default.info

    def printDetails(default):  # print details of the event
        print(default.getName())
        print(default.getDate())
        print(default.getInfo())


Eventlist = []  # GLOBAL VARIABLE


def readEventlist():
    with open('events.csv', 'r') as csvfile:
        for i in csvfile:
            i = i.split(",")
            Eventlist.append(Event(name=i[0], date=i[1], info=str(i[2])))
        csvfile.close()


def saveEventlist():
    '''
    Erases file as this is a very short list and not a huge database file.
    :return: none
    '''
    with open('events.csv', 'w') as csvfile:
        csvfile.truncate(0)
        writer = csv.writer(csvfile)
        for i in Eventlist:
            writer.writerow([i.getName(), i.getDate(), i.getInfo()])
        csvfile.close()


def addEvent(name, date, info):  # add event to list
    '''

    :param name: name of event
    :param date: date of event
    :param info: info about event
    :return: none
    '''

    Eventlist.append(Event(name=name, date=date, info=info))
    saveEventlist()  # save to database


def deleteEvent(name):  # delete event from list
    '''

    :param name: name of event
    :return: none
    '''
    '''
    Here it is assumed that if the event is present in the list then it is deleted else pass silently
    '''
    for i in Eventlist:
        if i.getName() == name:
            Eventlist.remove(i)
    saveEventlist()  # save to database


def editEvent(name, date, info):  # edit event info (Never used)
    '''

    :param name: name of event
    :param date: date of event
    :param info: info of event
    :return: none
    '''
    '''
    Editing will be carried out as deleting the event and adding a new one
    '''
   # Editing the event.
    for i in Eventlist:
        if i.getName() == name:
            i.setDate(date)
            i.setInfo(info)
    saveEventlist()  # save to database


def printEvents():  # print events Debug function
    '''
    :return: none
    '''
    print()
    for i in Eventlist:
        i.printDetails()
        print("----------------------------------------------------")


def displayEvents():
    # display events from list in scope1
    '''

    :return: None
    '''
    displaylist = [['Name of the event', 'Date of the event',
                    'Information']]  # lost to feed in put_table function contains a list of list.
    for i in Eventlist:
        displaylist.append([i.getName(), i.getDate(), i.getInfo()])
    pout.clear("scope1")  # clear prev display
    with pout.use_scope('scope1'):
        pout.put_table(displaylist)


def notBlank(data):
    # check if event parameters are blank else returns False
    '''

    :param data: input data from pywebio
    :return: error message or False
    '''
    if (data['name'] == ""):
        return ('name', 'Name cannot be blank!')
    if (data['date'] == ""):
        return ('date', 'Date cannot be blank!')
    if (data['info'] == ""):
        return ('info', 'Info cannot be blank!')
    return False


def addEventWeb():
    # add event from pywebio to list
    '''

    :return: none
    '''
    if(acess_modifier!=0):
        data = pimp.input_group("Add Event", [
            pimp.input('Enter name of the event you want to add', name='name'),
            pimp.input('Enter date of the event you want to add',
                    name='date', type=pimp.DATE),
            pimp.input('Enter info of the event you want to add', name='info')],
            validate=AddEventValidate
            # check if event exists or is blank to show error. error is handled by pywebio
        )
        addEvent(name=data['name'], date=data['date'], info=data['info'])


def AddEventValidate(data):
    # check if event exists or is blank to show error. error is handled by pywebio
    '''

    :param data: input data from pywebio
    :return: Tuple of (name, error)
    if the parameters are blank then it returns error for the parameter which is blank.
    Then it checks if the event exists or not and returns the error accordingly.
    '''
    if (notBlank(data) != False):  # if not blank return error message
        return notBlank(data)  # must return a tuple of (name, error)
    if (exists(data) == True):  # if already present then return error message
        return ('name', 'Event already exists!')


def DeleteEventValidate(data):
    # check if event exists or is blank to show error. error is handled by pywebio
    '''

    :param data: input data from pywebio
    :return: Tuple of (name, error)
    if the name is blank then it returns error
    Then it checks if the event exists or not and returns the error accordingly.
    '''
    if (data['name'] == ""):
        return ('name', 'Name cannot be blank!')
    if (exists(data) == False):  # if not present then return error message
        return ('name', 'Event doesnt exists!')


def exists(data):
    # check if event exists
    '''

    :param data: input data from pywebio
    :return: True if name already in Eventlist and false if name not found in Eventlist
    '''
    exists = False
    for i in Eventlist:
        if (i.getName() == data['name']):
            exists = True

    return exists


def deleteEventWeb():
    '''

    :return: None

    Deleted events from the web using the name parameter.
    '''
    if(acess_modifier!=0):
        data = pimp.input_group("Delete Event", [
            pimp.input('Enter name of the event you want to delete', name='name')],
            validate=DeleteEventValidate
            # check if event exists or is blank to show error. error is handled by pywebio
        )
        deleteEvent(name=data['name'])
def Login():
    data2 = pimp.input_group("Login", [
            pimp.input('Enter Username', name='username'),
            pimp.input('Enter Password',
                    name='password', type=pimp.PASSWORD),
            ]
            # check if event exists or is blank to show error. error is handled by pywebio
        )
def Register():
    data3 = pimp.input_group("Login", [
            pimp.input('Enter Username', name='username'),
            pimp.input('Enter Password',
                    name='password', type=pimp.PASSWORD),
            pimp.input('Enter Verif Code',
                    name='code')
            ]
            # check if event exists or is blank to show error. error is handled by pywebio
        )
acess_modifier=1
readEventlist()  # Get initial list of events
pout.put_button("Login", onclick=Login)  # a group of buttons
pout.put_button("Register", onclick=Register)  # a group of buttons
pout.put_button("Add Event", onclick=addEventWeb)  # a group of buttons
pout.put_button("Delete Event", onclick=deleteEventWeb)  # a group of buttons
pout.put_button("Display Events", onclick=displayEvents)  # a group of buttons
