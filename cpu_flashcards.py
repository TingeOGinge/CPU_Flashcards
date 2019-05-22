from Registers import Register
from random import *


def getNumberOfRounds():
    return int(input("How many times would you like to play? "))

def askQuestion(chosenFlashcard):
    if random() < 0.5:        
        userAnswer = input("What does the following sentence describe\n'{0}'\n".format(
                            chosenFlashcard.getDescription()))
        return userAnswer
    
    userAnswer = input("The full name of {0} is the ____ \n".format(
                    chosenFlashcard.getAcronym()))
    return userAnswer

def checkAnswer(chosenFlashcard, userAnswer):
    if chosenFlashcard.getName() == userAnswer.title():
        return True
    return False

def printResult(chosenFlashcard, response, score, i):
    print("The correct answer was {0} \n".format(chosenFlashcard.getName()) + 
        "It seems you are {0} \nYour current score is {1}/{2} \n".format(
        response, score, i + 1))

def createCPURegisters():
    return [
        Register("PC", "Program Counter", "Contains the address of the instruction currently being executed"),
        Register("MAR", "Memory Address Register", "Holds the memory location of data that needs to be accessed"),
        Register("MBR", "Memory Buffer Register", "Holds the contents of the memory which are to be transferred from memory to other components, or vice versa"),
        Register("IBR", "Instruction Buffer Register", "Holds the opcode of the current fetched instruction"),
        Register("IR", "Instruction Register", "Holds the instruction currently being executed"),
        Register("AC", "Accumulator", "Temporarily stores data whilst calculations are being performed within the ALU")
    ]

def createComputerFunctions():
    return [
        Register("DP Function", "Data Processing", "Completes the instructions given from the 'control'"),
        Register("DS Function", "Data Storage", "Retains information for either short or long term periods for future use"),
        Register("DM Function", "Data Movement", "Loads and stores data from on place to another"),
        Register("C Function", "Control", "Runs the overall process of computer functions")
    ]

def playFlashcards(rounds, chosenFlashcard):
    score = 0
    for i in range(rounds):
        userAnswer = askQuestion(chosenFlashcard)
        if (userAnswer == "EXIT"): 
            break
        response = "wrong :("
        if checkAnswer(chosenFlashcard, userAnswer):
            response = "correct!"
            score += 1
        printResult(chosenFlashcard, response, score, i)
    print("\n\nYou ended with a score of {0}/{1}".format(score, i))

def memoryRegisters():
    cpuRegisters = createCPURegisters()
    rounds = getNumberOfRounds()
    playFlashcards(rounds, choice(cpuRegisters))

def computerFunctions():
    computerFunctions = createComputerFunctions()
    rounds = getNumberOfRounds()
    playFlashcards(rounds, choice(computerFunctions))

def combinedQuestions():
    computerFunctions = createComputerFunctions()
    cpuRegisters = createCPURegisters()
    rounds = getNumberOfRounds()
    playFlashcards(rounds, choice([choice(computerFunctions), choice(cpuRegisters)]))