# String Operations Example
str1 = "Hello"
str2 = "Python"

# 1. Concatenation
concatenated = str1 + " " + str2
print(f"Concatenation: {concatenated}")

# 2. Repetition
repetition = str1 * 3
print(f"Repetition: {repetition}")

# 3. Length
length_str1 = len(str1)
length_str2 = len(str2)
print(f"Length of str1: {length_str1}, Length of str2: {length_str2}")

# 4. Indexing
print(f"First character of str1: {str1[0]}")
print(f"Last character of str2: {str2[-1]}")

# 5. Slicing
print(f"Slice str1[1:4]: {str1[1:4]}")
print(f"Slice str2[::2]: {str2[::2]}")

# 6. Case conversion
print(f"str1.upper(): {str1.upper()}")
print(f"str2.lower(): {str2.lower()}")
print(f"str1.capitalize(): {str1.capitalize()}")
print(f"str2.title(): {str2.title()}")

# 7. Comparison
print(f"str1 == 'Hello': {str1 == 'Hello'}")
print(f"str1 < str2: {str1 < str2}")

# 8. Membership
print(f"'H' in str1: {'H' in str1}")
print(f"'x' in str2: {'x' in str2}")

# 9. String methods
print(f"str1.find('l'): {str1.find('l')}")
print(f"str2.count('o'): {str2.count('o')}")
print(f"str1.replace('Hello', 'Hi'): {str1.replace('Hello', 'Hi')}")

# 10. Split and Join
words = "Hello Python Programming".split()
print(f"Split: {words}")
print(f"Join: {'-'.join(words)}")

# 11. Stripping whitespace
str_with_spaces = "  Hello  "
print(f"Original: '{str_with_spaces}'")
print(f"strip(): '{str_with_spaces.strip()}'")
print(f"lstrip(): '{str_with_spaces.lstrip()}'")
print(f"rstrip(): '{str_with_spaces.rstrip()}'")

# 12. String formatting
formatted = f"{str1} {str2}"
print(f"f-string: {formatted}")
print("format(): {} {}".format(str1, str2))

