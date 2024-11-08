import random
import time

def quicksort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort_deterministic(left) + [pivot] + quicksort_deterministic(right)

def quicksort_randomized(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_randomized(left) + middle + quicksort_randomized(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = [random.randint(0, 10000) for _ in range(n)]
    
    print(f"Original array (first 10 elements): {arr[:10]} ...")
    
    det_time = measure_time(quicksort_deterministic, arr.copy())
    print(f"Time taken by Deterministic Quick Sort: {det_time:.6f} seconds")
    
    rand_time = measure_time(quicksort_randomized, arr.copy())
    print(f"Time taken by Randomized Quick Sort: {rand_time:.6f} seconds")
