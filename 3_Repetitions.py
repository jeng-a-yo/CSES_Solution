max_length = 1

string_list = input().strip()

temp_len = 0
cur = 'A'
for char in string_list:
    if char == cur:
        temp_len += 1
        max_length = max(max_length, temp_len)
    else:
        cur = char
        temp_len = 1
print(max_length)