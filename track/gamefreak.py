from collections import deque                           # BFS用キュー

# パラメータの入力
step = int(input())                                     # step数
H, W = map(int, input().split())                        # H,Wを入力
c = [list("#"+input()+"#") for _ in range(H)]           # リストに格納

# リストの外周を壁(#)パディング
c.insert(0, ["#"]*(W+2))
c.append(["#"]*(W+2))

# 各リストを定義
path = [[[] for _ in range(W+2)]for _ in range(H+2)]    # 各点から出ている道
distance = [[-1]*(W+2) for _ in range(H+2)]             # スタートからのコスト
seeing = [[-1]*(W+2) for _ in range(H+2)]               # そこを監視しているトレーナーの座標
trainers = [[set((0,0)) for _ in range(W+2)]for _ in range(H+2)]#道に睨みを利かせているトレーナー

for i in range(1,H+1):                                  # 全走査
    for j in range(1,W+1):

        # 町の時は適宜パラメータ初期化
        if c[i][j] == "A":                              
            start = (i,j)                               # スタート地点に登録
            distance[i][j] = 0                          # 移動コストを0に初期化
        if c[i][j] == "B":
            goal = (i,j)                                # ゴール地点に登録

         # トレーナーの場合
        if c[i][j] == "N":                             
            k = 1
            while c[i-k][j] == ".":                     # 道が続く限り
                trainers[i-k][j].add((i,j))             # 遭遇済みトレーナーに追加
                seeing[i-k][j] = (i,j)                  # 縄張りとして初期化
                k += 1
        if c[i][j] == "S":
            k = 1
            while c[i+k][j] == ".":
                trainers[i+k][j].add((i,j))
                seeing[i+k][j] = (i,j)
                k += 1
        if c[i][j] == "W":
            k = 1
            while c[i][j-k] == ".":
                trainers[i][j-k].add((i,j))             
                seeing[i][j-k] = (i,j)
                k += 1
        if c[i][j] == "E":
            k = 1
            while c[i][j+k] == ".":
                trainers[i][j+k].add((i,j))             
                seeing[i][j+k] = (i,j)
                k += 1

        # 四方に道(or 町B)があればpathに追加             
        if c[i-1][j] == "." or c[i-1][j] == "B":
            path[i][j].append((i-1,j))
        if c[i+1][j] == "." or c[i+1][j] == "B":        
            path[i][j].append((i+1,j))
        if c[i][j-1] == "." or c[i][j-1] == "B":
            path[i][j].append((i,j-1))
        if c[i][j+1] == "." or c[i][j+1] == "B":
            path[i][j].append((i,j+1))

# 幅優先探索で最短歩数を求める
q = deque()
q.append(start)
while len(q)>0:                                         # 幅優先探索
    now = q.popleft()                                   # 現在の探索点   
    for go in path[now[0]][now[1]]:                     # 行き先選択

        if distance[go[0]][go[1]] == -1:                # 行き先が未探索
            q.append(go)
            distance[go[0]][go[1]] = distance[now[0]][now[1]]+1# 移動コストを自分+1
            trainers[go[0]][go[1]] = trainers[go[0]][go[1]].union(trainers[now[0]][now[1]])
                                                        # 遭遇済みトレーナーを更新
        
        if distance[go[0]][go[1]] == distance[now[0]][now[1]]+1:# 探索済みで自分+1のコストの場合
            tmp = set()                                 # 退避用セット
            for i in trainers[now[0]][now[1]]:          # 現在地の遭遇済みトレーナーをコピー
                tmp.add(i)
            if seeing[go[0]][go[1]] != -1:              # そこを縄張りとするトレーナーがいた場合
                tmp.add(seeing[go[0]][go[1]])           # その人も追加する
            if len(tmp) > len(trainers[go[0]][go[1]]):  # (その上で)現在地の方が遭遇人数多ければ更新
                trainers[go[0]][go[1]] = tmp
        


# 最短ルートを全て洗い出す
I, J = goal[0], goal[1]
walk = distance[I][J]                                   # 町Bへの最短移動コスト
ans = len(trainers[I][J])-1                             # 町B時点でのトレーナー遭遇数

def main():
    if step == 1:                                       # step1
        print(W-1, c[1][2:-2].count("S"))               # W-3とs[1][2:-2]の"S"の数を出力

    else:                                               # step2,3
        print(walk, ans)                                # 最短距離と最大トレーナー遭遇数
        
if __name__ == '__main__':
    main()