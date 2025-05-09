numero = int(input("qual o numero da tabuada? "))
print('Imprimindo a tabuada de', numero)
for contador in range(0, 11, 1):
    print(contador, 'x', numero, '=', contador * numero)
