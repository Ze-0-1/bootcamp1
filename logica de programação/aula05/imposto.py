sal = float(input("Qual o seu salario? "))

# Forma-1

imposto = 0
# De R$1.903,99 até R$2.826,65 - 7.5%
if sal >= 1903.99 and sal <= 2826.65:
    imposto = sal * 0.075
# De R$2.826,66 até R$3.751,05 - 15%
elif sal >= 2826.66 and sal <= 3751.05:
    imposto = sal * 0.15
# De R$3.751,06 até R$4.664,68 - 22.5%
elif sal >= 3751.06 and sal <= 4664.68:
    imposto = sal * 0.225
# Acima de R$4.664,68 27.5%
elif sal > 4664.68:
    imposto = sal * 0.275

print("O seu salario é", sal)
print("Você tem que recolher R$", imposto, "de IRPF.")
print(f"Seu salario liquido é: {sal-imposto}")
