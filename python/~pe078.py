MOD = 1000000
# top down approach
cache = [
    [0],
    [0] + [1]
]
# swal = starts with at least
def calculate(n):
    if cache[n] == []:
        cache[n] = [0] + [1 for i in range(n)]
        acc = 1
        for swal in reversed(range(1, n//2+1)):
            remainder = n - swal 
            if cache[remainder] == []:
                calculate(remainder)
            cache[n][swal] = (cache[remainder][swal] + acc) % MOD
            acc += cache[remainder][swal]
def partitions(n):
    for i in range(len(cache), n+1):
        cache.append([])
    calculate(n)
    return cache[n][1]
    
n = 3
while True:
    a = partitions(n)
    if a == 0:
        print(n)
        break
    n += 1