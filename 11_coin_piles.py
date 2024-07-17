def can_empty_piles(a, b):
    if (a + b) % 3 != 0:
        return "NO"
    if a > 2 * b or b > 2 * a:
        return "NO"
    return "YES"

t = int(input())
data = []

for _ in range(t):
    a, b = map(int, input().split())
    data.append((a, b))
for i in data:
    a, b = i
    print(can_empty_piles(a, b))