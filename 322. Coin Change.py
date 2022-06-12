# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

def solution(coins, amount):
    dp = [amount+1] * (amount + 1)

    # default case
    dp[0] = 0

    for a in range(1, amount+1):
        # bruteforcing from old solutions
        for c in coins:
            # we are trying to create 'a'
            if a - c >= 0:
                # one comes from current coin
                # a-c is what to be made after we use the current coin
                dp[a] = min(dp[a], 1+dp[a-c])

    # return if we have a solution
    return dp[amount] if dp[amount] != amount + 1 else -1


out = solution([1, 2, 5], 11)
print(out)
