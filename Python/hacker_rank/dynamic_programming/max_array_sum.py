def maxSubsetSum(arr):
    n = len(arr)
    
    # Special cases: when array is empty or contains a single element
    if n == 0:
        return 0
    elif n == 1:
        return max(0, arr[0])

    # Initializing the DP array
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])

    for i in range(2, n):
        # There are two choices: 
        # 1. We include the current element and the maximum sum excluding the previous element
        # 2. We exclude the current element which means maximum sum so far remains same
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

    return dp[n - 1]
