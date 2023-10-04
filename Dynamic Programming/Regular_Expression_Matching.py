class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]  # 2D table for DP
        
        dp[m][n] = True  # Base case: empty pattern matches empty string
        
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                match = i < m and (p[j] == s[i] or p[j] == '.')  # Check current characters match
                
                if j+1 < n and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j] = match and dp[i+1][j+1]
        
        return dp[0][0]