def replace_non_x_alphabet(input_string):
    result = ""
    for char in input_string:
        if char.isalpha() and char != 'x':
            result += 'x'
        elif char.isdigit():
            result += char
        else:
            result += char
    return result

# Example usage:
original_string = "Hello, World! This is a test. 12345"
result = replace_non_x_alphabet(original_string)
# print(result)  # Output: xxxxx, xxxxx! xxxxx xx x xxxx. 12345
