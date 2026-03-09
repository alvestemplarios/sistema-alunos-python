alunos = []

def cadastrar_aluno():
    nome = input("Nome do aluno: ").strip()

    if nome == "":
        print("Nome não pode ficar vazio.")
        return

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
    except:
        print("Digite notas válidas.")
        return

    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "APROVADO"
    elif media >= 5:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\n===== LISTA DE ALUNOS =====")

    for aluno in alunos:
        print("Nome:", aluno["nome"])
        print("Nota 1:", aluno["nota1"])
        print("Nota 2:", aluno["nota2"])
        print("Média:", round(aluno["media"], 2))
        print("Situação:", aluno["situacao"])
        print("----------------------")


while True:

    print("\n===== SISTEMA ESCOLAR =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")