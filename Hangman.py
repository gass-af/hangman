def hangman(word):
    wrong = 0
    rletters = list(word)
    stages = ["","______  ","|  | ","|  | ","|  0 ","| /|\ " , "| / \ ","|    "]
    board=["-"]*len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages):
        print("\n")
        msg="Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong +=1
        print(("".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "-" not in board:
              print("\nYou win! It was '{}'".format(word))
              win = True
              break
    
    if win == False:
        print("\n".join(stages[0:wrong]))
        print("\n You lose! It was '{}'.".format(word))
hangman("gaston")





