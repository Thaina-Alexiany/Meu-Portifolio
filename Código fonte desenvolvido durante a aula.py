# Inicialização das variaveis
lista_nomes = list()
lista_prova1 = list()
lista_prova2 = list()
lista_media = list()

# laço de repetição
while True:
    # entrada de dados do usuario com input e conversao de str para float em alguns dados
    nome = input('Digite nome: ')
    prova1 = float(input('Digite nota da prova1: '))
    prova2 = float(input('Digite nota da prova2: '))
    
    # variavel que recebe do usuario se ele deseja continuar ou no laço de repetição
    # A função lower() funciona em strings retornado o resultado em caixa baixa
    continuar = input('Deseja inserir um próximo nome ? n / s: ').lower()
    
    # adiciona os dados que o usuario digitou em listas
    lista_nomes.append(nome)
    lista_prova1.append(prova1)
    lista_prova2.append(prova2)

    media = (prova1+prova2) / 2

    lista_media.append(media)
    
    # verifica se o usuario deseja continuar ou nao
    if continuar == 'n':
        break

# mostra o tamanho da lista nomes, ou seja a quantidade de nomes que tem
print('Quantidade de alunos: ', len(lista_nomes))

# percorre de uma vez só varias listas
for nome, prova1, prova2, media in zip (lista_nomes , lista_prova1, lista_prova2, lista_media):
    print(f'Aluno: {nome}, Prova1: {prova1}, Prova2: {prova2}, Media: {prova2}')