# use the following list: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def sequential_search(target, items):
    for index in range(len(items)):
        if items[index] == target:
            return index

    return None

items_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_item = 9
result = sequential_search(target_item, items_list)

if result is not None:
    print(f"Item {target_item} found at index {result}.")

else:
    print(f"Item {target_item} not found in the list.") 

# I used the sequential search algorithm (aka linear search)to find the number 9, since the elements in the list are not in order and we know which element we intend to find


# implementing the insertion sort:

def insertion_sort(list):
    
    for i in range(1, len(list)):

        for j in range(i, 0, -1):

            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]

            else:
                break

    return list

sorted_list = insertion_sort(items_list)
print()
print(sorted_list)

# implementing binary search

def binary_search(target,items):
    low, high = 0, len(items) - 1

    while high >= low:

        mid = (low + high) // 2

        if items[mid] == target:
            return mid

        elif items[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None

binary_result = binary_search(target_item, sorted_list)

print()

if result is not None:
    print(f"Item {target_item} found at index {binary_result}.")
else:
    print(f"Item {target_item} not found in the list.")

# In the real world we would use the binary search algorithm to locate a specific item in a sorted list, for example a name in a list of contacts, or a word in a dictionary - both ordered alphabetically





















    
    