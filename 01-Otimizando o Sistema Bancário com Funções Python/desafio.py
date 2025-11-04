import os
import textwrap





def carregar_nome_programa() -> None:

    print('''
 ▗▄▄▖▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖     ▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▖ 
▐▌     █  ▐▌     █  ▐▌   ▐▛▚▞▜▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌  █  ▐▌ ▐▌
 ▝▀▚▖  █   ▝▀▚▖  █  ▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌    ▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌▐▌   ▐▛▀▜▌▐▛▀▚▖  █  ▐▌ ▐▌
▗▄▄▞▘▗▄█▄▖▗▄▄▞▘  █  ▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌    ▐▙▄▞▘▐▌ ▐▌▐▌  ▐▌▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▝▚▄▞▘
''')

def carregar_menu_principal() -> None:
    
    menu = """

        1. [d] Depositar
        2. [s] Sacar
        3. [e] Extrato
        4. [q] Sair

     """

    print(textwrap.dedent(menu))


def exibir_subtitulo(subtitulo: str) -> None:
    print(subtitulo)


def efetuar_deposito(*, saldo: float, extrato: str) -> tuple[float, str]:
    valor = float(input('Informe o valor do depósito: '))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def efetuar_saque(*, saldo: float, extrato: str, limite: float, numero_saques: int, limite_saques: int) -> tuple[float, str, int]:
    valor = float(input('Informe o valor do saque: '))

    if valor <= 0:
        print('Valor inválido!')
    elif valor > saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques > limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato, numero_saques

def exibir_extrato(saldo: float, extrato: str) -> None:
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def opcao_invalida() -> None:        
    carregar_tela_inicial()

def limpar_tela() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def finalizar_app() -> None:
    exibir_subtitulo('\nEncerrando o programa...\n')


def carregar_tela_inicial() -> None:
    limpar_tela()
    carregar_nome_programa()
    carregar_menu_principal()


def main():

    carregar_tela_inicial()

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:
        opcao = input('Escolha uma opcão: ')
        try:
            match opcao:            
                case 'd':
                    limpar_tela()
                    saldo, extrato = efetuar_deposito(saldo=saldo, extrato=extrato)
                    input('\nDepósito realizado com sucesso! Pressione qualquer tecla para retornar ao menu principal...')
                    carregar_tela_inicial()                
                case 's':
                    limpar_tela()
                    saldo, extrato, numero_saques = efetuar_saque(saldo=saldo, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)
                    input('\nSaque realizado com sucesso! Pressione qualquer tecla para retornar ao menu principal...')
                    carregar_tela_inicial() 
                case 'e':
                    limpar_tela()
                    exibir_extrato(saldo=saldo, extrato=extrato)
                    input('\nPressione qualquer tecla para retornar ao menu principal...')
                    carregar_tela_inicial() 
                case 'q':
                    finalizar_app()
                    break
                case _:
                    carregar_tela_inicial()
        except ValueError as e:
            input("Operação falhou! O valor informado é inválido. Pressione qualquer tecla para continuar...")
            carregar_tela_inicial() 



    

if __name__ == '__main__':    
    main()