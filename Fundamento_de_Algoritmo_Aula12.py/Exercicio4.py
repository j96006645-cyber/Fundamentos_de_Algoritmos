def carregar_agenda():
    agenda = {}
    try:
        arquivo = open("agenda.txt", "r")
        for linha in arquivo.readlines():
            partes = linha.strip().split(",")
            if len(partes) == 4:
                nome, sobrenome, tel, email = partes
                agenda[nome.lower()] = [nome, sobrenome, tel, email]
        arquivo.close()
    except FileNotFoundError:
        pass
    return agenda

def salvar_agenda(agenda):
    arquivo = open("agenda.txt", "w")
    for dados in agenda.values():
        arquivo.write(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
    arquivo.close()

agenda = carregar_agenda()

while True:
    print("\n1 - Novo contato\n2 - Procura\n3 - Atualiza contato\n4 - Apaga contato\n0 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        tel = input("Telefone: ")
        email = input("E-mail: ")
        agenda[nome.lower()] = [nome, sobrenome, tel, email]
        salvar_agenda(agenda)
        
    elif opcao == "2":
        nome_proc = input("Digite o nome para procurar: ").lower()
        if nome_proc in agenda:
            contato = agenda[nome_proc]
            print(f"Nome: {contato[0]} {contato[1]} | Tel: {contato[2]} | E-mail: {contato[3]}")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "3":
        nome_act = input("Digite o nome do contato que deseja atualizar: ").lower()
        if nome_act in agenda:
            print("Insira os novos dados:")
            sobrenome = input("Sobrenome: ")
            tel = input("Telefone: ")
            email = input("E-mail: ")
            agenda[nome_act] = [agenda[nome_act][0], sobrenome, tel, email]
            salvar_agenda(agenda)
        else:
            print("Contato não encontrado.")
            
    elif opcao == "4":
        nome_del = input("Digite o nome para apagar: ").lower()
        if nome_del in agenda:
            del agenda[nome_del]
            salvar_agenda(agenda)
            print("Contato apagado.")
        else:
            print("Contato não encontrado.")
            
    elif opcao == "0":
        break
