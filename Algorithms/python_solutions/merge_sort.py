def merge(array_one, array_two):
    """
    """
    length_array_one = len(array_one)
    length_array_two = len(array_two)
    index_for_array_one = 0
    index_for_array_two = 0
    merged_array = \
        [0 for _ in range(len(array_one) + len(array_two))]

    # end for both is not reached
    while (index_for_array_one + index_for_array_two <
           length_array_one + length_array_two):

        # move forward in the array one if

        # end for the second is reached or
        # we can (end for the first is not reached)
        # and need to move forward inside array one
        # (i-th element from the first
        # less than j-th element from the second)
        if (index_for_array_two == length_array_two or
           (index_for_array_one < length_array_one and
                array_one[index_for_array_one] <
                array_two[index_for_array_two])):

            # append to c an element from the first
            merged_array[index_for_array_one + index_for_array_two] = \
                array_one[index_for_array_one]
            index_for_array_one += 1

        # end for the first is reached but not for the second
        # or bpth ends are not reached and element from array two
        # less than element from array one
        else:

            # append to c an element from the second
            merged_array[index_for_array_one + index_for_array_two] = \
                array_two[index_for_array_two]
            index_for_array_two += 1
    del array_one
    del array_two
    return merged_array


def merge_sort(array):
    '''
        Divide and conquer
        Divide on 2 parts
        Sort them using recursive func
        Merge them into one
        o(nlogn)
    '''
    length_array = len(array)
    if (length_array == 1):
        return array
    left_part_of_array = array[:round(length_array / 2)]
    # print('l=',l)
    right_part_of_array = array[round(length_array / 2):length_array]
    # print('r=',r)
    left_part_of_array = merge_sort(left_part_of_array)
    right_part_of_array = merge_sort(right_part_of_array)
    return merge(left_part_of_array, right_part_of_array)
