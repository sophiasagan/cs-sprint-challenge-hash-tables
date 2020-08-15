# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {} # ht for filepath(v) and word(k)
    result = [] # list for results

    # loop - doesn't pass large test
    # for i in files:
    #     txt_filepath = ht[i.split("/")[-1]] = i # split each filepath by backslash store last string/word in ht index
    #     # print(ht)

    # for j in queries:
    #     if j in ht: # if word in query match word in ht
    #         result.append(ht[j]) # add filepath to result


    # loop through files
    for i in files:
        split_txt = i.split("/")[1:] # split filepath by / ignoring the "" 
        # print(split_txt)
        for j in split_txt: # for texts in split filepath
            if j not in ht: # if not in hash table
                ht[j] = i # add to hash table

    for k, v in ht.items(): # for key values in hash table
        # print(ht)
        if k in queries: # if key(word) in queries
            result.append(v) # add value(filepath) to result

    return result

# minimized from large test: 
files = []

for i in range(50):
    files.append(f"/dir{i}/file{i}")

for i in range(50):
    files.append(f"/dir{i}/dirb{i}/file{i}")

queries = []

for i in range(100):
    queries.append(f"nofile{i}")

queries += [
    "file3",
    "file2",
    "file9",
    "file8"
]

print(finder(files, queries))

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "bar"
    ]
    print(finder(files, queries))
