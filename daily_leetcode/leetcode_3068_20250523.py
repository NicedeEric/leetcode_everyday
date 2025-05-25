'''
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
'''

'''
这个问题首先因为XOR操作的特殊性,一个数假如一直和另一个数进行XOR操作,他的值会在两个值之间反复。这里的主要原因是发现整个nums可不可以一起取到最大,不可以的话就牺牲两个值之间差距最小的数
'''

'''
然后这个问题可以看成对某个数进行偶数还是奇数次操作可以取得最大值。然后对于任意一个数,假如他和剩下的其他所有数可以取得最大值的次数的和是同奇偶的那说明整个都可以取最大,否则,就减去需要牺牲的最小的difs.
所以最后其实是判断整个num operation是不是偶数
'''

from collections import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # find the differences between 2 values
        difs = [abs((x ^ k) - (x)) for x in nums]
        
        # find the minimum difs
        min_difs = min(difs)
        
        targets = [max(x^k, x) for x in nums]
        
        # num of operations to get bigger value for each node
        num_operations = [0 if x >= x ^k else 1 for x in nums]
        
        # find the node that meet the requirements, if so, then can get maximum
        if sum(num_operations) % 2 == 0:
            return sum(targets)
        else:
            return sum(targets) - min_difs