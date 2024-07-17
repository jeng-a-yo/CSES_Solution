def two_knights(n):
    results = []
    for k in range(1, n + 1):
        total_ways = k * k * (k * k - 1) // 2
        attacking_ways = 4 * (k - 1) * (k - 2)
        results.append(total_ways - attacking_ways)
    return results

# Read input
n = int(input())
results = two_knights(n)
for result in results:
    print(result)
