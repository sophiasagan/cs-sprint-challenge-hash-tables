#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tock_tickets = {} # ht for tickets

    # loop through tickets
    for ticket in tickets:
        # set source as key and dest as value
        tock_tickets[ticket.source] = ticket.destination
    
    # recreate trip route
    route = [tock_tickets["NONE"]] # starting location

    # find and add next location
    for i in range(1, length): #for each ticket in list
        route.append(tock_tickets[route[i-1]]) # add to route based on previous dest

    return route




ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))