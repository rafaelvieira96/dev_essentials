#!/usr/bin/python3

num = input('Digite um numero: ')

#try:
if num.isnumeric():
    print(int(num) +2)
else:
#except Exception:
    print('num nao é um numero')