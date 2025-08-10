
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def register(self, username, email, password):
        username = self.username
        email = self.email
        password = self.password

    def login(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")
        print("Welcome back " + username)

    def password(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")

def main():
    user1 = User("John", "kk@ko", "9jiooi")
    user1.login("John", "Steve", "huioa")
    a = "Daniel"
    print(a.upper())
    print(user1.username)

    print(type(a))
    print(type(user1))


if __name__ == "__main__":
    main()