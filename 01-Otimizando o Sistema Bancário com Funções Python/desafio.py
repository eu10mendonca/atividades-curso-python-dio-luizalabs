import os
import random
import textwrap





def carregar_nome_programa() -> None:

    print("""
 ▗▄▄▖▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖     ▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▖ 
▐▌     █  ▐▌     █  ▐▌   ▐▛▚▞▜▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌  █  ▐▌ ▐▌
 ▝▀▚▖  █   ▝▀▚▖  █  ▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌    ▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌▐▌   ▐▛▀▜▌▐▛▀▚▖  █  ▐▌ ▐▌
▗▄▄▞▘▗▄█▄▖▗▄▄▞▘  █  ▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌    ▐▙▄▞▘▐▌ ▐▌▐▌  ▐▌▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▝▚▄▞▘
""")

def carregar_menu_principal() -> None:
    
    menu = """

        1. Cadastrar Usuário
        2. Cadastrar Conta
        3. Listar Usuários Cadastrados
        4. Depositar
        5. Sacar
        6. Extrato
        7. Sair

     """

    print(textwrap.dedent(menu))

def exibir_subtitulo(subtitulo: str) -> None:
    print(subtitulo)

def efetuar_deposito(saldo: float, extrato: str, /) -> tuple[float, str, str]:
    try:        
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        return saldo, extrato, "Operação falhou! O valor informado não é numérico."
    
    if valor < 0:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."
    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"        
    return saldo, extrato, "Depósito realizado com sucesso!"

def efetuar_saque(*, saldo: float, extrato: str, limite: float, numero_saques: int, limite_saques: int) -> tuple[float, str, int, str]:

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        return saldo, extrato, numero_saques, "Operação falhou! O valor informado não é numérico."
    
    msg = ""

    if valor <= 0:
        msg = "Valor inválido!"
    elif valor > saldo:
        msg = "Operação falhou! Você não tem saldo suficiente."
    elif valor > limite:
        msg = "Operação falhou! O valor do saque excede o limite."
    elif numero_saques >= limite_saques:
        msg = "Operação falhou! Número máximo de saques excedido."
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        msg = "Saque realizado com sucesso!"

    return saldo, extrato, numero_saques, msg

def exibir_extrato(saldo: float, /, *, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(lista_usuarios: list[dict]) -> tuple[list[dict], str]:

    try:
        cpf = input("Por favor, informe o CPF do titular da conta, sem pontos e sem dígito: ")
        if existe_item(lista_usuarios, "cpf", cpf):
            return lista_usuarios, "Usuário já cadastrado!"
        
        data_nascimento_titular = input("\nPor favor, informe a data de nascimneto do titular da conta, no formato dd-mm-yyyy: " )
        nome_titular = input("\nPor favor, informe o nome do titular da conta: ")
        input("\nPerfeito. Agora vamos preencher as informações referentes ao endereço do titular da conta. (Pressionar qualquer tecla para continuar...)")
        endereco_logradouro = input("\nPor favor, informe o logradouro: ")
        numero_logradouro = input("\nPor favor, informe o número: ")
        bairro_logradouro = input("\nPor favor, informe o bairro: ")
        cidade_logradouro = input("\nPor favor, informe a cidade: ")
        uf_logradouro = input("\nPor favor, informe o estado: ")

        lista_usuarios.append({"cpf":cpf, "data_nascimento_titular":data_nascimento_titular, "nome_titular":nome_titular,
                               "endereco":{"logradouro":endereco_logradouro, "numero":numero_logradouro, "bairro":bairro_logradouro,
                                           "cidade":cidade_logradouro, "uf":uf_logradouro},})
        #  "conta_corrente":[{"agencia":"","c/c":"", "cpf_titular": cpf}]
        
    except ValueError:
        return lista_usuarios, "O cpf informado é inválido!"
    
    return lista_usuarios, "\nUsuário cadastrado com sucesso!"

def gerar_conta_unica(lista_contas:list[dict]) -> str:
    while True:
        s = f"{random.randint(0, 999_999):06}"   # permite zeros à esquerda
        if s == "0000000":                          # opcional: evitar tudo zero
            continue
        s = f"{s[:5]}-{s[5:]}"
        if existe_item(lista_contas, "numero_conta_corrente", s):
            continue
        return s

def cadastrar_conta(lista_usuarios:list[dict], lista_contas: list[dict]) -> tuple[list[dict], str]:

    if not lista_usuarios:
        return lista_contas, "Nenhum usuário cadastrado no sistema!"
    
    cpf = input("Digite o CPF do usuário para o qual deseja cadastrar a conta: ")
    if not existe_item(lista_usuarios, "cpf", cpf):
        return lista_contas, "Usuário não cadastrado!"

    numero_conta = gerar_conta_unica(lista_contas)
    lista_contas.append({"agencia":"001", "numero_conta_corrente":numero_conta, "cpf_titular":cpf})
    return (lista_contas, "Conta cadastrada com sucesso!")

def listar_usuarios(lista_usuarios: list[dict], lista_contas: list[dict]) -> str:

    def val(v, default="-"):
        if isinstance(v, str):
            v = v.strip()
        return v if v not in (None, "") else default
    
    if not lista_usuarios:
        return "Não existe usuário cadastrado no sistema!"
    
    linha = "#" * 60
    barra = "*" * 60
    
    if len(lista_usuarios) > 0:
        for usuario in lista_usuarios:
            
            endereco = usuario.get("endereco") or {}
            bloco_informacoes_cadastrais = textwrap.dedent(f"""
                {linha}
                Nome do Titular: {val(usuario.get("nome_titular"))}
                Cpf: {val(usuario.get("cpf"))}
                Data de Nascimento: {val(usuario.get("data_nascimento_titular"))}
                Endereço:
                    Logradouro: {val(endereco.get("logradouro"))}
                    Numero: {val(endereco.get("numero"))}
                    Bairro: {val(endereco.get("bairro"))}
                    Cidade: {val(endereco.get("cidade"))}
                    UF: {val(endereco.get("uf"))}
                """)
            print(bloco_informacoes_cadastrais)            
            
            if lista_contas:                

                for i, conta in enumerate(lista_contas, start=1):
                    bloco_conta = textwrap.dedent(f"""
                    Dados Bancários #{i}
                    {barra}    
                        Agência: {val(conta.get("agencia"))}
                        Conta Corrente: {val(conta.get("numero_conta_corrente"))}
                        Titular da Conta (CPF): {val(conta.get("cpf_titular"))}
                    {barra}
                """)
                    print(bloco_conta)
            else:
                print("Nenhuma conta cadastrada.")

            print(linha)
    
    return ""

def opcao_invalida() -> None:        
    carregar_tela_inicial()

def limpar_tela() -> None:
    os.system("cls" if os.name=="nt" else "clear")

def finalizar_app() -> None:
    exibir_subtitulo("\nEncerrando o programa...\n")

def carregar_tela_inicial() -> None:
    limpar_tela()
    carregar_nome_programa()
    carregar_menu_principal()

def existe_item(lista_items:list[dict], chave:str, valor) -> bool:

    if not lista_items:
        return False
    
    """Retorna True se existir algum item cujo valor de `chave` seja igual a `valor`."""
    return any(item.get(chave) == valor for item in lista_items)
   


def main():
    carregar_tela_inicial()

    lista_usuarios:list[dict] = []
    lista_contas:list[dict] = []

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:
        opcao = input("Escolha uma opcão: ")
        try:
            match opcao:
                case "1":
                    limpar_tela()
                    lista_usuarios, msg = cadastrar_usuario(lista_usuarios)
                    input(f"{msg} Pressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial()
                case "2":
                    limpar_tela()
                    lista_contas, msg = cadastrar_conta(lista_usuarios, lista_contas)
                    input(f"{msg} Pressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial()
                case "3":
                    limpar_tela()
                    msg = listar_usuarios(lista_usuarios, lista_contas)
                    input(f"{msg} Pressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial()
                case "4":
                    limpar_tela()
                    saldo, extrato, msg = efetuar_deposito(saldo, extrato)
                    input(f"\n{msg} Pressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial()                
                case "5":
                    limpar_tela()
                    saldo, extrato, numero_saques, msg = efetuar_saque(saldo=saldo, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)
                    input(f"\n{msg} Pressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial() 
                case "6":
                    limpar_tela()
                    exibir_extrato(saldo, extrato=extrato)
                    input("\nPressione qualquer tecla para retornar ao menu principal...")
                    carregar_tela_inicial() 
                case "7":
                    finalizar_app()
                    break
                case _:
                    carregar_tela_inicial()
        except ValueError as e:
            input("Operação falhou! O valor informado é inválido. Pressione qualquer tecla para continuar...")
            carregar_tela_inicial() 



    

if __name__ == "__main__":    
    main()