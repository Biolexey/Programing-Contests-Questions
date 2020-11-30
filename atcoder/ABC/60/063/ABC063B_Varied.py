import collections 
s = input()
nums = collections.Counter(s).values()
print("yes" if len(nums) == sum(nums) else "no")

#もっと賢い方法があった
s = input()
print("yes" if len(s) == len(set(s)) else "no")