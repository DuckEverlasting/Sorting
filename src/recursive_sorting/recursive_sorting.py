import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    while len(arrA) or len(arrB):
        if not len(arrA):
            merged_arr.extend(arrB)
            arrB = []
        if not len(arrB):
            merged_arr.extend(arrA)
            arrA = []
        else:
            merged_arr.append(arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0))
            
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort_old( arr ):
    # edge case: empty array
    if len(arr) < 2:
        return arr

    # simple breakdown of array
    arr = [[i] for i in arr]
    
    # While loop of merge function.
    # Divides array into pairs of arrays, then merges the pairs, 
    # then adds on the final unpaired array if it exists.
    while len(arr) > 1:
        new_arr = []
        for i in (j for j in range(len(arr) - 1) if j % 2 == 0):
            new_arr.append(merge(arr[i], arr[i + 1]))
        if len(arr) % 2 == 1:
            new_arr.append(arr[len(arr) - 1])
        arr = new_arr

    # reformats array for return
    arr = arr[0]
    return arr

def merge_sort( arr ):
    # don't modify empty arrays or arrays with length 1
    if len(arr) < 2:
        return arr

    # find midpoint
    mid = int(len(arr) / 2)

    # split array (and keep splitting until done)
    arr = [merge_sort(arr[:mid]), merge_sort(arr[mid:])]

    # rejoin arrays
    if isinstance(arr[0], list):
        return merge(arr[0], arr[1])

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    for i in range(start, end):
        if not mid - start or not end - mid:
            break
        else:
            if arr[i] <= arr[i + (mid - start)]:
                end -= 1
                mid -= 1
            else:
                arr.insert(i, arr[i + (mid - start)])
                arr.pop(i + (mid - start) + 1)
                end -= 1
    return arr


def merge_sort_in_place(arr, l, r): 
    # correction for... differing opinions on what r should represent 😜
    r += 1

    # don't modify empty selections or selections with length 1
    if r - l < 2:
        return arr

    # find number of iterations, then iterate (iterations = int(math.log(r - l)/math.log(2)))
    for i in range(int(math.log(r - l)/math.log(2))):
        i = 2 ** (i + 1)
        for j in (k for k in range(r - l) if k % i == 0):
            if l + j + i <= r:
                merge_in_place(
                    arr = arr,
                    start = l + j,
                    mid = l + j + int(i / 2),
                    end = l + j + i
                )

    # handle remainder
    if (r - l) % i != 0:
        merge_sort_in_place(arr, r - ((r - l) % i), r - 1)
        merge_in_place(
            arr = arr,
            start = l,
            mid = r - ((r - l) % i),
            end = r
        )

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
