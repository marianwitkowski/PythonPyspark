
# Metody statyczne i klasowe
import random
import time


class User:
    def __init__(self, username, password):
        self.username = username
        self.pasword = password

    def __str__(self):
        return f"{self.username}:{self.pasword}"

    @staticmethod # metoda statyczna
    def generate_password():
        random.seed(time.time_ns())
        items = random.choices("123456789lmnoqprstuw", k=8)
        passwd = "".join(items)
        return passwd

    @classmethod # metoda klasowa
    def create_user(cls, username):
        return cls(username, User.generate_password())

####
for _ in range(5):
    #user = User("jkowalski", User.generate_password())
    user = User.create_user("jkowalski")
    print(user)