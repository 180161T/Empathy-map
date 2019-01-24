import shelve
import uuid


users = shelve.open('user.db')


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
    def __init__(self):
        self.chore = ''
        self.person = ''


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



