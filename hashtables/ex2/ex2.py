#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    dict = {}

    # loop through all the tickets
    for i in tickets:

        # link source to destination
        dict[i.source] = i.destination

    route = []

    # add destination of none to last ticket
    next = dict["NONE"]
    route.append(next)

    # loop through the number of tickets
    for i in range(0, length):

        # add none to the starting point route
        next = dict[next]

        # add none to the end of route
        route.append(next)
        if next == "NONE":
            break

    return route
