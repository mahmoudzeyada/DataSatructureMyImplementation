def binary_search(input_array, value):
    input_array.sort()
    #import pdb; pdb.set_trace()
    pointer = 0
    max = len(input_array)-1
    min = 0
    while min <= max:
        pointer = (max+min)/2
        if input_array[pointer] == value:
            return pointer
        elif input_array[pointer] < value:
            min = pointer+1
        elif input_array[pointer] > value:
            max = pointer-1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 30]
test_val1 = 3
#test_val2 =3
print binary_search(test_list, test_val1)
# print binary_search(test_list, test_val2)
