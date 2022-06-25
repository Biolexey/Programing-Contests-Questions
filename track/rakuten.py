# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import permutations

def solution(S):
    # write your code in Python 3.6
    MOD = (10**9)+7
    vowels = {"A", "E", "I", "O", "U"}
    vo = ""
    co = ""
    for i in range(len(S)):
        if S[i] in vowels:
            vo += S[i]
        else:
            co += S[i]
    voc = list(permutations(vo, len(vo)))
    coc = list(permutations(co, len(co)))
    
    vonum = len(set(voc)) % MOD
    conum = len(set(coc)) % MOD

    if len(vo)+1 == len(co):
        ans = vonum*conum % MOD
    elif len(vo) == len(co):
        ans = vonum*conum % MOD
    else:
        ans = 0

    return ans