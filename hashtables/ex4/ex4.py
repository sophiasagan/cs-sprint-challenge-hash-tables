import math

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {} # hash table for numbers and count
    result = [] # list of results

    # loop through the array
    for num in a:
        num = abs(num) # convert all numbers to positive
        if num in ht: # if number in hash table 
            ht[num] += 1 # add to count
            if ht[num] > 1: # if hash table count
                result.append(num) # number to results
                # print(ht)
                # print(result)
        else:
            ht[num] = 1 # add to hash table

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
