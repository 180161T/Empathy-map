import shelve
import uuid


users = shelve.open('user.db')

#Yusuf part


def addTime(userName, newTime):
    if userName in timeInfo: # check if time already exists
        retrieveTimeValue = timeInfo[userName]   # retrieve the time history
        retrieveTimeValue.append(newTime)  # add new time
        del timeInfo[userName]
        timeInfo[userName] = retrieveTimeValue # update the new time history
    else:
        timeInfo[userName] = [newTime]  # just add a new time

def getTime(userName):
    if userName in timeInfo:
        return timeInfo[userName]

    else:
        return None

timeInfo = shelve.open('timeInfo')


class Settings:
    def __init__(self,num):
        self.__num=num


    def get_num(self):
        return self.__num


def createsettings(num):
    n=Settings(num)
    return n.get_num()

#Xavier part


class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


def create_user(username, password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    users[id] = user


def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
            return user
    return None


def update_user(id, user):
    users[id] = user
    return users[id]


def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]


def init_db():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))


def init():
    create_user("123","123")



class Notification:
    def __init__(self, chore, person):
        self.__chore = chore
        self.__person = person


todo = shelve.open('chores.db')


def get_chore(chore, person):
    if chore in todo:
        chore = todo[chore]
        if chore.person == person:
            return person
    return None


def clear_chore():
    clist = list(todo.keys())
    for key in clist:
        del todo[key]


def create_chore(chore, person):
    c = Notification()
    c.chore = chore
    c.person = person
    todo[chore] = c

#Ryan part


shelveopen = shelve.open('Temperature')


class Temperature:
    def __init__(self, ID):
        self.__ID = ID

    def getTemperature(self):
        return self.__Temperature

    def setTemperature(self, Temperature):
        self.__Temperature = Temperature

    def StoreData(self):
        shelveopen[self.__ID] = self.__Temperature
