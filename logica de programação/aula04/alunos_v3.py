import mysql.connector

cnx = mysql.connector.connect(user='root', password='ceub123456', host='localhost', database='db_teste')
cs = cnx.cursor()
sql = "SELECT * FROM aluno;"
cs.execute(sql, [])

for (ra, nome, nota1, nota2) in cs:
    print('-' * 30)

    print(ra, nome, nota1, nota2)

    media = (nota1 + nota2) / 2
    print('Média =', media)

    if media >= 5:
        print('Aprovado')
    else:
        print('Reprovado')

    if media == 0:
        print ('Menção = SR')
    elif media < 2:
        print('Menção = II')
    elif media < 5:
        print('Menção = MI')
    elif media < 7:
        print('Menção = MM')
    elif media < 9:
        print ('Menção = MS')
    else:
        print ('Menção = SS')

# Número total de alunos = 99
# Média Geral da turma = .99

cs.close()
cnx.close()
