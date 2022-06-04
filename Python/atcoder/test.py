import sys
import requests
import pprint
import json

global url
url = "http://challenge-server.code-check.io/api/recursive/ask"



def func(n):
    global url, txt

    N = [0 for _ in range(51)]

    if n == 0:
        return 1
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return func(n-1) + func(n-2) + func(n-3) + func(n-4)
    else:
        if N[n]:
            return N[n]
        else:
            param = {"seed": txt, "n": n}
            res = requests.get(url, params=param)
            data = res.json()
            result = int(data["result"])
            N[n] = result
            return result

if __name__ == '__main__':
    try:
        global txt
        args = sys.argv
        if len(args) > 3:
            main()
        txt, num = args[1], int(args[2])
        print(func(num))

    except:
        print("error!")
        main()