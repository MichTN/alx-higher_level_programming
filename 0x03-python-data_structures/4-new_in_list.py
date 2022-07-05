def new_in_list(my_list, idx, element):
    my_list_two = my_list.copy()
    if idx < 0:
        return my_list_two
    if idx >= len(my_list_two):
        return my_list_two
    for my_list_two[idx] = element:
        return my_list_two
