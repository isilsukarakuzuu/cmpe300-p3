import random
import time
import sys

sys.setrecursionlimit(100000)

'''Ver1. The classical deterministic algorithm. The pivot is chosen as the first element of the 
list.
Ver2. The randomized algorithm. The pivot is chosen randomly. This is the algorithm 
“Quicksort (1st version)” in the course slides.
Ver3. The randomized algorithm. The list is first randomly permuted and then the classical 
deterministic algorithm is called where the pivot is chosen as the first element of the 
list. This is the algorithm “Quicksort (2nd version)” in the course slides.
Ver4. The deterministic algorithm. The pivot is chosen according to the “median of three” 
rule.
'''

#ver_type decides the version of quick sort 
def pivot_decider(ver_type, array, low, high):
  if(ver_type == 1):
    return array[low]
  if(ver_type == 2):
    return random.choice(array[low:high+1])
  if(ver_type == 3):
    random.shuffle(array[low:high+1])
    return array[low]
  if(ver_type == 4):
    return median_of_three(array,low,high)

#median of three function for Ver4:
def median_of_three(array,low,high):
  mid = low + (high - low)//2
  median = sorted([array[low], array[high], array[mid]])[1]
  return median

#function to find partitions
def partition(ver_type, array, low, high):
    pivot = pivot_decider(ver_type, array, low, high)
    pivot_index = low
    i = low
    # Traverse through all elements and compare each element with pivot
    for j in range(low, high+1):
        if array[j] <= pivot:
            (array[i], array[j]) = (array[j], array[i])
            if array[i] == pivot:
              pivot_index = i
            i += 1
    (array[i - 1], array[pivot_index]) = (array[pivot_index], array[i - 1])
    return i-1
  

# Function to perform quicksort 
def quick_sort(ver_type, array, low, high):

    if low < high:
        pivot = partition(ver_type, array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(ver_type, array, low, pivot - 1)
  
        # Recursive call on the right of pivot
        quick_sort(ver_type, array, pivot + 1, high)
  

#generating input

'''InpType1. Each element of the list is an integer between 1 and 10*n. The elements are 
randomly chosen within this range. Note that the elements in the list will be 
mostly distant integers due to the interval used to choose the elements.
InpType2. Each element of the list is an integer between 1 and 0.75*n. Note that in this case 
there will be duplicate elements in the list.
InpType3. Each element of the list is an integer between 1 and 0.25*n. Note that in this case 
there will be much more duplicate elements in the list.
InpType4. All the elements are the integer 1.'''

def generate_array(type, size):
  if(type == 1):
     return [random.randint(1, 10 * size) for i in range(size)]
  if(type == 2):
     return [random.randint(1, 0.75 * size) for i in range(size)]
  if(type == 3):
    return [random.randint(1, 0.25 * size) for i in range(size)]
  if(type == 4):
    return [1] * size

def run(sort_type, n, input):
  t = time.time()
  quick_sort(sort_type, input, 0, n-1)
  t = time.time() - t
  return t

for sort_type in range(1,5):
  for n in [100, 1000,10000]:
    for input_type in range(1,5):
      average_time = 0
      for average in range(1,6):
        input = generate_array(input_type, n)
        average_time += run(sort_type, n, input)
      average_time /= 5
      worstTime = run(sort_type, n, sorted(generate_array(input_type, n), reverse=True))

      print(f"SortType: {sort_type} n: {n} inputType: {input_type} averageTime: {average_time} worstTime: {worstTime}")

  