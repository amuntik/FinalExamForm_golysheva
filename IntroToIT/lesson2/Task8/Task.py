#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def count_words(line):
    return len(line.split())
line = "Python is beautiful!"
print(f"В '{line}' {count_words(line)} слов")
