# Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrom(slovo):
    if slovo==slovo[len(slovo)::-1]:
        print('слово '+slovo+' - палиндромом')
    else:
        print('слово '+slovo+' - не палиндромом')

palindrom(input('Введите слово: '))