#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def counting_of_the_voiceless(line):
    return sum(1 for symbol in line if symbol.lower() in "ft`bjes'.z")
line = "Hello, World!"
print(f"In '{line}' {counting_of_the_voiceless(line)} voiceless")
