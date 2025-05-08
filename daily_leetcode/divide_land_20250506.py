# 原题目链接https://www.programmercarl.com/kamacoder/0044.%E5%BC%80%E5%8F%91%E5%95%86%E8%B4%AD%E4%B9%B0%E5%9C%9F%E5%9C%B0.html

'''
【题目描述】

在一个城市区域内,被划分成了n * m个连续的区块,每个区块都拥有不同的权值,代表着其土地价值。目前,有两家开发公司,A 公司和 B 公司，希望购买这个城市区域的土地。

现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。

然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。

为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。

注意：区块不可再分。

【输入描述】

第一行输入两个正整数，代表 n 和 m。

接下来的 n 行，每行输出 m 个正整数。

输出描述

请输出一个整数，代表两个子区域内土地总价值之间的最小差距。

【输入示例】

3 3 1 2 3 2 1 3 1 2 3

【输出示例】

0
###
'''

def main():
    import sys
    input = sys.stdin.read()
    data = input.split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    # create the land array
    total_sum = 0
    land_matrix = []
    for _ in range (n):
        row = []
        for _ in range (m):
            row.append(int(data[idx]))
            total_sum += int(data[idx])
            idx += 1
        land_matrix.append(row)
    
    # horizontal cut
    result = float('inf')
    row_sum = 0
    for i in range (n):
        for j in range (m):
            row_sum += land_matrix[i][j]
        result = min(result, abs((total_sum - row_sum)-row_sum))
    
    col_sum = 0
    for j in range (m):
        for i in range (n):
            col_sum += land_matrix[i][j]
        result = min(result, abs((total_sum-col_sum)-col_sum))
    
    return result
        
if __name__ == '__main__':
    minium_diff = main()

    print(minium_diff)

# This file needs to be run in command
# python3 .\divide_land_20250506.py
# Press enter
# Input 3 3 1 2 3 2 1 3 1 2 3
# Press Ctrl + z
# Press enter