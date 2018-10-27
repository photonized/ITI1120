import random

# Read and understand the docstrings of all of the functions in detail.


def make_deck(num):
    '''(int)->list of int
        Returns a list of integers representing the strange deck with num ranks.

    >>> deck=make_deck(13)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404, 105, 205, 305, 405, 106, 206, 306, 406, 107, 207, 307, 407, 108, 208, 308, 408, 109, 209, 309, 409, 110, 210, 310, 410, 111, 211, 311, 411, 112, 212, 312, 412, 113, 213, 313, 413]

    >>> deck=make_deck(4)
    >>> deck
    [101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]

    '''
    deck = []
    for i in range(1, num + 1):
        for j in range(1, 5):
            p1 = str(j)
            p2 = str(i)
            card = p1 + p2
            if len(card) == 2:
                card = p1 + "0" + p2
            deck += [int(card)]
    return deck


def shuffle_deck(deck):
    '''(list of int)->None
       Shuffles the given list of strings representing the playing deck

    Here you should use random.shuffle function from random module.
    
    Since shufflling is random, exceptionally in this function
    your output does not need to match that show in examples below:

    >>> deck=[101, 201, 301, 401, 102, 202, 302, 402, 103, 203, 303, 403, 104, 204, 304, 404]
    >>> shuffle_deck(deck)
    >>> deck
    [102, 101, 302, 104, 304, 103, 301, 403, 401, 404, 203, 204, 303, 202, 402, 201]
    >>> shuffle_deck(deck)
    >>> deck
    [402, 302, 303, 102, 104, 103, 203, 301, 401, 403, 204, 101, 304, 201, 404, 202]
    '''
    random.shuffle(deck)

def deal_cards_start(deck):
     '''(list of int)-> list of int

     Returns a list representing the player's starting hand.
     It is  obtained by dealing the first 7 cards from the top of the deck.
     Precondition: len(dec)>=7
     '''
     player = []
     for i in range(7):
         player += [deck[len(deck) - 1]]
         del deck[len(deck) - 1]
     return player


def deal_new_cards(deck, player, num):
    '''(list of int, list of int, int)-> None
    Given the remaining deck, current player's hand and an integer num,
    the function deals num cards to the player from the top of the deck.
    If len(deck)<num then len(deck) cards is dealt, in particular
    all the remaining cards from the deck are dealt.

    Precondition: 1<=num<=6 deck and player are disjoint subsets of the strange deck. 
    
    >>> deck=[201, 303, 210, 407, 213, 313]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 313, 213, 407, 210]
    >>> deck
    [201, 303]
    >>>

    >>> deck=[201, 303]
    >>> player=[302, 304, 404]
    >>> deal_new_cards(deck, player, 4)
    >>> player
    [302, 304, 404, 303, 201]
    >>> deck
    []
    '''
    if num>len(deck):
        for i in range(len(deck)):
            player += [deck[len(deck) - 1]]
            del deck[len(deck) - 1]
    else:
        for i in range(num):
            player+=[deck[len(deck)-1]]
            del deck[len(deck)-1]


def print_deck_twice(hand):
    '''(list)->None
    Prints elements of a given list deck in two useful ways.
    First way: sorted by suit and then rank.
    Second way: sorted by rank.
    Precondition: hand is a subset of the strange deck.
    
    Your function should not change the order of elements in list hand.
    You should first make a copy of the list and then call sorting functions/methods.

    Example run:
    >>> a=[311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]
    >>> print_deck_twice(a)

    101 104 105 202 204 301 303 305 306 311 313 401 407 408 409 410 

    101 301 401 202 303 104 204 105 305 306 407 408 409 410 311 313 
    >>> a
    [311, 409, 305, 104, 301, 204, 101, 306, 313, 202, 303, 410, 401, 105, 407, 408]

    '''
    c = hand.copy()
    for i in range(len(hand)):
        print(min(c), end=" ")
        c.remove(min(c))
    print("\n")

    b = []
    c = hand.copy()
    c.sort()
    count = 0
    while len(hand) != len(b):

        mini = 999
        for i in range(len(c)):
            current = c[i]
            if int(str(current)[1:]) < int(str(mini)[1:]):
                mini = current

        c.remove(mini)
        b += [mini]
        print(b[count], end=" ")
        count += 1
        


def is_valid(cards, player):
    '''(list of int, list of int)->bool
    Function returns True if every card in cards is the player's hand.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.

    Precondition: cards and player are subsets of the strange deck.
    
    >>> is_valid([210,310],[201, 201, 210, 302, 311])
    310 not in your hand. Invalid input
    False

    >>> is_valid([210,310],[201, 201, 210, 302, 310, 401])
    True
    '''
    tf = ""
    b = []
    c = player.copy()
    for i in range(len(cards)):
        if cards[i] in c:
            tf += "t"
            c.remove(cards[i])
        else:
            b += [cards[i]]
            tf += "f"

    if "f" in tf:
        print(str(b)[1:len(str(b)) - 1] + " not in your hand. Invalid input")
        return False
    return True

def is_discardable_kind(cards):
    '''(list of int)->True
    Function returns True if cards form 2-, 3- or 4- of a kind of the strange deck.
    Otherwise it returns False. If there  is not enough cards for a meld it also prints  a message about it,
    as illustrated in the followinng example runs.
    
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.
    
    >>> is_discardable_kind([207, 107, 407])
    True
    >>> is_discardable_kind([207, 107, 405, 305])
    False
    >>> is_discardable_kind([207])
    Invalid input. Discardable set needs to have at least 2 cards.
    False
    '''
    if len(cards)<2:
        print("Invalid input. Discardable set needs to have at least 2 cards.")
        return False
    b=[]
    for i in range(len(cards)):
        b+=[cards[i]-100*(cards[i]//100)]

    return len(b) == sum(b)/b[0]



def is_discardable_seq(cards):
    '''(list of int)->True
    Function returns True if cards form progression of the strange deck.
    Otherwise it prints an error message and then returns False,
    as illustrated in the followinng example runs.
    Precondition: cards is a subset of the strange deck.

    In this function you CANNOT use strings except in calls to print function. 
    In particular, you cannot conver elements of cards to strings.

    >>> is_discardable_seq([313, 311, 312])
    True
    >>> is_discardable_seq([311, 312, 313, 414])
    Invalid sequence. Cards are not of same suit.
    False
    >>> is_discardable_seq([311,312,313,316])
    Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.
    False
    >>> is_discardable_seq([201, 202])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    >>> is_discardable_seq([])
    Invalid sequence. Discardable sequence needs to have at least 3 cards.
    False
    '''

    b = []
    if len(cards) < 3:
        print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")
        return False

    for i in range(len(cards)):
        b += [cards[i] // 100]

    cards.sort()


    if not sum(b) / b[0] == len(b):
        print("Invalid sequence. Cards are not of same suit.")
        return False

    for i in range(len(cards)-1):
        if not cards[i+1]-cards[i] == 1:
            print("Invalid sequence. While the cards are of the same suit the ranks are not consecutive integers.")
            return False

    return True

def rolled_one_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 1
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> rolled_one_round(player)
    Discard any card of your choosing.
    Which card would you like to discard? 103
    103
    No such card in your hand. Try again.
    Which card would you like to discard? 102

    Here is your new hand printed in two ways:

    201 212 311 

    201 311 212 

    '''
    length = len(player)
    while length == len(player):
        choice = input("Discard any card of your choosing.\nWhich card would you like to discard? ")
        choice = choice.strip()
        print(choice)
        if choice.isdigit() and int(choice) in player:
            player.remove(int(choice))
        else:
            print("No such card in the deck. Try again.")
    print("Here is your new hand printed in two ways:\n")
    print_deck_twice(player)
    print("\n")

def rolled_nonone_round(player):
    '''(list of int)->None
    This function plays the part when the player rolls 2, 3, 4, 5, or 6.
    Precondition: player is a subset of the strange deck

    >>> #example 1:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 102 103 104
    103 not in your hand. Invalid input
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 403 203

    Here is your new hand printed in two ways:

    102 104 401 

    401 102 104 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 2:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412 413

    Here is your new hand printed in two ways:

    103 211 

    103 211 
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no

    >>> #example 3:
    >>> player=[211, 412, 411, 103, 413]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? yes
    Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: 411 412
    Invalid meld: 11 is not equal to 12
    Invalid sequence. Discardable sequence needs to have at least 3 cards.

    >>> #example 4:
    >>> player=[401, 102, 403, 104, 203]
    >>> rolled_nonone_round(player)
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? alsj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? hlakj
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? 22 33
    Yes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? no
    '''

    length = len(player)
    yon = "yes"
    yon = yon.strip().lower()
    print("\nHere is your new hand printed in two ways:\n")
    print_deck_twice(player)
    while yon != "no":
        yon = input(
            "\nYes or no, do you  have a sequences of three or more cards of the same suit or two or more of a kind? ")
        yon = yon.strip().lower()
        if yon == "yes":
            cards = input(
                "Which 3+ sequence or 2+ of a kind would you like to discard? Type in cards separated by space: ")
            cards = cards.strip().split()
            b = []
            if all_ints(cards):
                for i in range(len(cards)):
                    b += [int(cards[i])]
                if len(cards) == 2:
                    c = []
                    for i in range(len(cards)):
                        c += [int(cards[i]) // 100]
                    if is_valid(b, player):
                        if is_discardable_kind(b):
                            for i in range(len(b)):
                                player.remove(b[i])
                            print("\nHere is your new hand printed in two ways:\n")
                            print_deck_twice(player)
                            print("\n")
                        elif not is_discardable_kind(b) and (len(c) == sum(c) / c[0]):
                            print("Invalid sequence. Discardable sequence needs to have at least 3 cards.")


                elif is_valid(b, player):
                    if is_discardable_kind(b):
                        for i in range(len(b)):
                            player.remove(b[i])
                        print("\nHere is your new hand printed in two ways:\n")
                        print_deck_twice(player)
                    elif is_discardable_seq(b):
                        for i in range(len(b)):
                            player.remove(b[i])
                        print("\nHere is your new hand printed in two ways:\n")
                        print_deck_twice(player)
            else:
                print("Make sure you have only integers in your deck!")

def all_ints(l):
    """
    (list) -> bool
    Returns True if the list only contains digits and false otherwise.
    Preconditions: input is a list
    """
    for i in range(len(l)):
        if not l[i].isdigit():
            return False
    return True

def dice_roll():
    """
    (none) -> int
    Returns a number between 1 and 6, simulating a dice roll.
    Preconditions: none
    """
    print("Please roll the dice")
    dice=random.randint(1, 6)
    return dice


print("Welcome to Single Player Rummy with Dice and strange deck.\n")
size_change=input("The standard deck  has 52 cards: 13 ranks times 4 suits.\nWould you like to change the number of cards by changing the number of ranks? ").strip().lower()
if size_change == "yes":
    number="0"
    flag=True
    while flag:
        number = input("Enter a number between 3 and 99, for the number of ranks: ")
        if number.isdigit() and 3<=int(number)<=99:
            deck=make_deck(int(number))
            flag=False
    print("You are playing with a deck of "+ str(int(number)*4) +" cards")
else:
    deck=make_deck(13)
    print("You are playing with a deck of 52 cards")
shuffle_deck(deck)
personal=deal_cards_start(deck)
print("Here is your starting hand printed in two ways: \n")
print_deck_twice(personal)

ct=0
while personal!=[]:
    ct += 1
    print("\nWelcome to round " + str(ct) + ".")
    dice=dice_roll()
    if len(deck)>0:
        if dice == 1:
            print("You rolled the dice and it showed: 1")
            rolled_one_round(personal)
        else:
            print("You rolled the dice and it showed: " + str(dice))
            print("Since you rolled, " + str(dice) + " the following " + str(dice) + " or " + str(
                len(deck)) + " (if the deck has less than" + str(
                dice) + ") cards will be added to your hand from the top of the deck.")
            deal_new_cards(deck, personal, dice)
            rolled_nonone_round(personal)
    else:
        print("The game is in empty deck phase.\n")
        rolled_one_round(personal)
    print("Round " + str(ct) + " completed.")


print("Congratulations, you completed the game in "+str(ct)+" rounds.")
exit(0)
