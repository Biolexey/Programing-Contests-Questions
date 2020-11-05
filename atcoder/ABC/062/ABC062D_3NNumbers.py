import heapq as hp
n = int(input())
nums = [*map(int, input().split())]

L = nums[:n]
hp.heapify(L)
Lmax = [0]*(n+1)
Lsum = sum(L)
Lmax[0] = Lsum
for i in range(n, 2*n):
    m = hp.heappushpop(L, nums[i])
    Lsum += nums[i] - m
    Lmax[i-n+1] = Lsum

R = [-x for x in nums[2*n:]]
hp.heapify(R)
Rmin = [0]*(n+1)
Rsum = -sum(R)
Rmin[n] = Rsum
for i in range(2*n-1, n-1, -1):
    M = -hp.heappushpop(R, -nums[i])
    Rsum -= M - nums[i]
    Rmin[i-n] = Rsum

print(max(Lmax[i] - Rmin[i] for i in range(n+1)))