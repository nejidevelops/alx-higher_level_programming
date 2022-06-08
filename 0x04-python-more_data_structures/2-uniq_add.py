#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    add_int = 0
    for i in new_set:
        add_int += i

    return add_int
