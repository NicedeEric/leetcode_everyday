
def one_d_bag_problem(weight, value, bagweight):
    dp = [0] * (bagweight + 1)

    for i in range (len(weight)):
        for j in range (bagweight, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
        print(dp)

    return dp[bagweight]    

weight = [1,3,4]
bagweight = 4
value = [15,20,30]

print(one_d_bag_problem(weight,value,bagweight))
