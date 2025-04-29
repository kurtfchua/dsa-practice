def insertion_sort(arr):
    # iterate through array with 2 pointers i and j
    # i will hold the next elem to be sorted and j will hold the last sorted elem
    # j + 1 is the next element to be checked
    # if j+1 < j we swap j+1 and j until j >= j +1
    for i in range(len(arr)):
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            j-=1
        
    return arr

def merge_sort(arr):
    # we recursively break down the list in half until we get subarrays with size 1
    # on the collapse of the call stack we merge the 2 lists comparing their values

    # if list is size 1 or empty we return list
    if len(arr) <= 1: return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    
    return merge(left, right)

def merge(arr1, arr2):
    result = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result

def quick_sort(arr, start, end):
    # recursively partition array comparing it to a pivot
    # if element is < pivot we swap it with an element greater than pivot to its left
    # continue until we get to pivot
    # call until we get to sub lists of 1 

    # base case
    if start >= end:
        return arr
    
    # partition step
    pivot = arr[end] # choose pivot
    j = start # swap pointer
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    # swap pivot to end of left partition
    arr[j], arr[end] = pivot, arr[j]

    # recursive calls on left and right partitions
    quick_sort(arr, start, j-1) # left partition
    quick_sort(arr, j+1, end) # right partition

    return arr

def bucket_sort(arr):
    # define counts list with known values of arr as index
    # update counts in index with how many times we come across arr[n]
    # overwrite original list while iterating through counts list
    
    counts = [0,0,0] # 0,1,2 as known values in arr
    
    for n in arr:
        counts[n] += 1
    
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    
    return arr


l1 = [2,3,4,1,6]
l2 = [2,3,4,1,6]
#print(insertion_sort(l1))c
#print(merge_sort(l2))

l3 = [6,2,4,1,3]
#print(quick_sort(l3, 0 , len(l3)-1))
#print(l3)
l4 = [2,1,2,0,0,2]
l5 = [0,2,2,1,1,0,0,1,2,1,1,1,0,0,0,2]
print(bucket_sort(l4))
print(bucket_sort(l5))