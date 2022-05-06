def is_prime(x):
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            return False
    return True

n = int(input())
print(sum(is_prime(int(input())) for _ in range(n)))