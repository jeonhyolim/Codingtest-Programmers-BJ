import sys

n = int(input())
_max = sys.maxsize
def sugar_2839(n):
    sugar_dp = [_max, _max, _max, 1, _max, 1]
    for i in range(6, n+1):
        cnt = min(sugar_dp[i-5], sugar_dp[i-3])
        sugar_dp.append(cnt + 1 if cnt != _max else _max) 
    return sugar_dp[n] if sugar_dp[n] != _max else -1

print(sugar_2839(n))