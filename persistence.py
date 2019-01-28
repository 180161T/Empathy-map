import shelve as s
import sqlite3

db = sqlite3.connect('user.db')

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
