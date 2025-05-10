#colocar "pass" para sair de uma fução enquanto coda, server para ver o codigo/montar a estrutura e depois mecher nas funções

compras = [('feijão 1kg', 3, 15.50)]


def adicionar():
    print('Aicionando...')
    produto = input('Digite o nome do produto')
    quantidade = int(input('Digite a quantidade'))
    preco = float(input('Digite o preço do produto'))
    item = (produto, quantidade, preco)
    compras.append(item)

def imprimir():
    print('Lista de compras:')
    total = 0.0
    num_item = 0
    for item in compras:
        #print(item[0], item[1], item[2], item[1] * item[2])
        print(f'{num_item} - {item[0]}  {item[1]} x R$ {item[2]:.2f} = R$ {(item[1] * item[2]):.2f}')
        total += item[1] * item[2]
        num_item += 1
    print(f'Total de {total:.2f}')

def remover():
    print('Removendo...')
    imprimir()
    indicie = int(input('Qual produto deseja remover? '))
    compras.pop(indicie)

def main():
    while True:
        print('''
        1 - Adicionar produto
        2 - Remover produto
        3 - Listar produtos
        4 - sair
        ''')
        opc = input('qual a opção? ')
        if opc == '1':
            adicionar()
        elif opc == '2':
            remover()
        elif opc == '3':
            imprimir()
        elif opc == '4':
            break
    print('programa encerrado')


main()
