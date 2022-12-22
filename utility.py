import random
import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=BELLY;'
                      'Database=belay.oop;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
class maths():
    def __init__(self):
        self.maths = []
    def get_math(self):
        self.maths = []
        self.maths.append(["what is the value of 'x' , 9x -2x+6=x?\nA.1  B.-2  C.-1  D.4", "c"])
        self.maths.append(["whats is the value of y, 3y-9=3? A. 2  B. 1 C. 4 D.6", "d"])
        self.maths.append(["maths is one of the subject that use to brainstorm?\n A.True  B.False", "True"])
        self.maths.append(["maths is the same as accounting?\n A. True  B. false", "A"])
        self.maths.append(["The simplify equation of x^+3x=x+9 is 4x.\n A. True  B. False", "A"])
        self.maths.append(["Types operation is similar to types of trigonometric.\n A. True B.false", "B"])
        return self.maths
    def sport(self):
        self.sports = self.get_math()
        random.shuffle(self.get_math())
        score = 0
        for s in self.sports:
            print( "", s[0])
            guess = input("enter Answer")
            if guess == s[1]:
                print("correct")
                score = score + 1
            else:
                print("incorrect")
        print("the final score:" + str(score),"/6")

        return self.sports
class generals():
    def __init__(self):
        self.generals = []
    def get_general(self):
        self.generals = []
        self.generals.append(["what is vires?\nA. kind of disease,B.incure disease,C.the same as bacteria D.easly transmitted disease", "D"])
        self.generals.append(["what is full abbrevaition of hiv?\nA.human immunity system B. human immunity virus","B"])
        self.generals.append(["what is abbrevaition oop?\nA.object oriented program B. object open program", "A"])
        self.generals.append(["what is object in python?\nA. one of class in python B.parts of python", " B"])
        self.generals.append(["what is class in python?\nA.parts of object B.direction indicator", " A"])
        self.generals.append(["what is sql?\nA.types of language B.types of computer language", "B"])
        return self.generals
    def general(self):
        self.gene = self.get_general()
        random.shuffle(self.get_general())

        score = 0
        for m in self.gene:
            print(":" + m[0])
            guess = input("enter answer")
            if guess == m[1]:
                print("correct")
                score = score + 1
            else:
                print("incorrect")
        print("the final score:" + str(score))
        return self.generals
class football():
    def __init__(self):
        self.bell = []
    def get_pro(self):
        self.bell = []
        self.bell.append(["who is the word best player?\nA.mess B.Ronaldo", "A"])
        self.bell.append(["who won the world cup 2022?\nA.argentina B.france", "B"])
        self.bell.append(["which team you appreciate?\nA.man united  B.arsenal", "A"])
        self.bell.append(["list five best team in premier league ?(only first letter of their name)\nA.mmacl B.wer", "A"])
        self.bell.append(["explain what is man united?\nA.a big club who won most trophys B. ", "man is"])
        self.bell.append(["which team is your favorite?", "fasil kenema"])
        self.bell.append(["what is the value of 'y', y^2 +2y+8=0?", ""])
        return self.bell
    def pro(self):
        self.problem = self.get_pro()
        random.shuffle(self.get_pro())
        score = 0
        for n in self.problem:
            print(":" + n[0])
            guess = input("enter answer")
            if guess == n[1]:
                print("correct")
                score = score + 1
            else:
                print("incorrect")
        print("the final score:" + str(score))
        return self.bell
class sql():
    def __init__(self):
        self.db1 = []
    def DB1(self):
        self.db1 = []
        name = input("NAME")
        Id = int(input("ID"))
        catagory = int(input("catagory"))
        equastion = input("equastion")
        opetion = int(input("opetion"))
        score = int(input("score"))
        cursor.execute("INSERT INTO [oop] (name,,Id,catagory,equastion, opetion,score) VALUES(?,?,?,?,?,?)", (name, Id, catagory,equastion,opetion, score))
        conn.commit()
        cursor.close()
        conn.close()