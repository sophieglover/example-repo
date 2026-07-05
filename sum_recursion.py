def sum_function(integer_list, single_integer):
    
    if single_integer == 0:
        return integer_list[0]

    else:
        return integer_list[single_integer] + sum_function(integer_list, single_integer - 1)


print(sum_function([1, 2, 4, 8], 3))
