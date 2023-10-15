#INTRO TO IT 2nd COURSE
# Задача 7: Факториал на месте!
# Рассчитай факториал введенного числа.
def factorial(number):
    return 1 if number == 0 else number * factorial(number-1)
number = 5
print(f"Factorial {number} equal to {factorial(number)}")
