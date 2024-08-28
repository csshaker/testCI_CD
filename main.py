print('hello world')

def printSomething(text):
    print(text)

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def printInvoice(invoice):
    print(invoice)

class Student:
    def __init__(self, id, name, gpa):
        self.name = name
        self.id = id
        self.gpa = gpa

    