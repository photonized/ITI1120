def is_square(m):
    '''2d-list => bool
    Return True if m is a square matrix, otherwise return False
    (Matrix is square if it has the same number of rows and columns'''
    for i in range(len(m)):
        if len(m[i]) != len(m):
            return False
    return True


def magic(m):
    '''2D list->bool
    Returns True if m forms a magic square
    Precondition: m is a matrix with at least 2 rows and 2 columns '''

    # this tests the condition that is implied by the definition
    # i.e. that m has to be a square matrix
    if (not (is_square(m))):  # if matrix is not square
        return False  # return False
    sums=[]

    #samechecker
    samelist=[]
    for l in m:
        for n in l:
            samelist.append(n)

    for i in range(len(samelist)-1):
        if samelist[i]==samelist[i+1]:
            return False
    #rows
    for l in m:
        sumrow = 0
        for num in l:
            sumrow+=num
        sums.append(sumrow)

    #diag-topleft-bottomright
    sumldiag = 0
    for i in range(len(m)):
        sumldiag+=m[i][i]
    sums.append(sumldiag)

    #diag-topright-bottomleft
    sumrdiag=0
    for i in range(len(m)):
        sumrdiag+=m[i][-1-i]
    sums.append(sumrdiag)

    #columns
    col=[]
    for i in range(len(m)):
        l=[]
        for j in range(len(m)):
            l.append(m[j][i])
        col.append(l)

    for l in col:
        sumcol = 0
        for num in l:
            sumcol+=num
        sums.append(sumcol)

    for i in range(len(sums)-1):
        if sums[i]!=sums[i+1]:
            return False
    return True


    # TEST CONDITION 1

    # TEST CONDITION 2


# main
# TESTING OF magic functions

# this should print True

m0 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(magic(m0))

# this should print True
m1 = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
print(magic(m1))

# this should print False. Why? Which condition imposed on magic squares is not true for m3
m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(magic(m2))

# this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 = [[1, 1], [1, 1]]
print(magic(m3))

# #this should print False. Why? Which condition imposed on magic squares is not
m3 = [[1, 1], [1, 1], [1, 2]]
print(magic(m3))
