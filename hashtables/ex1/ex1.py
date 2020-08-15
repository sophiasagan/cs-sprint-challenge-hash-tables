def get_indices_of_item_weights(weights, length, limit):
    # Your code here
    ht = {} # hash table for weights and indices

    # loop/iterate through list of weights
    for i in range(length):
        if weights[i] not in ht: # not in hash table
            ht[weights[i]] = i # store in hash table
        else:
            if limit - weights[i] == weights[i]: # if current weight equals limit
                return (i, ht[weights[i]]) # return curr index and stored index

        weight_diff = limit - weights[i] # calc weight difference needed to complete limit

        if weight_diff in ht and weight_diff != weights[i]: # if weight difference does not equal itself
            return sorted((ht[weight_diff], ht[weights[i]]), reverse=True) # return indices of weights, reversed to account for larger index being first

    return None # no solution found


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
