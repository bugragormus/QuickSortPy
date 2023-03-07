import random
import time

# Generating Random Array
arr = [random.randint(0, 1000) for i in range(10000)]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# Sorting With QuickSort
start_time = time.time()
sorted_arr = quicksort(arr)
end_time = time.time()


# ***********************************************************************

def brute_force_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# Sorting With Brute Force
start_time1 = time.time()
sorted_arr1 = brute_force_sort(arr)
end_time1 = time.time()

print("QuickSort:", end_time - start_time, "Second")

print("*" * 40)

print("BruteForce:", end_time1 - start_time1, "Second")
