Pmanager is the first Python application being uploaded in this repository. It uses Flask micro framework.
I recently learned Python, followed with Flask for about a week and to test my new skillset I decided to do this TODO app that manages tasks using Flask micro-framework.

Pmanager started initially as a task management system in which users are able to perform CRUD operations with it.

## FRONT-END
Materalize css - Finally after 4 years using Bootstrap I found the moment to try something else :)

## Back Features 
I used a few modules like: wtforms for the "create" part.
For the edit, I struggled a bit to set the default value of the form fields so I used regular HTML.
I also used bcrypt module, session(for authentication), and flashed messages.

## Authentication
During the time I was learning flask, I came across flask-login module which is pretty great per say. however, I opted to create my own authentication class which is still to be polished up.
Coming from Laravel background I'd say that there is a lot to be done still, but hey...I just lended in Python and actually spent most of my time looking into Jupyter!

## Database
Just before I looked into authentication, I also came across Alchemy module, pretty great, but again let's just say that it does a lot for one which is not good for someone like me who just started and need his practice.
Using mysql.connector I also built my own database class with the connection in its constructor.
It still has a long way to go of course, but slowly I'll get there surely.

# LET's GET STARTED! :)
After cloning the application, make sure you have a database which you will call pmanager and import the zipped the database from this repo.
The connection settings are in the database.py file's constructor class.



