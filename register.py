from main import *


class dbActions:
    db = sqlite3.connect('Users')
    cursor = db.cursor()

    def __init__(self):
        self.db = sqlite3.connect('Users')
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(
                '''CREATE TABLE users(id INT PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)''')
            self.db.commit()
        except sqlite3.OperationalError:
            pass

    def commitData(self, username, email, password, name, errorfunc):
        try:
            dataInsertQuery = "INSERT INTO users (username, email, password, name) VALUES ('" + username + "', '" + email + "', '" + password + "', '" + name + "')"
            self.cursor.execute(dataInsertQuery)
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            errorfunc()


class register:
    app = gui("Register", "450x350")
    app.setBg('orange')
    app.setPadding([5, 5])

    def already(self):
        self.app.warningBox("Error", "There is already a user with this Email or Username")

    def register(self, button):
        data = dbActions()
        unm = self.app.getEntry("Username")
        pwd = self.app.getEntry("Password")
        cpwd = self.app.getEntry("Confirm Password")
        nam = self.app.getEntry("First and Last names")
        eml = self.app.getEntry("Email")
        if len(unm)> 0:
            if len(eml) > 0:
                if len(nam) > 0:
                    if len(pwd) > 5:
                        if pwd == cpwd:
                            if data.commitData(unm, eml, pwd, nam, self.already):
                                self.app.infoBox("Success", "You are successfully registered! Congratulations")
                                self.app.stop()
                                contin = login()
                            else:
                                self.app.warningBox("Error", "Database Error, Try again later")
                        else:
                            self.app.warningBox("Error", "The Passwords do not match")
                    else:
                        self.app.warningBox("Error", "The Password must contain more than 6 letters")
                else:
                    self.app.warningBox("Error", "You have to fill in your Name")
            else:
                self.app.warningBox("Error", "You have to fill in your Email")
        else:
            self.app.warningBox("Error", "You have to fill in your Username")

    def __init__(self):
        self.app.enableEnter(self.register)
        self.app.addLabel("Title", "Register")
        self.app.setLabelBg("Title", 'blue')
        self.app.setLabelFg("Title", 'orange')
        self.app.setLabelFont(18)
        self.app.addLabelEntry("First and Last names")
        self.app.addLabelEntry("Username")
        self.app.addLabelEntry("Email")
        self.app.addLabelSecretEntry("Password")
        self.app.addLabelSecretEntry("Confirm Password")

        self.app.addButton('Register', self.register)

        self.app.go()


if __name__ == '__main__':
    window = register()
