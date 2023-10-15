#INTRO TO IT 2nd COURSE
# Задача 3: Четное или нечетное?
# Попробуй определить, является ли введенное число четным или нечетным.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
number = 5
print(f"{number} - {even_or_odd(number)}")
