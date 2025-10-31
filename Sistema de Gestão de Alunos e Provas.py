# ==========================================================
# SISTEMA DE GERENCIAMENTO DE ALUNOS E NOTAS
# Autor: [Thainá Alexiany dos Santos]
# ==========================================================

# ----------- IMPORTS ------------
from datetime import datetime

# ----------- VARIÁVEIS GLOBAIS ------------
alunos = []
codigo_atual = 1
matricula_atual = 1000

# ----------- FUNÇÕES AUXILIARES ------------

def gerar_codigo():
    """Gera código automático incremental para o aluno"""
    global codigo_atual
    codigo = codigo_atual
    codigo_atual += 1
    return codigo

def gerar_matricula():
    """Gera matrícula automática incremental"""
    global matricula_atual
    matricula = matricula_atual
    matricula_atual += 1
    return matricula

def encontrar_aluno_por_codigo(codigo):
    """Busca aluno pelo código"""
    for aluno in alunos:
        if aluno['codigo'] == codigo:
            return aluno
    return None

def encontrar_aluno_por_nome(nome):
    """Busca aluno pelo nome"""
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            return aluno
    return None

# ----------- CADASTRO DE ALUNOS ------------

def cadastrar_aluno():
    """Cadastra um novo aluno"""
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    cpf = input("CPF: ").strip()

    aluno = {
        'codigo': gerar_codigo(),
        'matricula': gerar_matricula(),
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'situacao': 'Matriculado',
        'notas': []
    }

    alunos.append(aluno)
    print(f"✅ Aluno {nome} cadastrado com sucesso! Código: {aluno['codigo']} | Matrícula: {aluno['matricula']}")

def remover_aluno():
    """Remove um aluno pelo nome ou matrícula"""
    print("\n--- Remover Aluno ---")
    opcao = input("Remover por (1) Nome ou (2) Matrícula? ")

    if opcao == '1':
        nome = input("Digite o nome: ").strip()
        aluno = encontrar_aluno_por_nome(nome)
    elif opcao == '2':
        matricula = input("Digite a matrícula: ").strip()
        aluno = next((a for a in alunos if str(a['matricula']) == matricula), None)
    else:
        print("❌ Opção inválida.")
        return

    if aluno:
        alunos.remove(aluno)
        print(f"🗑️ Aluno {aluno['nome']} removido com sucesso.")
    else:
        print("❌ Aluno não encontrado.")

def listar_alunos():
    """Lista todos os alunos"""
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"Código: {aluno['codigo']} | Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Situação: {aluno['situacao']} | Notas: {aluno['notas']}")

def ordenar_alunos():
    """Ordena alunos por nome"""
    alunos.sort(key=lambda a: a['nome'])
    print("\n✅ Alunos ordenados por nome!")

# ----------- CADASTRO DE NOTAS ------------

def cadastrar_notas():
    """Cadastra notas para um aluno existente"""
    print("\n--- Cadastro de Notas ---")
    try:
        codigo = int(input("Digite o código do aluno: "))
    except ValueError:
        print("❌ Código inválido.")
        return

    aluno = encontrar_aluno_por_codigo(codigo)
    if not aluno:
        print("❌ Aluno não encontrado.")
        return

    print(f"Aluno encontrado: {aluno['nome']}")
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 100.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    aluno['notas'] = notas
    print(f"✅ Notas cadastradas com sucesso para {aluno['nome']}.")

# ----------- APURAÇÃO DE RESULTADOS ------------

def apurar_resultados():
    """Calcula média e atualiza a situação dos alunos"""
    for aluno in alunos:
        if aluno['notas']:
            media = sum(aluno['notas']) / len(aluno['notas'])
            aluno['media'] = media
            aluno['situacao'] = 'Aprovado' if media >= 60 else 'Reprovado'
        else:
            aluno['media'] = None
            aluno['situacao'] = 'Matriculado'
    print("\n✅ Situações atualizadas com sucesso!")

# ----------- EXIBIÇÃO DE RESULTADOS ------------

def exibir_resultados():
    """Exibe resultados filtrados e ordenados"""
    print("\n--- Resultados ---")
    print("1. Aprovados\n2. Reprovados\n3. Todos")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        filtrados = list(filter(lambda a: a['situacao'] == 'Aprovado', alunos))
    elif opcao == '2':
        filtrados = list(filter(lambda a: a['situacao'] == 'Reprovado', alunos))
    elif opcao == '3':
        filtrados = alunos
    else:
        print("❌ Opção inválida.")
        return

    if not filtrados:
        print("Nenhum aluno encontrado para esta categoria.")
        return

    print("\nOrdenar por:\n1. Nome\n2. Nota (maior/menor)")
    ordem = input("Escolha: ")

    if ordem == '1':
        filtrados.sort(key=lambda a: a['nome'])
    elif ordem == '2':
        filtrados.sort(key=lambda a: a.get('media', 0), reverse=True)
    else:
        print("❌ Opção inválida. Exibindo sem ordenação.")

    print("\n--- RESULTADOS ---")
    for aluno in filtrados:
        media_str = f"{aluno['media']:.2f}" if aluno['media'] is not None else "-"
        print(f"Nome: {aluno['nome']} | Média: {media_str} | Situação: {aluno['situacao']}")

# ----------- MENU PRINCIPAL ------------

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Notas")
        print("3. Apurar Resultados")
        print("4. Exibir Resultados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                menu_alunos()
            case '2':
                cadastrar_notas()
            case '3':
                apurar_resultados()
            case '4':
                exibir_resultados()
            case '0':
                print("👋 Encerrando o sistema...")
                break
            case _:
                print("❌ Opção inválida. Tente novamente.")

def menu_alunos():
    """Submenu de alunos"""
    while True:
        print("\n--- MENU ALUNOS ---")
        print("1. Cadastrar")
        print("2. Remover")
        print("3. Listar")
        print("4. Ordenar")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                cadastrar_aluno()
            case '2':
                remover_aluno()
            case '3':
                listar_alunos()
            case '4':
                ordenar_alunos()
            case '0':
                break
            case _:
                print("❌ Opção inválida.")

# ----------- EXECUÇÃO DO SISTEMA ------------

if __name__ == "__main__":
    menu_principal()