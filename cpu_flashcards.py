from Registers import Register
from random import *


def getNumberOfRounds():
    return int(input("How many times would you like to play? "))

def askQuestion(chosenLayer):
    if random() < 0.5:        
        userAnswer = input("Which CPU register does the following sentence " + 
                    "describe\n'{0}'\n".format(chosenLayer.getDescription()))
        return userAnswer
    
    userAnswer = input("The full name of {0} is the ____ \n".format(
                    chosenLayer.getAcronym()))
    return userAnswer

def checkAnswer(chosenLayer, userAnswer):
    if chosenLayer.getName() == userAnswer.title():
        return True
    return False

def printResult(chosenLayer, response, score, i):
    print("The correct answer was {0} \n".format(chosenLayer.getName()) + 
        "It seems you are {0} \nYour current score is {1}/{2} \n".format(
        response, score, i + 1))

def createCPURegisters():
    return [
        Register("PC", "Program Counter", "Contains the address of the instruction currently being executed"),
        Register("MAR", "Memory Address Register", "Holds the memory location of data that needs to be accessed"),
        Register("MBR", "Memory Buffer Register", "Holds the contents of the memory which are to be transferred from memory to other components, or vice versa"),
        Register("IBR", "Instruction Buffer Register", "Holds the opcode of the current fetched instruction"),
        Register("IR", "Instruction Register", "Holds the instruction currently being executed"),
        Register("AC", "Accumulator", "Temporarily stores data whilst calculations ware being performed within the ALU")
    ]

def main():
    cpuRegisters = createCPURegisters()
    score = 0
    rounds = getNumberOfRounds()
    for i in range(rounds):
        chosenLayer = choice(cpuRegisters)
        userAnswer = askQuestion(chosenLayer)
        response = "wrong :("
        if checkAnswer(chosenLayer, userAnswer):
            response = "correct!"
            score += 1
        printResult(chosenLayer, response, score, i)

main()