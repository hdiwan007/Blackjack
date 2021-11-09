import random
from art import logo
import os


def score(slist):  # Calculate the score of player/computer through their card list
    if 11 in slist:
        if sum(slist) > 21:
            return (sum(slist) - 10)  # Consider ace as 1 if went over 21
        else:
            return sum(slist)
    else:
        return sum(slist)


def decide(plist, clist):  # Decide if the player wins or loses
    if score(clist) > 21:  # If the computer goes over 21
        print(f'  Your final hand: {plist}, final score: {score(plist)}')
        print(
            f'  Computer\'s final hand: {clist}, final score: {score(clist)}')
        print('Computer Went Over. You Win :)')
    elif score(plist) > 21:  # If the player goes over 21
        print(f'  Your final hand: {plist}, final score: {score(plist)}')
        print(
            f'  Computer\'s final hand: {clist}, final score: {score(clist)}')
        print('You went over. You lose :(')
    elif score(plist) < score(clist):  # If the computer's hand is better
        print(f'  Your final hand: {plist}, final score: {score(plist)}')
        print(
            f'  Computer\'s final hand: {clist}, final score: {score(clist)}')
        print('You lose :(')  # If the player's hand is better
    elif score(plist) > score(clist):
        print(f'  Your final hand: {plist}, final score: {score(plist)}')
        print(
            f'  Computer\'s final hand: {clist}, final score: {score(clist)}')
        print('You win :)')
    playmain()


def blackjack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pick01 = random.choice(cards)
    pick02 = random.choice(cards)
    # Choose 2 random cards and put them in a list of player's cards
    plist = [pick01, pick02]
    print(f'  Your cards: {plist}, current score: {score(plist)}')

    cick01 = random.choice(cards)
    cick02 = random.choice(cards)
    # Choose 2 random cards and put them in a list of computer's cards
    clist = [cick01, cick02]
    if score(clist) < 17:  # Draw a card if the sum is less than 17
        clist.append(random.choice(cards))
    print(f'  Computer\'s first card: {cick01}')

    while True:  # Prompt the user for drawing another card, repeat if they wish to do so
        if score(plist) < 21:
            draw = input(
                'Type \'y\' to get another card, type \'n\' to pass: ')
            if draw == 'y':
                plist.append(random.choice(cards))
                if score(plist) > 21:
                    decide(plist, clist)
                else:
                    print(
                        f'  Your cards: {plist}, current score: {score(plist)}')
                    print(f'  Computer\'s first card: {clist[0]}')
            else:
                decide(plist, clist)
        else:
            decide(plist, clist)


def playmain():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        os.system('clear')
        blackjack()
    else:
        quit()


playmain()
