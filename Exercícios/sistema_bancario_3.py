import textwrap

def menu():
    return input(textwrap.dedent("""
    ================ MENU ================
    [d]  Depositar      [s]  Sacar
    [e]  Extrato        [nc] Nova conta
    [lc] Listar contas  [nu] Novo usuário
    [q]  Sair
    => """))

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        return saldo, extrato, "\n@@@ Operação falhou! O valor informado é inválido. @@@"
    
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    return saldo, extrato, "\n=== Depósito realizado com sucesso! ==="

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        return saldo, extrato, numero_saques, "\n@@@ Operação falhou! Você não tem saldo suficiente. @@@"
    
    if valor > limite:
        return saldo, extrato, numero_saques, "\n@@@ Operação falhou! O valor do saque excede o limite. @@@"
    
    if numero_saques >= limite_saques:
        return saldo, extrato, numero_saques, "\n@@@ Operação falhou! Número máximo de saques excedido. @@@"
    
    if valor <= 0:
        return saldo, extrato, numero_saques, "\n@@@ Operação falhou! O valor informado é inválido. @@@"
    
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, numero_saques, "\n=== Saque realizado com sucesso! ==="

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe um usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, criação de conta cancelada! @@@")

def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada. @@@")
        return
    
    for conta in contas:
        print("=" * 40)
        print(f"Agência:\t{conta['agencia']}")
        print(f"C/C:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
    print("=" * 40)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques, mensagem = sacar(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
            print(mensagem)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, tente novamente.")

main()
