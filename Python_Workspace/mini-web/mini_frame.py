import time


def login():
    return "---login--- %s" % time.ctime()


def register():
    return "---register--- %s" % time.ctime()


def application(file_name):
    if file_name == 'login.py':
        return login()
    elif file_name == 'register.py':
        return register()
    else:
        return "File Not Found"