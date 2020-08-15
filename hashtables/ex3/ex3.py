def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {} # hash table for number and count
    result = [] # lists of intersection


    for k in arrays: # for each list in array
        for v in k: # for each element in list
            if v not in ht: # if not in hash table
                ht[v] = 1 # add to hash table
            else:
                ht[v] += 1 # increase count
            # print(ht[v])
            if ht[v] == len(arrays): # if hashtable value equals number in array
                result.append(v) # add value to result
                # print(result)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
