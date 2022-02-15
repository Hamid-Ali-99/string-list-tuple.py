# -*- coding: utf-8 -*-
"""Hamid-Ali-01.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XB7sLIMeX6XvtOQbAAHJ7HfAEbepySE1
"""

print("Asslam o Alikum Pakistan")

"""**Linear Search:**
* Linear search is a sequential searching algorithm where we start from one end and check every element of the list until the desired element is found. It is the simplest searching algorithm.

**Code:**
# Linear Search in Python

def linearSearch(array, n, x):
    #This code is copyed from the internet.
    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)


**Linear Search Complexities**

* Time Complexity: O(n)

* Space Complexity: O(1)

**Binary Search:**

https://www.programiz.com/dsa/binary-search

* A Python binary search is an algorithm that finds the position of an element in an ordered array. Binary searches repeatedly divide a list into two halves. Then, a search compares if a value is higher or lower than the middle value in the list.

**Code:**
# Binary Search in python
       #This Code is Copyed From the Internet.

def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


**Time Complexities**

* Best case complexity: O(1)

* Average case complexity: O(log n)

* Worst case complexity: O(log n)

**Space Complexity**

* The space complexity of the binary search is O(1).

***Bubble Sort***

* Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.

**Code:**
* # Bubble sort in Python
# This code is copyed from internet.

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')

print(data)

**Time Complexities**

* **Worst Case Complexity: O(n2)**

 If we want to sort in ascending order and the array is in descending order then the worst case occurs.

* **Best Case Complexity: O(n)**

 If the array is already sorted, then there is no need for sorting.

* **Average Case Complexity: O(n2)**

 It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

**Space Complexity**

* Space complexity is O(1) because an extra variable is used for swapping.
In the optimized bubble sort algorithm, two extra variables are used. Hence, the space complexity will be O(2).


**Bubble Sort Applications**

* Bubble sort is used if

* complexity does not matter

* short and simple code is preferred

**Selection Sort Algorithm**

https://www.programiz.com/dsa/selection-sort

* Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

**Working:**

* Set the first element as minimum.

* Compare minimum with the second element. If the second element is smaller than minimum, assign the second element as minimum.

* Compare minimum with the third element. Again, if the third element is smaller, then assign minimum to the third element otherwise do nothing. The process goes on until the last element.

* After each iteration, minimum is placed in the front of the unsorted list.

* For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.

**Code:**

* # Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
    this code is copyed from the internet or from above link.
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

**Time Complexities:**

* **Worst Case Complexity: O(n2)**

 If we want to sort in ascending order and the array is in descending order then, the worst case occurs.

* **Best Case Complexity: O(n2)**

 It occurs when the array is already sorted

* **Average Case Complexity: O(n2)**

 It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

**Space Complexity:**

* Space complexity is O(1) because an extra variable temp is used.



**Selection Sort Applications**

* The selection sort is used when

* a small list is to be sorted

* cost of swapping does not matter

* checking of all the elements is compulsory

cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)

**Insertion Sort Algorithm**

https://www.programiz.com/dsa/insertion-sort

* **Insertion sort** is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

* Insertion sort works similarly as we sort cards in our hand in a card game.

* We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left. In the same way, other unsorted cards are taken and put in their right place.

A similar approach is used by insertion sort.

**Working:**
⚙⚙⚙⚙


* The first element in the array is assumed to be sorted. Take the 
second element and store it separately in key.
Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.

* Now, the first two elements are sorted.
Take the third element and compare it with the elements on the left of it. Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.
* Similarly, place every unsorted element at its correct position.

**Code:**

# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an 
        
        element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]

insertionSort(data)

print('Sorted Array in Ascending Order:')

print(data)


**Time Complexities**

* **Worst Case Complexity: O(n2)**

 If we want to sort in ascending order and the array is in descending order then the worst case occurs.

* **Best Case Complexity: O(n)**

 If the array is already sorted, then there is no need for sorting.

* **Average Case Complexity: O(n2)**

 It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

**Space Complexity**

* Space complexity is O(1) because an extra variable is used for swapping.
* In the optimized bubble sort algorithm, two extra variables are used. Hence, the space complexity will be O(2).

**Merge Sort Algorithm:**

https://www.programiz.com/dsa/merge-sort

* Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.

*** Divide and Conquer Strategy**

 Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.

Suppose we had to sort an array A. A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].

* **Divide:**
 
 If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r].

* **Conquer:**

 In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

* **Combine:**

 When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].


***Code:**

 


def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)




**Time Complexity:**
* Best Case Complexity: O(n*log n)

* Worst Case Complexity: O(n*log n)

* Average Case Complexity: O(n*log n)

**Space Complexity**

* The space complexity of merge sort is O(n).


**Merge Sort Applications**
* Inversion count problem
* External sorting
* E-commerce applications

😀 😈 😺

**Fabonacci Series Generators**
* https://www.programiz.com/python-programming/examples/fibonacci-sequence Source Link:

* A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

 The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.

**Code:**
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1




**OutPut**
* How many terms? 7
* Fibonacci sequence:

0
1
1
2
3
5
8
"""