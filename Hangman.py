import random

won = 0
lose = 0
game = 1

print('H A N G M A N')
while game != 0:
    start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if start == 'exit':
        break

    elif start == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lose} times.')

    elif start == 'play':
        print()
        list = ['python', 'java', 'swift', 'javascript']
        list_elem = []
        list_letter = []

        elem = random.choice(list)
        dl = len(elem)
        for l in elem:
            list_elem.append(l)
            list_letter.append('-')
        i = 8
        print('-'* dl)
        victory = 0
        s_l = []

        while i != 0:
            letter = input('Input a letter: ')
            if len(letter) == 1:
                if letter.isalpha() and letter.islower():
                    if letter in list_elem and letter not in list_letter:
                        for b in range(0, len(list_elem)):
                            if list_elem[b] == letter:
                                list_letter[b] = letter
                        print()
                        print(''.join(list_letter))
                        if list_elem == list_letter:
                            print(f'You guessed the word {elem}!')
                            print('You survived!')
                            victory = 1
                            won += 1
                            break
                    elif letter in list_elem and letter in list_letter:
                        print("You've already guessed this letter.")
                        print()
                        print(''.join(list_letter))
                    elif letter in s_l:
                        print("You've already guessed this letter.")
                        print()
                        print(''.join(list_letter))
                    else:
                        print("That letter doesn't appear in the word.")
                        print()
                        print(''.join(list_letter))
                        i -= 1
                        s_l.append(letter)
                else:
                    print('Please, enter a lowercase letter from the English alphabet.')
                    print()
                    print(''.join(list_letter))
            else:
                print('Please, input a single letter.')
                print()
                print(''.join(list_letter))

        if victory == 0:
            print()
            print('You lost!')
            lose += 1

