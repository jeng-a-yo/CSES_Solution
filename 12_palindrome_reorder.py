def palindrome_recorder(s):
    # Step 1: Count character frequencies
    char_dict = {k: s.count(k) for k in set(s)}
    
    # Step 2: Check for palindrome feasibility
    odd_char_count = sum(1 for count in char_dict.values() if count % 2 != 0)
    if odd_char_count > 1:
        return "NO SOLUTION"
    
    # Step 3: Construct the palindrome
    left_half = []
    middle = []
    
    for char, count in sorted(char_dict.items()):  # Sorting to get a deterministic order
        if count % 2 == 0:
            left_half.append(char * (count // 2))
        else:
            left_half.append(char * (count // 2))
            middle.append(char)
    
    left_half = ''.join(left_half)
    right_half = left_half[::-1]
    middle = ''.join(middle)
    
    result = left_half + middle + right_half
    return result


s = input()
print(palindrome_recorder(s))