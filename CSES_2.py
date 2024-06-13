n = int(input())
nums_list = list(map(int, input().strip().split(' ')))

print(sum([i for i in range(1, n+1)]) - sum(nums_list))