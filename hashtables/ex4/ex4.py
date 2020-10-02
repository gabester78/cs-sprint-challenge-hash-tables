# https://www.w3schools.com/python/ref_func_abs.asp

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    dict = {}
    result = []

    for i in a:
        if abs(i) not in dict:
            dict[abs(i)] = 0
        else:
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
