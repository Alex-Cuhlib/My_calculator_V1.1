#калькулятор который смог

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init ()

print( Fore.BLACK )
print( Back.WHITE )

what = input ("Что делаем? (+, -, *, /): " )

print( Fore.BLACK )
print( Back.BLUE )

a = int ( input("Первое число: ") )
b = int ( input("Второе число: ") )

print( Fore.BLACK )
print( Back.RED )

if what == "+":
    c = a + b
    print ("Результат: " + str(c) )

elif what == "-":
    c = a - b
    print ("Результат: " + str(c) )

elif what == "*":
    c = a * b
    print ("Результат: " + str(c) )

elif what == "/":
    c = a / b
    print ("Результат: " + str(c) )

else:
    print("Выбрана неверная операция!")

input ()