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
    ht = HashTable(length)
    route = [None] * length
     

    for t in tickets:
        hash_table_insert(ht, t.source, t.destination)

    current = hash_table_retrieve(ht, "NONE")
    
    while current != "NONE": 
        for i in range(len(route)):
            route[i] = current
            current = hash_table_retrieve(ht, current)
            if current == "NONE":
                route[i+1] = current
                break
    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))