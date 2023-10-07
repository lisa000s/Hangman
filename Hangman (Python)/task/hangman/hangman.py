import random

words = ['python','java','swift','javascript']
# words = ['java']
computer_pick = random.choice(words)
print("H A N G M A N")
start_message = "Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit: "
choice = ""
count_lost = 0
count_win = 0
while choice != "exit":
    print(start_message, end='')
    choice = input()
    if choice == "play":
        attempts = 8
        guessed_word = list('-' * (len(computer_pick)))
        guessed_word_str = ""
        temp_letter = ''
        while attempts != 0:
            print("\n",end='')
            print(guessed_word_str.join(guessed_word))
            print("Input a letter: ",end='')
            letter = input()
            if len(letter) > 1 or len(letter) == 0:
                print("Please, input a single letter.")
            elif not letter.isalpha() or not letter != letter.upper():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in computer_pick:
                for i in range(len(guessed_word)):
                    if letter == computer_pick[i]:
                        if guessed_word[i] == letter:
                            print("You've already guessed this letter.")
                            break
                        else:
                            guessed_word[i] = letter
            else:
                if temp_letter == letter:
                    print("You've already guessed this letter.")
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
            if guessed_word_str.join(guessed_word) == computer_pick:
                break
            temp_letter = letter
        guessed_word_str = guessed_word_str.join(guessed_word)
        if guessed_word_str == computer_pick:
            print("\nYou guessed the word {}!".format(computer_pick))
            print("You survived!")
            count_win += 1
        else:
            print("\nYou lost!")
            count_lost += 1
    if choice == "results":
        print("You won:", count_win, "times.")
        print("You lost:", count_lost, "times.")


