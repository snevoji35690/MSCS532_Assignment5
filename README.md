## MSCS532_Assignment5
## Randomized Quicksort & Empirical Analysis
This project implements two versions of the Quicksort algorithm:

Deterministic Quicksort: A traditional version of Quicksort where the pivot is chosen as the last element of the array.

Randomized Quicksort: An optimized version where the pivot is selected randomly to prevent poor performance on sorted or patterned input.

Additionally, this project includes an Empirical Analysis to compare the performance of both algorithms across different input sizes and distributions (random, sorted, and reverse-sorted arrays).

## How to Run the Code
Requirements
Python 3.6 or higher

No external libraries are required (uses built-in Python libraries)

## File Structure
nginx
Copy
MSCS532_Assignment5
├── quicksort_algorithm.py   # Implementation of deterministic and randomized Quicksort algorithms with empirical analysis
├── README.md                # Project documentation
Run the Code
Clone the repository or download the project files from the GitHub repository.

To clone the repository:

Copy
git clone https://github.com/snevoji35690/MSCS532_Assignment5.git
cd MSCS532_Assignment5
## Run the Quicksort Algorithm:

You can test both the Deterministic Quicksort and Randomized Quicksort algorithms by running the script

### Empirical Analysis:

To run the Empirical Analysis and compare the execution times of Deterministic and Randomized Quicksort on different input sizes (100, 1000, 10000, and 50000), run
The results will include the time taken by both algorithms on random, sorted, and reverse-sorted arrays, as well as the first 10 elements of the sorted arrays for reference.

### Summary of Findings
Deterministic Quicksort
Time Complexity:
Best Case: 𝑂(𝑛log𝑛)
Average Case: 𝑂(𝑛log𝑛)
Worst Case: 𝑂(𝑛2)
when the pivot results in highly unbalanced partitions (e.g., sorted or reverse-sorted arrays).

Performance: Works well with random input, but can degrade to O(n2) 
if the input is already sorted or reverse-sorted, leading to unbalanced partitions.

## Randomized Quicksort
Time Complexity:
Best Case: O(nlogn)
Average Case: O(nlogn)
Worst Case: O(n2) 
(although the likelihood is reduced by the random pivot selection).

Performance: Random pivot selection helps avoid the worst-case O(n2) 
scenario and ensures more balanced partitions. The expected time complexity remains O(nlogn) for most inputs.

## Empirical Comparison
The empirical analysis tests both Quicksort algorithms on three types of input distributions:

Random arrays (elements are randomly shuffled)

Sorted arrays (elements in ascending order)

Reverse-sorted arrays (elements in descending order)
