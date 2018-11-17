import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friends is sorted).
    '''
    friends = open(file_name).read().splitlines()
    friends.pop(0)
    network=[]
    unfinished_net = []

    for i in range(len(friends)):
        con = friends[i].split(" ")
        connection=[int(con[0]), int(con[1])]
        unfinished_net.append(connection)

    unfinished_net.sort()


    for i in range(len(unfinished_net)):
        reversal=[int(unfinished_net[i][1]), int(unfinished_net[i][0])]
        if reversal not in unfinished_net:
            unfinished_net.append(reversal)

    unfinished_net.sort()

    c=1
    i=1




    while c <= len(unfinished_net):
        mini_list=[]
        lc=c
        while c<=len(unfinished_net)-1 and unfinished_net[c][0]==unfinished_net[c-1][0]:
            c+=1
        for j in range(lc-1, c):
                mini_list.append(unfinished_net[j][1])

        network.append((unfinished_net[c-1][0], mini_list))
        c += 1

    return network


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    id1=id_search(user1, network)
    id2=id_search(user2, network)

    u1=network[id1][1]
    u2=network[id2][1]

    for element in u1:
        if element in u2:
            common.append(element)

    return common


def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.

    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    max=0
    max_ele=None
    copy=network.copy()
    idu=id_search(user, network)
    personal_list=network[idu][1]
    copy.pop(idu)
    for element in copy:
        common_list=[]
        for friend in element[1]:
            if friend in personal_list and element[0] not in personal_list:
                common_list.append(friend)
        if len(common_list)>max:
            max=len(common_list)
            max_ele=element[0]
    return max_ele

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    c=0
    for element in network:
        if len(element[1])>=k:
            c+=1
    return c
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    max=0

    for element in network:
        if len(element[1])>max:
            max=len(element[1])
    return max
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    max = 0

    for element in network:
        if len(element[1]) > max:
            max = len(element[1])

    for element in network:
        if len(element[1])==max:
            max_friends.append(element[0])
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    number_of_users=len(network)
    c=0
    for element in network:
        c+=len(element[1])
    return c/number_of_users
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    for element in network:
        if len(element[1])==len(network)-1:
            return True
    return False

def id_search(value, net):
    """
    (int, 2Dlist)->int
    Returns the index number of the user ID requested using a simply binary search method.
    Preconditions: none
    """
    s=0
    e=len(net)-1
    avg = (s + e) // 2
    while s<=e:
        if value>net[avg][0]:
            s=avg+1
        elif value<net[avg][0]:
            e=avg-1
        else:
            return avg
        avg = (s + e) // 2
    return -1

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    ind=-1

    while ind==-1:
        user_id=input("Enter an integer for a user ID: ").strip()

        try:
            ind=id_search(int(user_id), network)
        except(ValueError):
            print("That was not an integer. Try again.")

        if ind==-1 and user_id[1:].isdigit():
            print("That user ID does not exist. Try again.")

    return ind




##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name = get_file_name()

net = create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is " + str(
    maximum_num_friends(net)) + ".")
print("The average number of friends is " + str(average_num_friends(net)) + ".")
mf = people_with_most_friends(net)
print("There are", len(mf), "people with " + str(maximum_num_friends(net)) + " friends and here are their IDs:",
      end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k = random.randint(0, len(net) // 4)
print("\nThat number is: " + str(k) + ". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net, k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid = get_uid(net)
rec = recommend(uid, net)
if rec == None:
    print("We have nobody to recommend for user with ID", uid,
          "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid, "we recommend the user with ID", rec)
    print("That is because users", uid, "and", rec, "have", len(getCommonFriends(uid, rec, net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1 = get_uid(net)
print("About 2st user ...")
uid2 = get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common = getCommonFriends(uid1, uid2, net)
for item in common:
    print(item, end=" ")



