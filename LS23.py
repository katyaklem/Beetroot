'''
8. Створіть декоратор, який заміряє час виконання задекорованої функції. Декоратор не обмежує кількість та порядок аргументів, 
що передаються функції. Декоратор має у циклі викликати задекоровану функцію 1000 разів, а після того виводити рядок з назвою функції, 
її аргументами, часом виконання 1000 викликів. Декоратор має повертати результат останнього, тисячного, виклику функції.

9. Реалізувати функцію eucledian_gcd(a: int, b: int) -> int, яка обраховуватиме найбільший спільний дільник для агрументів a та b за алгоритмом Евкліда. 

Алгоритм Евкліда для пошуку НСД:
    1) Допоки a != b:
        - якщо a > b, то a = a - b
        - якщо b > a, то b = b - a
    2) Коли a == b, повертаємо а, яке і буде найбільшим спільним дільником.

10. З модулю math імпортувати функцію gcd, яка обраховує набільший спільний дільник.

12. Викликати кожну задекоровану функцію з завдання 11 з аргументами:
    1) a = 30, b = 6
    2) a = 100, b = 1
    3) a = 999, b = 9
    4) a = 4, b = 1024
'''
from math import gcd
from time import time

def timer_func(func):
    def wrap_func(*args, **kwargs):
        i=0
        t1 = time()
        while i<1000:
            result = func(*args, **kwargs)
            i+=1
        t2 = time()
        work_time = t2-t1
        return [func.__name__, args, work_time, result]
        #return print(f'Function name is: {func.__name__}, Arguments are: {args}, Work time is {work_time}, Result is {result}')
    return wrap_func

@timer_func
def eucledian_gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a

@timer_func
def standart_gcd(a: int, b: int) -> int:
    return gcd(a, b)

standart_method1 = standart_gcd(30, 6)
standart_method2 = standart_gcd(100, 1)
standart_method3 = standart_gcd(999, 9)
standart_method4 = standart_gcd(4, 1024)

my_method1 = eucledian_gcd(30, 6)
my_method2 = eucledian_gcd(100, 1)
my_method3 = eucledian_gcd(999, 9)
my_method4 = eucledian_gcd(4, 1024)

print(standart_method1)
print(my_method1)

print(standart_method2)
print(my_method2)

print(standart_method3)
print(my_method3)

print(standart_method4)
print(my_method4)