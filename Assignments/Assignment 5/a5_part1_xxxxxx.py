import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    file_name=None
    while file_name==None:
        try:
            file_name=input("Enter the name of the file: ").strip()
            f=open(file_name)
            f.close()
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
            file_name=None
    return open(file_name)
   

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    file = fp.read().splitlines()
    not_allowed = ",.'!-"

    dic={}

    temp2=[]
    temp=[]

    for line in file:
        line=line.lower()
        add=line.split()
        temp2+=[add]

    for line in temp2:
        temp_not_allowed = []
        for word in line:
            a=""
            for char in word:
                if char not in not_allowed:
                    a+=char
            temp_not_allowed+=[a]
        temp.append(temp_not_allowed)
    for line in temp:
        for word in line:
            if not word.isalpha() or len(word) < 2:
                line.remove(word)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] not in dic:
                dic[temp[i][j]]={i+1}
            else:
                dic[temp[i][j]].add(i+1)

    return dic


def find_coexistance(D, query):
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
        not_in=""
        for word in LL:
            if word not in d:
                not_in+=word+", "
        if not_in!="":
            print("Word '"+not_in[:-2]+"' not in the file.")
        else:
            st=find_coexistance(d, query)
            a=""
            for char in st:
                a+=str(char)+" "
            print(a[0:-1])
