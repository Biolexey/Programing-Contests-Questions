#自分の回答
N = int(input())
cards = [i for i in map(int, input().split())]
cards.sort(reverse = True) 
alice = sum(cards[::2])
bob = sum(cards[1::2])

print(alice - bob)

#簡潔
N = int(input())
a = sorted(map(int, input().split()), reverse = True)
print(sum(a[::2]) - sum(a[1::2]))
