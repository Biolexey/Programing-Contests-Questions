n = int(input())
S = [*map(int, input().split())]

def merge(A, left, mid, right):
  #print("ここでmerge" + str(left) + " " + str(mid) + " " + str(right))
  L = A[left:mid] + [float("inf")]
  R = A[mid:right] + [float("inf")]
  i, j, count = 0, 0, 0
  for k in range(left, right):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
      count += mid - left - i
  return count

def merge_sort(A, left, right):
  #print("ここでmergesort" + str(left) + " " + str(right))
  count = 0
  if right - left > 1:
    mid = (left + right) // 2
    count += merge_sort(A, left, mid) + merge_sort(A, mid, right)
    count += merge(A, left, mid, right)
  return count

print(merge_sort(S, 0, n))

