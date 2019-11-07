# -*- coding:utf-8 -*-
# time: 2019/03/21 9:12
# File: edit_distance.py
import datetime

start = datetime.datetime.now()
def editDistDP(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # insert
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    print(dp)
    return dp[m][n]
s1 = "sunday"
s2 = "saturday"
edit_distance = editDistDP(s1, s2)
print("The Edit Distance of '%s and '%s' is %d." % (s1, s2, edit_distance))

end = datetime.datetime.now()
print("[ Finished in", (end - start), "]")