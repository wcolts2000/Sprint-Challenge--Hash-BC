#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    # build the list to store the strings linking the stops
    route = [None] * length

    """
    Takes a list of Ticket objects and a length and returns a new 
    list of strings with the stops of the trip in order based on 
    the given source and destinations on the Ticket objects
    """


    # build an object with the `key` being the Tickets source and the `value` being the Tickets destination
    for ticket in tickets:
        print(f"Ticket: src = {ticket.source}, dest = {ticket.destination}")
        # denote the start ticket based on None values in the source
        if ticket.source == "NONE":
            # print(f"found start: {ticket.source}: {ticket.destination}")
            # insert starting ticket in beginning of result list
            route[0] = ticket.destination
        # otherwise insert ticket info into hashtable
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        
    # print(hashtable.storage)
    # use hashtable to build result list based on value from the starting ticket
    # start at index 1 as the first ticket is already placed
    for index in range(1, length):
        route[index] = hash_table_retrieve(hashtable, route[index-1])
    
    print(f"Route: {route}")
    return route
