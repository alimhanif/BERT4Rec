from __future__ import print_function
import sys
import copy
import random
import numpy as np
from collections import defaultdict


def data_partition(fname):
    users = []
    items = []
    User = defaultdict(list)
    user_train = {}
    user_valid = {}
    user_test = {}
    # assume user/item index starting from 1
    f = open(fname, 'r')
    for line in f:
        u, i = line.rstrip().split(' ')
        u = int(u)
        i = int(i)
#         usernum = max(u, usernum) # not relevant in our case
#         itemnum = max(i, itemnum) # not relevant in our case
        User[u].append(i)
        users.append(u)
        items.append(i)

    users = set(users)
    items = set(items)
    usernum = len(users)
    itemnum = len(items)
    
    for user in User:
        # User[user] : items reviewed by that user
        nfeedback = len(User[user])
        if nfeedback < 3:
            user_train[user] = User[user]
            user_valid[user] = []
            user_test[user] = []
        else:
            user_train[user] = User[user][:-2] 
            user_valid[user] = []
            user_valid[user].append(User[user][-2])
            user_test[user] = []
            user_test[user].append(User[user][-1])
            
            # user_train : product review history
            # user_valid : second last product id
            # user_test : last product id
            # usernum : number of users
            # itemnum : number of users
            
    return [user_train, user_valid, user_test, usernum, itemnum]