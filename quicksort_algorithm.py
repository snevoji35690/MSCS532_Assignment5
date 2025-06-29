def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x < pivot]
    greater_than_or_equal_pivot = [x for x in arr[:-1] if x >= pivot]
    
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_or_equal_pivot)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print(f"Sorted array: {sorted_arr}")


#Randomized Quicksort
import random

def randomized_quicksort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    pivot_index = random.randint(0, len(arr) - 1)
    
    # Swap the chosen pivot with the last element
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
    
    # Pivot is now the last element, so partition the array
    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x < pivot]
    greater_than_or_equal_pivot = [x for x in arr[:-1] if x >= pivot]
    
    # Recursively apply quicksort on the two subarrays
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_or_equal_pivot)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = randomized_quicksort(arr)
print(f"Sorted array: {sorted_arr}")


# Emperical Analysis
import random
import time

# Deterministic Quicksort (Last element as pivot)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x < pivot]
    greater_than_or_equal_pivot = [x for x in arr[:-1] if x >= pivot]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_or_equal_pivot)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
    pivot = arr[-1]
    less_than_pivot = [x for x in arr[:-1] if x < pivot]
    greater_than_or_equal_pivot = [x for x in arr[:-1] if x >= pivot]
    return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_or_equal_pivot)

# Function to test both algorithms on different input distributions
def test_quicksort_algorithms(input_size):
    # Random array
    random_arr = [random.randint(1, 10000) for _ in range(input_size)]
    
    # Sorted array
    sorted_arr = sorted(random_arr)
    
    # Reverse sorted array
    reverse_sorted_arr = sorted_arr[::-1]
    
    # Test deterministic Quicksort on random array
    start_time = time.time()
    quicksort(random_arr[:])  # Create a copy to avoid in-place sorting
    deterministic_time = time.time() - start_time

    # Test randomized Quicksort on random array
    start_time = time.time()
    randomized_quicksort(random_arr[:])  # Create a copy to avoid in-place sorting
    randomized_time = time.time() - start_time

    return deterministic_time, randomized_time, sorted_arr, reverse_sorted_arr

# Testing on different input sizes and distributions
input_sizes = [100, 1000, 10000, 50000]
results = {}

for size in input_sizes:
    deterministic_time, randomized_time, sorted_arr, reverse_sorted_arr = test_quicksort_algorithms(size)
    results[size] = {
        'deterministic_time': deterministic_time,
        'randomized_time': randomized_time,
        'sorted': sorted_arr[:10],  # Only show first 10 elements for brevity
        'reverse_sorted': reverse_sorted_arr[:10],  # Only show first 10 elements for brevity
    }

for size, data in results.items():
    print(f"Input Size: {size}")
    print(f"Deterministic Quicksort Time: {data['deterministic_time']:.6f} seconds")
    print(f"Randomized Quicksort Time: {data['randomized_time']:.6f} seconds")
    print(f"First 10 elements of sorted array: {data['sorted']}")
    print(f"First 10 elements of reverse sorted array: {data['reverse_sorted']}")
    print("-" * 50)
