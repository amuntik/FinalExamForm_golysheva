#INTRO TO IT 2nd COURSE
# Задача 10: Квадраты на улице!
# Создай список, содержащий квадраты чисел от 0 до введенного числа.
def generation_quadrates(number):
    return [x**2 for x in range(number)]
чnumber = 5
print(f"{number} of the first squares: {generation_quadrates(number)}")