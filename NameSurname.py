import random, math, time, sys

sys.setrecursionlimit(10010)

'''
Ver1. The classical deterministic algorithm. The pivot is chosen as the first element of the 
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
  if ver_type == 1 or ver_type == 3:
    return array[low]
  if(ver_type == 2):
    return random.choice(array[low:high+1])
  if(ver_type == 4):
    return median_of_three(array,low,high)

#median of three function for Ver4:
def median_of_three(array,low,high):
  mid = low + (high - low) // 2
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

'''
InpType1. Each element of the list is an integer between 1 and 10*n. The elements are 
randomly chosen within this range. Note that the elements in the list will be 
mostly distant integers due to the interval used to choose the elements.
InpType2. Each element of the list is an integer between 1 and 0.75*n. Note that in this case 
there will be duplicate elements in the list.
InpType3. Each element of the list is an integer between 1 and 0.25*n. Note that in this case 
there will be much more duplicate elements in the list.
InpType4. All the elements are the integer 1.
'''

def run(sort_type, n, input):
  t = time.time()
  quick_sort(sort_type, input, 0, n-1)
  t = time.time() - t
  return t

f = open('output.txt', 'w')

def printArray(array, size):
  for i in range(size - 1):
    f.write(f'{array[i]}-')

  f.write(f'{array[size - 1]}\n')

# Version
for n in [100, 1000, 10000]:
  for input_type, maxElement in enumerate([10*n, math.ceil(0.75*n), math.ceil(0.25*n), 1]):
    for version in range(1,5):
      # Average Case
      average_time = 0
      for average in range(1,6):
        averageInput = [random.randint(1, maxElement) for T in range(n)]

        # If version is 3, start the algorithm by shuffling the list
        if version == 3:
          random.shuffle(averageInput)
        f.write(f'Input {average}: (Average)')
        printArray(averageInput, n)
        average_time += run(version, n, averageInput)
        f.write(f'Output {average}: (Average)')
        printArray(averageInput, n)
      average_time /= 5

      # Worst Case
      worstInput = sorted([random.randint(1, maxElement) for T in range(n)])
      f.write('Input: (Worst)')
      printArray(worstInput, n)

      # If version is 3, start the algorithm by shuffling the list
      if version == 3:
          random.shuffle(worstInput)

      worstTime = run(version, n, worstInput)
      f.write('Output: (Worst)')
      printArray(worstInput, n)

      f.write(f"Version: {version}\tN: {n}\tinputType: {input_type + 1}\tAverage Time: {average_time}\tWorst Time: {worstTime}\n\n")

