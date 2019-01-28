import shelve as s
import sqlite3

db = sqlite3.connect('user.db')

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




class User:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password

users = s.open('user')

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def get_users():
    user_list = []
    klist = list(users.keys())
    for key in klist:
        user_list.append(users[key])
    return user_list

def init_users():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))

def get_user(username, password):
    if username in users:
        user = users[username]
        if username.password == password:
            return user
    return None

def create_user(username, password):
    u = User()
    u.name = username
    u.password = password
    users[username] = u
