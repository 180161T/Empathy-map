import shelve


class User:
    def __init__(self):
        self.username = ''
        self.password = ''


with shelve.open('loginPage') as loginFile:
    loginFile['user1'] = {
        'Username': 'xavier',
        'Password': 'haha',
    }


def clear_user():
    klist = list(loginFile.keys())
    for key in klist:
        del loginFile[key]


def get_users():
    user_list = []
    klist = list(loginFile.keys())
    for key in klist:
        user_list.append(loginFile[key])
    return user_list


def init_users():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))


def get_user(username, password):
    if username in loginFile:
        user = loginFile[username]
        if  user.password == password:
            return user
    return None


def create_user(username, password):
    u = User()
    u.username = username
    u.password = password
    loginFile[username] = u


class Notification:
    def __init__(self):
        self.chore = ''
        self.person = ''


todo = shelve.open('chores')


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



