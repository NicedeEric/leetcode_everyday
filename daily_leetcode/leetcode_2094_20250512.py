# 这个题目，常规的做法会是，找出所有的三元数组。进行3个递归，然后在每一次递归开始进行去重，同时排除上一层取过的数值。
# 最后可以对结果进行去除奇数的逻辑，以及排序
# 然而这种做法是至少有O(n^3)的复杂度
# 考虑到只是3元数组，那么实际上最多只可能形成1000个数，只需要判断1000个数，是否可以被digits形成就可以了

from collections import Counter
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        digits_counter = Counter(digits)

        for i in range (100, 1000):
            if i % 2 != 0:
                continue
            
            cur_counter = {}
            for digit in str(i):
                cur_counter[int(digit)] = cur_counter.get(int(digit), 0) + 1

            flag = True

            for key, value in cur_counter.items():
                if value > digits_counter[key]:
                    flag = False
                    break
            if flag:
                res.append(i)

        return res