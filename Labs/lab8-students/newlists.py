import random

def make_matrix_random(a, b, x, y):
    '''(int,int,int)->2D list
    Returns a 2D list representing a matrix with a rows and b columns
    filled with random integers >=x and <=y
    Precondition: a,b positive and x <=y
    '''
    final = []


    for i in range(a):
        row = []
        for j in range(b):
            num = random.randint(x, y)
            row.append(num)
        final.append(row)
    return final


def sum_above_diagonal(m):
    '''(2D list)->number
    Returns the sum of the elements of the matarix m that are on or about the diagonal of m
    (for clarification see the slide entitled: Details about Prog Ex 2)
    Precondition: m is a square matrix filled with numbers

    >>> sum_above_diagonal([[1,2],[10,20]] )
    23
    '''
    # your code goes here
    sum=0
    for i in range(len(m)):
        for j in range(i, len(m[i])):
            sum+=m[i][j]
    return sum


def max_over_all_even_cols(m):
    '''(2D list)->number
    Returns the maximum element among all the numbers that are in even columns of m
    i.e the maximum element amoung all elements in 0th, 2th, 4th etc. column
    Precondition: m is a matrix filled with numbers with at least 1 row and 1 column

    >>> max_over_all_even_cols([1,1,1,1,1,1,1],[1,10,3,20,12,6,0] )
    12
    '''
    l=[]
    for i in range(len(m)):
        for j in range(0,len(m[i]),2):
            l.append(m[i][j])
    max=0
    for num in l:
        if num>max:
            max=num
    return max


def max_each_row(m):
    '''(2D list)->list
     Returns a list where in position p of the list is the max number among all the numebrs of p-th row of m
     Precondition: m is a matrix filled with numbers

     >>> max_each_row([[1,2],[200,0],[3,3],[-10,-20]])
     [2, 200, 3, -10]
     '''
    li=[]
    for l in m:
        max=0
        for n in l:
            if n<max:
                max=n
        for n in l:
            if n>max:
                max=n
        li.append(max)
    return li


def index_of_max_sum_row(m):
    '''(2D list)->int
    Returns the index of a row that has the largest sum of all the rows
    Precondition: m is a matrix filled with numbers
    >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [1,2]])
    2
    >>> index_of_max_sum_row([[100,100], [-100,0], [200,30], [10000,2]])
    3
    '''
    max=0
    ind=0
    for i in range(len(m)):
        sum=0
        for j in range(len(m[i])):
            sum+=m[i][j]
        if sum>max:
            max=sum
            ind=i
    return ind