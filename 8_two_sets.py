def two_sets(n):
    total_sum = n * (n + 1) // 2

    # If the sum is odd, it's not possible to split into two sets with equal sum
    if total_sum % 2 != 0:
        return "NO"

    set1 = []
    set2 = []
    target = total_sum // 2

    # Iterate from the largest number to the smallest
    for num in range(n, 0, -1):
        if target >= num:
            set1.append(num)
            target -= num
        else:
            set2.append(num)
    
    return ("YES", set1, set2)

# Read input
n = int(input())
result = two_sets(n)

if result == "NO":
    print(result)
else:
    print(result[0])
    set1, set2 = result[1], result[2]
    print(len(set1))
    print(" ".join(map(str, set1)))
    print(len(set2))
    print(" ".join(map(str, set2)))
