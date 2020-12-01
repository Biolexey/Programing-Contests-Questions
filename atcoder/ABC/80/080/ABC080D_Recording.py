n, c = map(int, input().split())
l = 2*10**5+5
t = [0]*l#0.5分単位なので実質時間２倍
C = set()#今回録画するチャンネルの総数(cとは別物)
for i in range(n):
    s, f, ch = map(int, input().split())
    t[s*2-1] += 1#開始時間の0.5秒前からレコーダを拘束
    t[f*2] -= 1#終了時間にはレコーダを開放
    C.add(ch)
for i in range(1, l):
    t[i] += t[i-1]#レコーダ継続使用を記録
 
ans = 0
for i in range(1, l):
    ans = max(t[i], ans)#レコードの最大同時使用数を調べる
print(min(len(C),ans))#録画チャンネル数と比較する
