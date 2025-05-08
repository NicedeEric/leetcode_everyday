# Min/Max Heap Operations Time Complexity. The default heap of heapq is min-heap
<ol>
<li>heapq.heappush(heap, item)
操作：将一个元素 item 插入堆 heap。
时间复杂度：O(log n)
这是因为在最坏情况下，插入一个元素可能需要调整堆的结构，最多需要遍历堆的高度，即 log n 的时间复杂度。
<li>heapq.heappop(heap)
操作：移除并返回堆中的最小元素（即堆顶元素）。
时间复杂度：O(log n)
移除堆顶元素后，堆的结构需要重新调整（即“下沉”操作），时间复杂度为 log n。
<li>heapq.heapify(iterable)
操作：将一个无序的列表转化为一个有效的堆。
时间复杂度：O(n)
heapify 操作通过对每个元素进行调整（“下沉”）来构建堆，其时间复杂度是 O(n)，比逐个插入元素更高效。
<li>heapq.nlargest(n, iterable)
操作：返回可迭代对象中最大的 n 个元素，通常会使用堆来实现。
时间复杂度：O(n log k)
这里 n 是可迭代对象的大小，k 是要返回的最大元素个数。因为需要对前 k 个元素建堆，然后扫描剩余的 n - k 个元素。
<li>heapq.nsmallest(n, iterable)
操作：返回可迭代对象中最小的 n 个元素，通常会使用堆来实现。
时间复杂度：O(n log k)
同 nlargest，k 是要返回的最小元素个数。
<li>heapq.replace(heap, item)
操作：移除堆顶元素并将新元素 item 插入堆。
时间复杂度：O(log n)
因为移除堆顶元素需要重新调整堆结构，然后再插入新元素。
<li>堆的排序的时间复杂度是O(nlogn)
</ol>

# Heap Usage
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

## heapify function have no return value, it turns the original list into a heap

```python

import heapq

unordered_list = [4,23,5,6,12,3,7,8]

heapq.heapify(unordered_list)

while unordered_list:
    print(heapq.heappop(unordered_list))

```
