def largest_number(integer_list):

    if len(integer_list) == 1:
        return integer_list[0]

    else:
        number = integer_list[0]

        other_numbers = largest_number(integer_list[1:])

        if number > other_numbers:
            return number

        elif number < other_numbers:
            return other_numbers


print(largest_number([1, 10, 15, 100]))


