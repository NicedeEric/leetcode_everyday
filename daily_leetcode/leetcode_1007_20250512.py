# 实际上只有1-6这几种结果。所以针对每种结果，我们都去判断一下能不能被swap实现就好了

class Solution:
    def minDominoRotations(self, tops, bottoms):
        res = float('inf')
        for val in range (1,7):
            top_swap = bottom_swap = 0
            valid = True
            for t, d in zip(tops, bottoms):
                if t != val and d != val:
                    valid = False
                    break
                if t != val:
                    top_swap += 1
                if d != val:
                    bottom_swap += 1
            if valid == True:
                res = min(res, top_swap, bottom_swap)
        
        if res == float('inf'):
            return -1
        else:
            return res
                