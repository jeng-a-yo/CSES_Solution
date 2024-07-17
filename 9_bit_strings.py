def bit_strings(n):
    MOD = 10**9 + 7
    return pow(2, n, MOD)

# Read input
n = int(input())
print(bit_strings(n))
