n, m = map(int, input().split())
nums = [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    nums[a-1] += 1
    nums[b-1] += 1

print(*nums, sep = "\n")