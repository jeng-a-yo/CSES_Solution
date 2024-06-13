n = int(input().strip())

if n == 1:
    print("1")
elif n <= 3:
    print("NO SOLUTION")
else:
    odds = list(range(1, n+1, 2))
    evens = list(range(2, n+1, 2))
    permutatiom = evens + odds
    for i in permutatiom:
        print(i, end=' ')