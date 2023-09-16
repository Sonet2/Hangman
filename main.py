from wisielec import hangman

print("Hangman!")

gierka = hangman()

while not gierka.wins:
    gierka.input()

