EURO = 6.34
DOLAR = 5.81
YUAN = 0.80

print('*' * 30)
print('Digite o valor em real R$ para converter:')
real = float(input())
print('*' * 30)

em_euro = real / EURO
em_dolar = real / DOLAR
em_yuan = real / YUAN

print('Aqui estão os resultados')
print(f'R${real} são €{em_euro:.2f} euros.')
print(f'R${real} são ${em_dolar:.2f} dolares')
print(f'R${real} são ¥{em_yuan:.2f} yuans')
