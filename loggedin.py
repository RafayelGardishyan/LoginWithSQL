from appJar import gui
import sqlite3



class welcome:

    app = gui("Welcome")
    app.setBg('orange')
    app.setPadding([5, 5])

    def editProfile(self, button):
        print("Hello")

    def __init__(self, unm):
        self.app.addLabel('message', 'Welcome to your profile ' + unm, 0, 0, 2)
        self.app.setLabelBg('message', 'blue')
        self.app.setLabelFg('message', 'orange')
        self.app.addLabelEntry('Name', 1, 0)
        self.app.addLabelEntry('Username', 1, 1)
        self.app.addLabelEntry('Email', 2, 0)
        self.app.addLabelEntry('Password', 2, 1)
        self.app.addButton('Save your profile settings', self.editProfile, 3, 1, 3)


        self.app.go()


if __name__ == '__main__':
    file = open('data/state.txt', 'r')
    status = file.read()
    if status == 'true':
        window = welcome()
        file = open('data/state.txt', 'w')
        status = file.write('false')
