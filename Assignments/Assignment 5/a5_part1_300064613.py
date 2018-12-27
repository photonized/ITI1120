import string

def open_file():
    '''None->file object
    Prompts for user input and returns an object of the file name given.
    Preconditions: none
    '''
    file_name=None
    while file_name==None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    return open(file_name, encoding="UTF-8")
   

def read_file(fp):
    '''(file object)->dict
    Processes the file and returns a dictionary of all the words in the file, with the lines that contain that word as
    keys for the dictionary values minus all punctuation, spaces, and words that have less that two letters.
    Preconditions: none'''
    f = fp.read().splitlines()

    temp2=split_and_lower(f)
    temp=remove_pun(temp2)

    temp=remove_unneeded(temp)

    dic=make_dic(temp)

    return dic


def find_coexistance(D, query):
    """(dict, str)->list
    returns a list of all the line numbers that contain all of the words given in the dictionary.
    Preconditions: none"""
    query=query.strip().split()

    dicnum=[]

    common=[]


    for word in query:
        if word not in D:
            return None
        dicnum.append(D[word])

    if len(dicnum)==0:
        return None

    if len(dicnum)==1:
        for num in dicnum[0]:
            common.append(num)

    if len(dicnum)>1:
        inter=dicnum[0].intersection(dicnum[1])

        for i in range(2,len(dicnum)):
            inter = inter.intersection(dicnum[i])

        for num in inter:
            common.append(num)
    common.sort()
    return common

###my personal functions###
def remove_pun(lst):
    """(list)->list
    returns a list of all the words with the punctuation removed.
    Preconditions: none"""
    not_allowed = string.punctuation
    removed=[]
    for line in lst:
        temp_not_allowed = []
        for word in line:
            a=""
            for char in word:
                if char not in not_allowed:
                    a+=char
            temp_not_allowed+=[a]
        removed.append(temp_not_allowed)
    return removed


def split_and_lower(file):
    """(file)->list
    returns a split and lowered list of lists that contain every word in every line in the file.
    Preconditions: none"""
    lst=[]
    for line in file:
        line=line.lower()
        add=line.split()
        lst+=[add]
    return lst


def remove_unneeded(lst):
    """(list)->none
    removes all the words in the list that contain non alphabetic characters
    Preconditions: none"""
    better=[]

    for line in lst:
        temp = []
        for word in line:
            if word.isalpha() and len(word) >= 2:
                temp.append(word)
        better.append(temp)
    return better


def make_dic(lst):
    """(list)->dict
    returns a dictionary with every word as a value in the list and every key as the number of line that the word is in.
    Preconditions: none"""
    dic = {}
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] not in dic:
                dic[lst[i][j]]={i+1}
            else:
                dic[lst[i][j]].add(i+1)
    return dic

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=""
while query!="q":
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query!="q" and query!="":
        LL=query.split()
        not_in=[]
        in_q=""
        for word in LL:
            ac=""
            for character in word:
                if character.isalnum():
                    ac+=character
            if ac not in d or len(ac)==0:
                not_in.append(ac)
            elif ac in d:
                in_q+=ac+" "
        in_q.strip().lower()
        if not_in!=[]:
            print("Word '"+not_in[0]+"' not in the file.")
        else:
            st=find_coexistance(d, in_q)
            a=""
            for char in st:
                a+=str(char)+" "
            print("The one or more words you entered coexisted in the following lines of the file:\n{}".format(a[0:-1]))