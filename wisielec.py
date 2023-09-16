import random

class hangman:

    def __init__(self):
        self.word = ['coke', 'coffee', 'tea', 'water']
        self.random_word = random.choice(self.word)
        self.wordlength = len(self.random_word)
        self.letters = []
        self.usedLetters = []
        self.health = 10
        self.wins = 0
        for i in range(self.wordlength):
            self.letters.append("_")
        self.printUserLetters()

    def input(self):
        userInput = input("Gimme a letter!: ")
        self.main(userInput)
    def printUserLetters(self):
        letters = ''
        for i in self.letters:
            letters += i

        print(letters)

    def main(self, litera):
        usedletter = 0
        WordContainsLetter = 0
        for i in self.usedLetters:
            if i == litera:
                print("You used this letter before!")
                return

        for i in range(self.wordlength):
            if self.random_word[i] == litera:
                self.letters[i] = self.random_word[i]
                WordContainsLetter = 1

            if usedletter == 0:
                self.addUsedLetter(litera)
                usedletter = 1

        if not WordContainsLetter:
            self.health -= 1
            self.addUsedLetter(litera)
            print("There is no such letter!")
            print("You have: ", self.health, " lifes")

            if not self.health:
                self.defeat()
                return

        self.win()
        self.printUserLetters()


    def addUsedLetter(self, letter):
        self.usedLetters.append(letter)

    def printUsedLetters(self):
        letters = ''
        for i in self.usedLetters:
            letters += i

        print(letters)
    def defeat(self):
        print("Defeat!")

    def win(self):
        if '_' not in self.letters:
            print("You Won!")