# Homeworck 10.1
def pow(x):
    return x ** 2 # возведения числа в квадрат

def some_gen(begin, n, func):

    value = begin # первый элемент записываем в value
    for i in range(n):
        yield value # записываю текущее заначение
        value = func(value) # передача в функцию pow для возведения в квадрат

# Homeworck 10.2
def first_word(text):
    # заменяем запятые и точки на пробелы. после этого разбиваем на слова и записываем это в переменную word
    word = text.replace("."," ").replace(",", " ").split()
    return word[0]

# Homeworck 10.3
def is_even(digit):
    if digit % 2 == 0: # если число делиться без остатка тогда возвращается True в остальных случаях False
        return True
    else:
        return False

print("Homeworck 10.1")

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

print("Homeworck 10.2")
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

print("Homeworck 10.3")
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

