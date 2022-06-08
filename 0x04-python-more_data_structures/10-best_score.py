#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    biggest_key = list(a_dictionary.keys())[0]
    tmp = a_dictionary[biggest_key]
    for k, v in a_dictionary.items():
        if v > tmp:
            tmp = v
            biggest_key = k

    return (biggest_key)
