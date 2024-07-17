n = int(input())

# Initialize the list with the 1-bit Gray codes
gray_codes = ['0', '1']

# Generate Gray codes for each additional bit
for i in range(2, n + 1):
    # Reflect the current list of Gray codes
    reflected = gray_codes[::-1]
    
    # Add '0' to the beginning of each code in the original list
    gray_codes = ['0' + code for code in gray_codes]
    
    # Add '1' to the beginning of each code in the reflected list
    reflected = ['1' + code for code in reflected]
    
    # Concatenate the two lists to form the new list of Gray codes
    gray_codes += reflected

# Print the n-bit Gray codes
for code in gray_codes:
    print(code)
