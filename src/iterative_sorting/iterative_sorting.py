# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if smallest_index != cur_index:
            to_shift = arr[smallest_index]
            arr.pop(smallest_index)
            arr.insert(cur_index, to_shift)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    reset = True
    while reset == True:
        reset = False
        for i in range(0, len(arr) - 1):
            cur_index = i
            next_index = i + 1
            if arr[cur_index] > arr[next_index]:
                reset = True
                to_shift = arr[next_index]
                arr.pop(next_index)
                arr.insert(cur_index, to_shift)

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # edge case: check for negative numbers
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"

    # find maximum if none provided
    if maximum == -1:
        maximum = 0
        for i in range(0, len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]

    # set count array
    count_arr = []

    # iterate each num in range through original array, keeping track 
    # of frequency in count array
    for i in range(0, maximum + 1):
        cur_int = i
        int_count = 0
        for j in range(0, len(arr)):
            if arr[j] == cur_int:
                int_count += 1
        count_arr.append(int_count)

    # create sorted array based off frequencies
    sorted_arr = []
    for i in range(0, maximum + 1):
        if count_arr[i] > 0:
            for j in range(0, count_arr[i]):
                sorted_arr.append(i)

    return sorted_arr

def better_insertion_sort( arr ):
    # print("ORIGINAL ARRAY:", arr)
    def sort_check(arr, index, value):
        if arr[index] == value:
            # print(f"### VALUE {value} IS EQUAL TO {arr[index]} ###")
            return index
        elif arr[index] > value:
            if index == 0:
                # print(f"### VALUE {value} IS SMALLEST IN {arr} ###")
                return 0
            else:
                # print(f"### VALUE {value} IS SMALLER THAN {arr[index]} ###")
                return "lower"
        elif arr[index] < value:
            if index == len(arr) - 1:
                # print(f"### VALUE {value} IS LARGEST IN {arr} ###")
                return index + 1
            else:
                # print(f"### VALUE {value} IS LARGER THAN {arr[index]} ###")
                return "upper"
        else:
            return "error"

    # edge case: single item or empty arrays
    if len(arr) < 2:
        # print("\n####### SORT COMPLETE (SMALL ARRAY) #######\n\n")
        return arr

    for i in range(0, len(arr) - 1):
        cur_index = i
        next_index = i + 1
        # print("\nSORTING INDEX:", next_index)
        # print("VALUE:", arr[next_index])
        sorted_array = arr[0 : cur_index + 1]
        actual_array_index = 0
        # print("SORTED ARRAY:", sorted_array)
        midpoint = int((cur_index + 1) / 2)
        lower = arr[0 : midpoint]
        upper = arr[midpoint : cur_index + 1]
        continue_sort = True
        while continue_sort == True:
            result = sort_check(sorted_array, midpoint, arr[next_index])
            try:
                int(result)
                to_shift = arr[next_index]
                arr.pop(next_index)
                arr.insert(result + actual_array_index, to_shift)
                # print("PLACED AT INDEX:", result)
                # print("NEW ARRAY:", arr)
                continue_sort = False
            except:
                if result == "upper":
                    sorted_array = upper
                    actual_array_index += len(lower)
                    midpoint = int((len(upper)) / 2)
                    lower = sorted_array[0 : midpoint]
                    upper = sorted_array[midpoint : len(upper)]
                elif result == "lower":
                    sorted_array = lower
                    midpoint = int((len(lower)) / 2)
                    lower = sorted_array[0 : midpoint]
                    upper = sorted_array[midpoint : len(upper)]
                else:
                    return "error"
    # print("\n####### SORT COMPLETE #######\n\n")
    return arr
