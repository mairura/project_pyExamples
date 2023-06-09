from collections import Counter


def count_occurrences(my_list):
    counts = {}
    for item in my_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


my_list = [4, 3, 2, 1, 3, 1, 2, 3, 1, 4, 4, 2, 1, 4]
print(count_occurrences(my_list))

# Using collections mode
def count_occurrences(my_list):
    return Counter(my_list)


my_list = [4, 3, 2, 1, 3, 1, 2, 3, 1, 4, 4, 2, 1, 4]
print(count_occurrences(my_list))

# Using count mode
def count_occurrences(my_list):
	return {x:my_list.count(x) for x in set(my_list)}
my_list = [4,3,2,1,3,1,2,3,1,4, 4,2,1, 4]
print(count_occurrences(my_list))

#using bincount() method
import numpy as np
def count_occurrences(my_list):
	return dict(zip(np.unique(my_list),np.bincount(my_list)))
my_list = [4,3,2,1,3,1,2,3,1,4, 4,2,1, 4]
print(count_occurrences(my_list))
