def cadastrar_paciente(pacientes):
    print("\n--- CADASTRO DE PACIENTE ---")

    # 1. Entrada de Nome
    nome = input("Nome do paciente: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return

    # 2. Entrada e Tratamento de Erro para Idade
    while True:
        try:
            idade_str = input("Idade: ")
            idade = int(idade_str)
            if idade <= 0 or idade > 120:
                print("Erro: Idade inválida. Deve ser um número positivo (máx 120).")
                continue
            break
        except ValueError:
            print("Erro: A idade deve ser um número inteiro.")

    # 3. Entrada de Telefone
    telefone = input("Telefone (Ex: (11) 99999-9999): ").strip()

    # 4. Armazenamento em Dicionário e Lista
    paciente = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone
    }
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def ver_estatisticas(pacientes):
    print("\n--- ESTATÍSTICAS ---")

    num_pacientes = len(pacientes)
    print(f"Número total de pacientes cadastrados: {num_pacientes}")

    if num_pacientes == 0:
        print("Nenhum paciente cadastrado para calcular estatísticas.")
        return

    # Cálculo da Idade Média
    idades = [p['idade'] for p in pacientes]
    idade_media = sum(idades) / num_pacientes
    print(f"Idade média dos pacientes: {idade_media:.2f} anos")

    # Paciente mais novo e mais velho
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])

    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)")
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)")

def buscar_paciente(pacientes):
    print("\n--- BUSCAR PACIENTE ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    termo_busca = input("Digite o nome ou parte do nome do paciente: ").strip().lower()

    resultados = [
        p for p in pacientes
        if termo_busca in p['nome'].lower()
    ]

    if resultados:
        print("\n--- Resultados da Busca ---")
        for p in resultados:
            print(f"Nome: {p['nome']}, Idade: {p['idade']}, Telefone: {p['telefone']}")
    else:
        print(f"Nenhum paciente encontrado com o nome '{termo_busca}'.")

def listar_pacientes(pacientes):
    print("\n--- LISTA DE PACIENTES CADASTRADOS ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    # Cabeçalho da tabela
    print(f"{'Nome':<30} | {'Idade':<5} | {'Telefone':<15}")
    print("-" * 55)

    # Dados dos pacientes
    for p in pacientes:
        print(f"{p['nome']:<30} | {p['idade']:<5} | {p['telefone']:<15}")

def menu():
    pacientes = [] # Lista principal para armazenar os dicionários de pacientes

    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("-" * 28)

        # Tratamento de erro para a opção do menu
        try:
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_paciente(pacientes)
            elif opcao == '2':
                ver_estatisticas(pacientes)
            elif opcao == '3':
                buscar_paciente(pacientes)
            elif opcao == '4':
                listar_pacientes(pacientes)
            elif opcao == '5':
                print("Encerrando o sistema. Até mais!")
                break
            else:
                print("Opção inválida. Por favor, escolha um número de 1 a 5.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

# Execução do programa
if __name__ == "__main__":
    menu()
