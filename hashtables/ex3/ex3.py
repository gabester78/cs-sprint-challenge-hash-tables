def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}
    result = []

    # loop though arrays
    for i in arrays:

        # loop through each element in each array and
        # add it to the dict if not included already
        for j in i:
            if j not in dict:
                dict[j] = 0
            else:
                dict[j] += 1

    # compare if any values in dict match last element seen and add it to the results
    for key, value in dict.items():
        if value == len(arrays)-1:
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
