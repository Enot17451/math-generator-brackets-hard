from random import *

class Number:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])
        self.number = randint(1, 10)

    def __str__(self):
        return f"{self.number}"

    def printMinusOnly(self):
        if self.sign == "+":
            return f"{self.number}"
        else:
            return f"{self.sign}{self.number}"

    def printWithSign(self):
        return f"{self.sign}{self.number}"

    def printNoSign(self):
        return f"{self.number}"


class Sign:

    def __init__(self):
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        return f"{self.sign}"


class Var:

    def __init__(self,letterNum):
        self.number = randint(1, 10)
        self.letter = choice(letterNum)
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        temp = ""
        if self.sign != "+":
            temp += "-"
        if self.number != 1:
            temp += str(self.number)
        return f"{temp}{self.letter}"

    def printWithSign(self):
        return f"{self.sign}{self.number}"

class NumberChoicer:
    lettersList = ["x","y","z","a","b","c","m","n","k"]

    def __init__(self,lettersNumber):
        self.choicesLetters = choices(self.lettersList,k=lettersNumber)

    def createNumberOrVar(self):
        temp = randint(1,100)
        if temp > 10:
            return Var(self.choicesLetters)
        else:
            return Number()

class BracketsHard:

    def __init__(self):
        self.numberChoicer = NumberChoicer(2)

    def __str__(self):
        return (f"{self.numberChoicer.createNumberOrVar()}"
                f"{Sign()}"
                f"({self.numberChoicer.createNumberOrVar()}"
                f"{self.numberChoicer.createNumberOrVar().printWithSign()})"
                f"{Sign()}"
                f"({self.numberChoicer.createNumberOrVar()}"
                f"{self.numberChoicer.createNumberOrVar().printWithSign()})"
                f"{self.numberChoicer.createNumberOrVar().printWithSign()}")


n = 20
for x in range(n):
    print(BracketsHard())
