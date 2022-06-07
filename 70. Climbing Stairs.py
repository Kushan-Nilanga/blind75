# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 4:
        return n

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = sum(dp[i-2:i])

    return dp[-1]


out = climbStairs(10)
print(out)
