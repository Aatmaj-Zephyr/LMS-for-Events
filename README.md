### Python miniproject

"A website for showing college events"

###### Implemented using Pywebio

### Problem statement

In Engineering colleges as we know a lot of events take place.All these events can be helpful for students to bond
as well as to boost their confidence and skill.But its quite possible that the information about these events don’t
reach the students or the targeted mass.In order to solve this problem we need a website that display the events
along with its attributes and is also editable.

Project description:The LMS event management system website is a website that is made using a python library
known as PYWEBIO that allows you to build simple web applications without the knowledge of HTML and Javascript. On this website you can :

1.Display the events being carried out in our college

2.Add events

3.Delete events


### How the code works

Firstly we created 2 classes Login and Event and then used getter setter method to get its details.

• We appended the details into a list named Eventlist and Loginlist respectively and then saved it in a csv file .

• This csv file is used to keep track of the events added and also the login credentials of the users.

• There are 2 separate csv files used …. 1 is Login.csv for login details and other is events.csv for event details.

• This csv is written read and saved using user built functions namely readEventlist,saveEventlist,readLoginlist,saveLoginlist.
