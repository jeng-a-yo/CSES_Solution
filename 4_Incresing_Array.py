ans = 0


n = int(input().strip())
arr = list(map(int, input().strip().split()))

for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        ans += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]

print(ans)
