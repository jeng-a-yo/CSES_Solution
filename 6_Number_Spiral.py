def find_spiral_number(y, x):
    if y > x:
        ans = (y-1) ** 2
        if y % 2 == 0:
            add = 2 * y - x
        else:
            add = x
        
    else:
        ans = (x-1) ** 2
        if x % 2 == 0:
            add = y
        else:
            add = 2 * x - y
        
    print(ans + add)

n = int(input().strip())
for i in range(n):
    y, x = map(int, input().strip().split())
    find_spiral_number(y, x)

