def abbreviation(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[False] * (m+1) for _ in range(n+1)]

    # Initialize the DP table
    dp[0][0] = True
    for i in range(n):
        if s1[i].isupper():
            break
        else:
            dp[i+1][0] = True

    # Fill in the DP table
    for i in range(n):
        for j in range(m):
            if s1[i].upper() == s2[j]:
                dp[i+1][j+1] = dp[i+1][j+1] or dp[i][j]
            if s1[i].islower():
                dp[i+1][j+1] = dp[i+1][j+1] or dp[i][j+1]
        
    return 'YES' if dp[n][m] else 'NO'


print(abbreviation('AbCDE', 'ABDE'))
