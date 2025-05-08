from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        all_values = []
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                all_values.append(grid[i][j])

        sorted_values = sorted(all_values, reverse=False)

        diff_list = [sorted_values[i] - sorted_values[0] for i in range (len(sorted_values))]

        for diff in diff_list:
            if diff % x == 0:
                continue
            else:
                return -1

        target_list = [diff/x for diff in diff_list]

        target = target_list[len(target_list)//2]

        distance = 0

        for value in target_list:
            distance += abs(target-value)

        return int(distance)