import math
import random


class Point:
    'class that represents a point in the plane'

    ## exectuting Point(2,3)
    ## 1. creates an object of type point
    ## 2. calls an objects __init__ method
    ## 3. produces an object's memory address

    ## Assigning to a new variable using dot operator
    ## CREATES THAT VARIABLE INSIDE OF THE OBJECT

    ## Variables INSIDE of an object are called INSTANCE variables

    ## __init__ is method that is called to initialize the object (create it and initialize its variables)
    ## the first parameter of method is usually called self
    ## self refers to the object that is being initialized

    #    constructor
    #    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def distance(self, other):
        side1 = other.x - self.x
        side2 = other.y - self.y
        return math.sqrt(side1 ** 2 + side2 ** 2)

    def up(self):
        self.move(0, 1)

    def down(self):
        self.move(0, -1)

    def right(self):
        self.move(1, 0)

    def left(self):
        self.move(-1, 0)


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', years=0):
        self.spec = species
        self.lang = language
        self.age = years

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def getAge(self):
        return self.age

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec, 'and I', self.lang)


class Bird(Animal):  # class Bird inherits all atributes (data and method) from class Animal
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        print(self.language * 3)


class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit

    def __repr__(self):
        'return formal representation'
        return 'Card(' + self.rank + ',' + self.suit + ')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank


class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []  # deck is initially empty

        for suit in Deck.suits:  # suits and ranks are Deck
            for rank in Deck.ranks:  # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank, suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)

    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck(' + str(self.deck) + ')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck


class BankAccount:
    'da bank'

    def __init__(self, balance=0):
        self.bal = balance

    def balance(self):
        return float(self.bal)

    def withdraw(self, withdraw):
        self.bal -= withdraw

    def deposit(self, deposit):
        self.bal += deposit

    def __repr__(self):
        return "BankAccount(" + str(float(self.bal)) + ")"


class PingPong:
    def __init__(self):
        self.curr = "PING"
        self.later = "PONG"

    def next(self):
        print(self.curr)
        self.curr, self.later = self.later, self.curr


class Queue:
    def __init__(self, q=None):
        if q == None:
            q=[]

        self.q = q

    def enqueue(self, other):
        self.q.append(other)

    def dequeue(self):
        return self.q.pop(0)

    def isEmpty(self):
        return self.q == []

    def __eq__(self, other):
        return self.q == other

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        return "Queue()"


class Vector:
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        return self.x * other.x

    def __repr__(self):
        return "Vector("+str(self.x)+")"


class Marsupial:

    def __init__(self, color):
        self.color=color
        self.pouch=[]

    def put_in_pouch(self, item):
        self.pouch.append(item)

    def pouch_contents(self):
        print(self.pouch)

    def __str__(self):
        return "I am a {} Marsupial".format(self.color)


class Kangaroo(Marsupial):
    def __init__(self, col, x, y):
        super().__init__(col)
        self.x=x
        self.y=y

    def jump(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def __str__(self):
        return "I am a {} Kangaroo located at ({}, {})".format(self.color, self.x, self.y())

class Points:
    def __init__(self, points=None):
        if points == None:
            points=[]
        self.points = points

    def add(self, x, y):
        self.points.append(Point(x,y))

    def __len__(self):
        return len(self.points)

    def __repr__(self):
        return "Points({})".format(self.points)

    def left_most_point(self):
        if not self.points: return None

        answer = self.points[0]

        for p in self.points:
            if p.x<answer.x:
                answer=p
            elif p.x == answer.x and p.y < answer.y:
                answer = p
        return answer
