# List Sorting - Selection Sort
This repository contains a Python code file, Selection_sorting.py, which implements the selection sort algorithm to sort a list of numbers in ascending order.

# How it works
The selection sort algorithm works by dividing the input list into two parts: the sorted portion and the unsorted portion. The sorted portion starts as an empty list, while the unsorted portion contains all the elements. The algorithm repeatedly selects the minimum element from the unsorted portion and moves it to the end of the sorted portion. This process continues until the entire list is sorted.

Here's a brief explanation of the algorithm:

The main function, selection_sort, takes a list of numbers as input.
The function iterates through the list, starting from the first element.
For each iteration, it finds the minimum element in the remaining unsorted portion of the list.
The minimum element is then swapped with the current element, effectively moving it to the end of the sorted portion.
The process continues until the entire list is sorted in ascending order.
Usage
To use this code, you need to have Python installed on your system. Follow these steps to run the code:

Clone the repository or download the Selection_sorting.py file.

Open a terminal or command prompt and navigate to the directory where the file is located.

Run the following command:

# bash
Copy code
python Selection_sorting.py
The code will generate a random list of numbers and display the original unsorted list.

It will then apply the selection sort algorithm to sort the list in ascending order and display the sorted list.

Example
Here's an example run of the code:

less
# Copy code
Original list: [64, 34, 25, 12, 22, 11, 90]
Sorted list: [11, 12, 22, 25, 34, 64, 90]
# Limitations
It's important to note that the code is designed to sort a list of numbers. If the input list contains non-numeric elements, the code may raise an error. Additionally, the code implements the selection sort algorithm, which has a time complexity of O(n^2). For large lists, more efficient sorting algorithms like merge sort or quicksort may be preferable.

# Contributing
Contributions to this code are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# License
This code is licensed under the MIT License. Feel free to use and modify it as per the terms of the license.

# Acknowledgments
This code was created by @Eddy Kubwimana.
