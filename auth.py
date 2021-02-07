import sys


class UserAuth :

    def checkUserAuth(self):
        return False

    def checkUserNameAndPassWord(self, user_name, password):
        if user_name == "admin" and password == "123":
            return True

        return False
