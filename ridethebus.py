

import random
deck = []
faces = ['ace','two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
running = True
yourhand = []


class card:
    def __init__(self,face,suit, value):
        self.face = face
        self.suit = suit
        self.value = value


def generateDeck():
    deck = [] 
    for x in range (len(faces)):
        deck.append(card(faces[x],'hearts', values[x]))
        deck.append(card(faces[x],'diamonds', values[x]))
        deck.append(card(faces[x],'clubs', values[x]))
        deck.append(card(faces[x],'spades', values[x]))
    return deck



def gameOn():
    yourhand = []
    stage = 1
    while stage == 1:
        guess = None
        random.shuffle(deck)
        for x in range (4):
            yourhand.append(deck[x])
        print("There are four face-down cards in front of you, guess the color of the first card\n") 
        print("Black or Red: ")
        guess = input()
        guess.lower()
        if (guess == 'black'):
            if (yourhand[0].suit == 'spades' or yourhand[0].suit == 'clubs'): 
                print("correct", "the card was a", yourhand[0].face ,"of", yourhand[0].suit)
                stage = 2
            else:
                print("wrong! the card was a ", yourhand[0].face,"of",yourhand[0].suit, "The game will restart now")
                gameOn()

        if (guess == 'red'):
            if (yourhand[0].suit == 'hearts' or yourhand[0].suit == 'diamonds'): 
                print("correct", "the card was a", yourhand[0].face ,"of", yourhand[0].suit)
                stage = 2
            else:
                print("wrong! the card was a ", yourhand[0].face,"of",yourhand[0].suit, "The game will restart now")
                gameOn()
        else:
            print("It looks like your input was not 'red', or 'black', try again! ")

    while stage ==2:
        guess = None
        print("Welcome to stage two\n")
        print("You have a ", yourhand[0].face , "of", yourhand[0].suit ,"showing", "as well as three face down cards")
        print ("Will the next card be higher, or lower than the first?")
        print("higher, or lower: ")
        guess = input()
        guess.lower()
        if (guess == 'lower'):
            if (yourhand[1].value  < yourhand[0].value): 
                print("correct", "the card was a", yourhand[1].face ,"of", yourhand[1].suit)
                stage = 3
            else:
                print("wrong! the card was a ", yourhand[1].face,"of",yourhand[1].suit, "The game will restart now")
                gameOn()

        if (guess == 'higher'):
            if (yourhand[1].value > yourhand[0].value): 
                print("correct", "the card was a", yourhand[1].face ,"of", yourhand[1].suit)
                stage = 3
            else:
                print("wrong! the card was a ", yourhand[1].face,"of",yourhand[1].suit, "The game will restart now")
                gameOn()
        else:
            print("It looks like your input was not 'higher', or 'lower', try again! ")
 
    while stage == 3:
        guess = None
        print("Welcome to stage three\n")
        print("You have a ", yourhand[0].face , "of", yourhand[0].suit ,"and a", yourhand[1].face, "of", yourhand[1].suit, "showing", "as well as two face down cards")
        print ("Will the next card be inside, or outide the range of the first two cards?")
        print("inside, or outside: ")
        guess = input()
        guess.lower()
        if (guess == 'outside'):
            if (yourhand[2].value < yourhand[0].value and yourhand[2].value < yourhand[1].value): 
                print("correct", "the card was a", yourhand[2].face ,"of", yourhand[2].suit)
                stage = 4 
            elif(yourhand[2].value > yourhand[0].value and yourhand[2].value > yourhand[1].value):
                print("correct", "the card was a", yourhand[2].face ,"of", yourhand[2].suit)
                stage = 4 
            else:
                print("wrong! the card was a ", yourhand[2].face,"of",yourhand[2].suit, "The game will restart now")
                gameOn()

        if (guess == 'inside'):
            if (yourhand[2].value >= yourhand[0].value and yourhand[2].value <= yourhand[1].value): 
                print("correct", "the card was a", yourhand[2].face ,"of", yourhand[2].suit)
                stage = 4
            elif (yourhand[2].value >= yourhand[1].value and yourhand[2].value <= yourhand[0].value): 
                print("correct", "the card was a", yourhand[2].face ,"of", yourhand[2].suit)
                stage = 4
            else:
                print("wrong! the card was a ", yourhand[2].face,"of",yourhand[2].suit, "The game will restart now")
                gameOn()
        else:
            print("It looks like your input was not 'inside', or 'outside', try again! ")
 

    while stage == 4:
        guess = None
        print("Welcome to stage four\n")
        print("You have a ", yourhand[0].face , "of", yourhand[0].suit ,"a", yourhand[1].face, "of", yourhand[1].suit,"and a ", yourhand[2].face, "of", yourhand[2].suit, "showing", "as well as one face down card")
        print ("What is the suit of the final card?")
        print("diamonds, hearts, clubs, or spades: ")
        guess = input()
        guess.lower()
        if (guess == 'diamonds' or guess == 'hearts' or guess == 'spades' or guess == 'clubs'):
            if(guess == yourhand[3].suit):
                print("correct", "the card was a", yourhand[3].face ,"of", yourhand[3].suit)
                stage = 5 
            else:
                print("wrong! the card was a ", yourhand[3].face,"of",yourhand[3].suit, "The game will restart now")
                gameOn()

        else:
            print("It looks like your input was not a suit , try again! ")
    
    
    if (stage == 5):
        print("YOU WIN!!!")
        running = False


deck = generateDeck()
gameOn()


