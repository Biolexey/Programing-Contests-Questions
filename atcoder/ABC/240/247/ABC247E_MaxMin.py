def f(a):                                   #0が連続してる部分で範囲の組み合わせn_C_2を計算する
  ans, s = 0, 1
  for x in a:
    if x == 1:
      ans += s * (s - 1) // 2
      s = 1
    else:
      s += 1
  ans += s * (s - 1) // 2
  return ans

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

__, X_, _Y, XY = [0]*N, [0]*N, [0]*N, [0]*N #__は全ての列、X_はXを含まない列、_YはYを含まない列、XYは両方含まない列(1は範囲外であることを示す)
for i in range(N):
  if not (Y <= A[i] and A[i] <= X):
    __[i], X_[i], _Y[i], XY[i] = 1, 1, 1, 1 #範囲外の数はもれなく1に設定
  if A[i] == X:
    X_[i], XY[i] = 1, 1
  if A[i] == Y:
    _Y[i], XY[i] = 1, 1


print(f(__)-f(X_)-f(_Y)+f(XY))