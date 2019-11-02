#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Returns a tuple of indices that indicate the placement of the 2 values that sum up to a specified limit
    """
    for index in range(length):
        # find what number is needed to make the match based on current index locations value
        difference_needed = limit - weights[index]
        # grab current value from hashtable
        found_match = hash_table_retrieve(ht, difference_needed)
        # if no found match yet, build up the hashtable
        if found_match is None:
            hash_table_insert(ht, weights[index], index)
        else:
            # else return the tuple with the current index (the highest one) first
            return (index, found_match)
        # print(f"difference_needed: {difference_needed}...found_match: {found_match}")
    # If no matches are found, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
