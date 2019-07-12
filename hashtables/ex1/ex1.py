#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Add all the weights to the hash table 
    # key is weight, value is index
    for k, v in enumerate(weights):
        hash_table_insert(ht, v, k)
    

    for k, v in enumerate(weights):
        difference = limit - v
        # Check to see if the difference is in the hash table
        if hash_table_retrieve(ht, difference) is not None:
            index = hash_table_retrieve(ht, difference)

            # returning them in order
            if index >= k:
                return [index, k]
            else:
                return [k, index]

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
