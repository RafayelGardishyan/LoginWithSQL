from register import *


class dbActions:
    db = sqlite3.connect('Users')
    cursor = db.cursor()
    dataGetQuery = "SELECT password FROM users WHERE username = '"

    def __init__(self):
        self.db = sqlite3.connect('Users')
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(
                '''CREATE TABLE users(id INT PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)''')
            self.db.commit()
        except sqlite3.OperationalError:
            pass

    def getData(self, username, password):
        self.cursor.execute(self.dataGetQuery + username + "'")
        gotpassword = self.cursor.fetchone()
        if gotpassword:
            gotpassword = gotpassword[0]
        if gotpassword == password:
            return True
        else:
            return False


class login:
    app = gui("Login", "400x200")
    app.setBg('orange')
    app.setPadding([5, 5])

    def login(self, button):
        if button == 'Register':
            self.app.stop()
            regiwindow = register()
        else:
            data = dbActions()
            unm = self.app.getEntry("Username")
            pwd = self.app.getEntry("Password")
            if data.getData(unm, pwd):
                self.app.infoBox("Success", "You are successfully logged in! Congratulations")
                self.app.stop()
                data.db.close()
                file = open('data/state.txt', 'w')
                file.write('true')
                file = open('data/state.txt', 'r')
                status = file.read()
                if status == 'true':
                    file = open('data/state.txt', 'w')
                    status = file.write('false')
                    window3 = welcome(unm)
            else:
                self.app.warningBox("Error", "Invalid username or password. Try again")

    def __init__(self):
        self.app.enableEnter(self.login)
        self.app.addLabel("Title", "Login or register to continue!")
        self.app.setLabelBg("Title", 'blue')
        self.app.setLabelFg("Title", 'orange')
        self.app.setLabelFont(18)
        self.app.addLabelEntry("Username")
        self.app.addLabelSecretEntry("Password")
        self.app.addButtons(['Register', 'Login'], self.login)

        self.app.go()


if __name__ == '__main__':
    window = login()

