import sys

def main():
    a, b, n  = map(int, input().split())
    point = a
    day = 10

    ten = 10*a+b                            # 十日分
    hundred = 9*ten+10*(a+b)                # 百日分
    thousand = 9*hundred+10*(100*(a+b))     # 千日分

    while point < n:
        
    
    while point < n:
        day += 1
        point += a
        if "7" in str(day):
            point += b

    print(day)


if __name__ == '__main__':
    main()
