#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def this_is_a_palindrome(line):
    return line == line[::-1]
line = "radar"
print(f"Is it '{line}' palindrome? {this_is_a_palindrome(line)}")
