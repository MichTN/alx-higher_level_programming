#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_two = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list_two):
        return my_list
    my_list_two[idx] = element:
        return my_list_two
