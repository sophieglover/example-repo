# modify the merge sort algotirhm to order a list of strings by string length from the longest to the shortest string

def merge_sort(items):
    items_length = len(items)

    temporary_storage = [None] * items_length

    size_of_subsections = 1

    while size_of_subsections < items_length:
        for i in range(0, items_length, size_of_subsections * 2):
            first_section_start, first_section_end = i, min(i + size_of_subsections, items_length)

            second_section_start, second_section_end = first_section_end, min(first_section_end + size_of_subsections, items_length)

            sections = (first_section_start, first_section_end), (second_section_start, second_section_end)

            merge(items, sections, temporary_storage)

        size_of_subsections *= 2

    return items

def merge(items, sections, temporary_storage):
    (first_section_start, first_section_end), (second_section_start, second_section_end) = sections

    left_index = first_section_start
    right_index = second_section_start
    temp_index = 0

    while left_index < first_section_end or right_index < second_section_end:
        if left_index < first_section_end and right_index < second_section_end:
            if len(str(items[right_index])) < len(str(items[left_index])): #THIS IS WHERE I HAVE CHANGED IT 
                temporary_storage[temp_index] = items[left_index]
                left_index += 1

            else:
                temporary_storage[temp_index] = items[right_index]
                right_index += 1

            temp_index += 1

        elif left_index < first_section_end:
            for i in range(left_index, first_section_end):
                temporary_storage[temp_index] = items[left_index]
                left_index += 1
                temp_index += 1

        else:
            for i in range(right_index, second_section_end):
                temporary_storage[temp_index] = items[right_index]
                right_index += 1
                temp_index += 1

    for i in range(temp_index):
        items[first_section_start + i] = temporary_storage[i]


example_list1 = ["3300", "10", "590", "2600000", "410000", "58000", "1800000", "2102361575", "2", "9876543245678"]
example_list2 = ["Tyrannosaurus Rex", "Velociraptor", "Spinosaurus", "Brachiosaurus", "Diplodocus", "Triceratops", "Stegosaurus", "Allosaurus", "Alectrosaurus", "Pterodactylus"]
example_list3 = ["Bev", "Tim", "Sophie", "Aideen", "Marion", "Bridget", "Mark", "Dorje", "Marie", "Emma"]

sorted_list1 = merge_sort(example_list1)
sorted_list2 = merge_sort(example_list2)
sorted_list3 = merge_sort(example_list3)

print(sorted_list1)
print()
print(sorted_list2)
print()
print(sorted_list3)









