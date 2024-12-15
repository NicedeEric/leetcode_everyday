## Max Heap Official Lib
The heapq is a built-in Python library that has been available since Python 2.3. It implements a min heap, and its functions are designed to work with lists. <br>

The below given example is of how to use the heapq module to implement a max heap using min-heap in Python:

```python
import heapq

heap = []
# add elements to heap
heapq.heappush(heap, -5)
heapq.heappush(heap, -1)
heapq.heappush(heap, -10)

# get the maximum element
print(-heapq.heappop(heap))

```

The output should be 10

## Another example of heapq usage

```python

from heapq import heappop, heappush, heapify

# Creating an empty max heap
max_heap = []
heapify(max_heap)

# Adding values to max heap
heappush(max_heap, -15)
heappush(max_heap, -20)
heappush(max_heap, -87)
heappush(max_heap, -304)

# Printing the value of the maximum element
print("Maximum value in the max heap: " + str(-max_heap[0]))

# Printing the elements of the max heap
print("The max heap elements: ")
for item in max_heap:
    print(-item, end=" ")
print("\n")

# Extracting the maximum element from the max heap
max_element = heappop(max_heap)

# Printing the elements of the max heap after extraction
print("The max heap elements after extracting maximum: ")
for item in max_heap:
    print(-item, end=' ')
    
```