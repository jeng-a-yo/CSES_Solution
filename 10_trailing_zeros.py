def trailing_zeros(n):
    count = 0
    power_of_5 = 5
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    return count

# Read input
n = int(input())
print(trailing_zeros(n))
