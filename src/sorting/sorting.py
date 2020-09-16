# TO-DO: complete the helper function below to merge 2 sorted arrays
"""
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    

    return merged_arr

"""
def merge(arrA, arrB):
    result = []
    i = 0
    j = 0

    while i<len(arrA) and j<len(arrB):
        if arrA[i] <= arrB[j]:
            result.append(arrA[i])
            i += 1
        else:
            result.append(arrB[j])
            j += 1
    
    #if any elements are remaining in the left array from
    #indice "i" to the end ":" of the array
    #then append it to the result list
    result += arrA[i:]
    #if any elements are remaining in the right array from
    #indice "j" to the end ":" of the array
    #then append it to the result list
    result += arrB[j:]
    return result


def merge_sort(arr):
    #if the arr is already sorted (1)
    #the return the arr
    if(len(arr) <= 1):
        return arr
    middle = int(len(arr)/2)
    arrA = merge_sort(arr[:middle])
    arrB = merge_sort(arr[middle:])
    return merge(arrA, arrB)

# TO-DO: implement the Merge Sort function below recursively
"""
def merge_sort(arr, left_index, right_index):
    # Your code here
    if left_index >= right_index:
        return
    
    #divide the sub-arrays into halves
    #until we end up with sub arrays with only one element
    middle = (left_index + right_index) // 2
    merge_sort(arr, left_index, middle)
    merge_sort(arr, middle + 1, right_index)
    merge(arr, left_index, right_index, middle)



    return arr
"""
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

