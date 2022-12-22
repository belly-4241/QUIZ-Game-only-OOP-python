from utility import *

class menuu(maths, generals, football, sql):
    def con(self):
        choice = input("Available types of game .\n\t\t1 for maths\n\t\t2 for sport\n\t\t3 for general\nselect types of game you want to play ")
        if choice =="1":
            self.sport()
            self.db1 = []
        elif choice =="2":
            self.pro()
            self.db1 = []
        elif choice =="3":
            self.general()
            self.db1 = []

        else:
            print("please select one types of game")