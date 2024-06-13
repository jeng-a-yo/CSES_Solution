max_length = 1

string_list = input().strip()

temp_len = 0
for i in range(len(string_list) - 1):

    if string_list[i] == string_list[i + 1] and temp_len == 0:
        temp_len += 2
    elif string_list[i] == string_list[i + 1]:
        temp_len += 1
    else:
        temp_len = 0

    max_length = max(max_length, temp_len)
    

print(max_length)