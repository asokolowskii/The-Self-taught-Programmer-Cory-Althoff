from random import randint

word_list = ["cat", "dog" , "horse", "chicken", "duck", "zebra", "elephant"]
random_index = randint(0, len(word_list) - 1)
word = word_list[random_index]


def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Hangman Game")

    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Choose a letter: ")
        if guess in rletters:
            correct = rletters.index(guess)
            board[correct] = guess
            rletters[correct] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are the winner!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You've lost! The word was: {}.".format(word))

hangman(word)
