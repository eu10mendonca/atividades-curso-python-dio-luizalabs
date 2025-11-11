import functools
import os
import random
import textwrap
import time
from collections.abc import Callable
from datetime import datetime
from typing import Any


def registrar_log(
    *, operacao: str
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Cria um decorador parametrizado para registrar logs de início e fim de execução.

    O decorador exibe no console informações de data e hora quando uma operação
    específica é iniciada e concluída, conforme definido pelo parâmetro `operacao`.
    Pode ser aplicado a funções de exibição ou regras de negócio, sem alterar
    seus retornos originais.

    Args:
        operacao (str): Nome descritivo da operação sendo registrada no log.

    Returns:
        Callable[[Callable[..., Any]], Callable[..., Any]]:
            Uma função decoradora que, por sua vez, retorna uma função wrapper
            responsável por imprimir os logs e executar a função original.
    """

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        # serve para preservar o nome da função que está com o decorator.
        # Se não utilizar, quando chamar funcao.__name__ vai retornar "wrapper" e não o nome da função
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(
                f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Iniciando operação: {operacao}"
            )
            resultado = function(*args, **kwargs)
            print(
                f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Operação concluída: {operacao}"
            )
            return resultado

        return wrapper

    return decorator


@registrar_log(operacao="gerar_extrato")
def exibir_extrato_console(function: Callable[..., Any], *args, **kwargs) -> None:
    """Executa a função geradora de extrato e exibe o resultado no console.

    A função recebe uma função responsável por montar o extrato, executa-a com
    os argumentos fornecidos e imprime o texto retornado, caso exista.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado)


@registrar_log(operacao="efetuar_saque")
def exibir_operacao_saque_console(
    function: Callable[..., Any], *args, **kwargs
) -> tuple[Any, ...]:
    """Executa a função de saque, exibe a mensagem de retorno e repassa o resultado.

    A função encapsula a chamada da função de saque, imprimindo somente a
    mensagem de feedback ao usuário e retornando a tupla completa com os dados
    atualizados da operação.
    """
    resultado: tuple = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado[3])

    return resultado


@registrar_log(operacao="efetuar_deposito")
def exibir_operacao_deposito_console(
    function: Callable[..., Any], *args, **kwargs
) -> tuple[Any, ...]:
    """Executa a função de depósito, exibe a mensagem de retorno e repassa o resultado.

    A função chama a função de depósito recebida, exibe a mensagem de status da
    operação ao usuário e devolve a tupla com saldo, extrato e mensagem.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado[2])

    return resultado


@registrar_log(operacao="listar_usuarios")
def exibir_lista_usuarios_console(
    function: Callable[..., Any], *args, **kwargs
) -> None:
    """Executa a função de listagem de usuários e exibe o conteúdo gerado.

    A função é responsável por chamar a função de listagem, obtendo o texto
    formatado com os usuários e contas cadastradas, e imprimir o resultado no
    console.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado)


@registrar_log(operacao="cadastrar_usuario")
def exibir_cadastro_usuario_console(
    function: Callable[..., Any], *args, **kwargs
) -> tuple[Any, ...]:
    """Executa a função de cadastro de usuário e exibe a mensagem retornada.

    A função encapsula o processo de cadastro de usuário, mostrando apenas a
    mensagem de sucesso ou erro ao usuário e retornando a tupla completa com a
    lista atualizada e a mensagem.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado[1])

    return resultado


@registrar_log(operacao="cadastrar_conta")
def exibir_cadastro_conta_console(
    function: Callable[..., Any], *args, **kwargs
) -> tuple[Any, ...]:
    """Executa a função de cadastro de conta e exibe a mensagem retornada.

    A função chama a função de criação de conta corrente, imprime a mensagem de
    resultado para o usuário e devolve a tupla com a lista de contas atualizada
    e a mensagem.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado[1])

    return resultado


def carregar_nome_programa() -> None:
    """Exibe no terminal o banner ASCII que apresenta o nome do programa."""
    print(
        """
 ▗▄▄▖▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖     ▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▖ 
▐▌     █  ▐▌     █  ▐▌   ▐▛▚▞▜▌▐▌ ▐▌    ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌  █  ▐▌ ▐▌
 ▝▀▚▖  █   ▝▀▚▖  █  ▐▛▀▀▘▐▌  ▐▌▐▛▀▜▌    ▐▛▀▚▖▐▛▀▜▌▐▌ ▝▜▌▐▌   ▐▛▀▜▌▐▛▀▚▖  █  ▐▌ ▐▌
▗▄▄▞▘▗▄█▄▖▗▄▄▞▘  █  ▐▙▄▄▖▐▌  ▐▌▐▌ ▐▌    ▐▙▄▞▘▐▌ ▐▌▐▌  ▐▌▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌▗▄█▄▖▝▚▄▞▘
"""
    )


def carregar_menu_principal() -> None:
    """Exibe o menu de opções principais com identação corrigida via textwrap."""

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
    """Mostra um subtítulo simples no console, destacando a etapa atual do fluxo."""
    print(subtitulo)


def efetuar_deposito(saldo: float, extrato: str, /) -> tuple[float, str, str]:
    """Processa um depósito e atualiza saldo/extrato após validar o valor.

    Args:
        saldo (float): Saldo atual disponível para movimentações.
        extrato (str): Histórico de transações em formato de string.

    Returns:
        tuple[float, str, str]: Novo saldo, extrato atualizado e mensagem da operação.
    """
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        return saldo, extrato, "Operação falhou! O valor informado não é numérico."

    if valor <= 0:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."

    saldo += valor
    extrato += f"\nDepósito:"
    str_deposito = f"R$ {valor:.2f}"
    extrato += f"{str_deposito:>31}"
    return saldo, extrato, "Depósito realizado com sucesso!"


def efetuar_saque(
    *, saldo: float, extrato: str, limite: float, numero_saques: int, limite_saques: int
) -> tuple[float, str, int, str]:
    """Realiza uma operação de saque, atualizando o saldo, o extrato e o número de saques.

    A função solicita ao usuário o valor do saque e executa validações relacionadas
    ao saldo disponível, limite por operação e limite diário de saques.
    Em caso de sucesso, o valor é debitado e o extrato atualizado.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico de transações em formato de string.
        limite (float): Valor máximo permitido por saque.
        numero_saques (int): Quantidade de saques já realizados no dia.
        limite_saques (int): Número máximo de saques permitidos por dia.

    Returns:
        tuple[float, str, int, str]:
            - Novo saldo após a conclusão de saque.
            - Extrato atualizado com a transação (se bem-sucedida).
            - Número atualizado de saques realizados.
            - Mensagem indicando o resultado da operação (sucesso ou erro).
    """

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        return (
            saldo,
            extrato,
            numero_saques,
            "Operação falhou! O valor informado não é numérico.",
        )

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
        extrato += f"\nSaque:"
        str_saque = f"R$ {valor:.2f}"
        extrato += f"{str_saque:>34}"
        numero_saques += 1
        msg = "Saque realizado com sucesso!"

    return saldo, extrato, numero_saques, msg


def gerar_extrato(saldo: float, /, *, extrato: str) -> str:
    """Monta e retorna o texto formatado do extrato e do saldo atual.

    Args:
        saldo (float): Valor de saldo disponível que será mostrado ao final do extrato.
        extrato (str): Texto consolidado com as transações realizadas.

    Returns:
        str: Texto formatado contendo o cabeçalho, movimentações e saldo final.
    """
    msg = " EXTRATO ".center(40, "=")
    msg += "\nSem movimentações.\n" if not extrato else extrato
    msg += f"\n\n\nSaldo:"
    str_saldo = f"R$ {saldo:.2f}"
    msg += f"{str_saldo:>34}"
    msg += "\n" + "".center(40, "=") + "\n"

    return msg


def validar_cpf(cpf: str) -> bool:
    """Valida se o CPF informado é composto por 11 dígitos numéricos.

    A função não realiza validação matemática de CPF (dígitos verificadores),
    apenas garante que o valor possui o comprimento e formato corretos.

    Args:
        cpf (str): CPF a ser validado, contendo apenas números.

    Returns:
        bool: True se o CPF for válido (11 dígitos numéricos), False caso contrário.
    """
    return cpf.isdigit() and len(cpf) == 11


def validar_data(data_str: str) -> bool:
    """Valida se uma data está no formato 'dd-mm-yyyy' e representa uma data real.

    A função utiliza o módulo datetime para verificar se a data informada é válida,
    considerando meses de 30/31 dias e anos bissextos.

    Args:
        data_str (str): Data informada pelo usuário no formato 'dd-mm-yyyy'.

    Returns:
        bool: True se a data for válida e estiver no formato correto, False caso contrário.
    """
    try:
        datetime.strptime(data_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def cadastrar_usuario(lista_usuarios: list[dict]) -> tuple[list[dict], str]:
    """Registra um novo usuário solicitando dados pessoais e endereço.

    A função solicita ao usuário informações de CPF, nome, data de nascimento
    e endereço, validando se o CPF já está cadastrado. Em caso de sucesso,
    adiciona o novo registro à lista existente.

    Args:
        lista_usuarios (list[dict]): Lista atual de usuários cadastrados,
            onde cada item representa um usuário com seus dados pessoais e endereço.

    Returns:
        tuple[list[dict], str]:
            - Lista atualizada de usuários.
            - Mensagem indicando o resultado da operação (sucesso ou erro).
    """

    cpf = input(
        "Por favor, informe o CPF do titular da conta, sem pontos e sem traços: "
    )
    while not validar_cpf(cpf):
        cpf = input(
            "CPF Inválido! Por favor, informe o CPF do titular da conta, sem pontos e sem traços: "
        )

    if existe_item(lista_usuarios, "cpf", cpf):
        return lista_usuarios, "Usuário já cadastrado!"

    data_nascimento_titular = input(
        "\nPor favor, informe a data de nascimento do titular da conta, no formato dd-mm-yyyy: "
    )

    while not validar_data(data_nascimento_titular):
        data_nascimento_titular = input(
            "Data de nascimento inválida! Por favor, informe a data de nascimento do titular da conta, no formato dd-mm-yyyy: "
        )

    nome_titular = input("\nPor favor, informe o nome do titular da conta: ")
    input(
        "\nPerfeito. Agora vamos preencher as informações referentes ao endereço do titular da conta. (Pressionar qualquer tecla para continuar...)"
    )
    endereco_logradouro = input("\nPor favor, informe o logradouro: ")
    numero_logradouro = input("\nPor favor, informe o número: ")
    bairro_logradouro = input("\nPor favor, informe o bairro: ")
    cidade_logradouro = input("\nPor favor, informe a cidade: ")
    uf_logradouro = input("\nPor favor, informe o estado: ")

    lista_usuarios.append(
        {
            "cpf": cpf,
            "data_nascimento_titular": data_nascimento_titular,
            "nome_titular": nome_titular,
            "endereco": {
                "logradouro": endereco_logradouro,
                "numero": numero_logradouro,
                "bairro": bairro_logradouro,
                "cidade": cidade_logradouro,
                "uf": uf_logradouro,
            },
        }
    )

    return lista_usuarios, "\nUsuário cadastrado com sucesso!"


def gerar_conta_unica(lista_contas: list[dict]) -> str:
    """Gera um número de conta corrente único e formatado.

    A função cria um número de conta aleatório com seis dígitos,
    garantindo que ele não se repita em relação às contas já existentes
    e que seja formatado com um hífen antes do último dígito.
    Exemplo de formato: "12345-6".

    Args:
        lista_contas (list[dict]): Lista de contas já cadastradas, utilizada
            para verificar duplicidades do número gerado.

    Returns:
        str: Número de conta corrente único e formatado (ex: "12345-6").
    """
    while True:
        s = f"{random.randint(0, 999_999):06}"  # permite zeros à esquerda
        if s == "000000":  # opcional: evitar tudo zero
            continue
        s = f"{s[:5]}-{s[5:]}"
        if existe_item(lista_contas, "numero_conta_corrente", s):
            continue
        return s


def cadastrar_conta(
    lista_usuarios: list[dict], lista_contas: list[dict]
) -> tuple[list[dict], str]:
    """
    Cria uma nova conta corrente vinculada a um usuário existente.

    A função verifica se há usuários cadastrados, valida se o CPF informado
    pertence a um usuário existente e, em caso de sucesso, gera um número
    de conta único e adiciona o novo registro à lista de contas.

    Args:
        lista_usuarios (list[dict]): Lista de usuários cadastrados.
        lista_contas (list[dict]): Lista de contas já cadastradas.

    Returns:
        tuple[list[dict], str]:
            - Lista de contas atualizada.
            - Mensagem indicando o resultado da operação.
    """
    if not lista_usuarios:
        return lista_contas, "Nenhum usuário cadastrado no sistema!"

    cpf = input("Digite o CPF do usuário para o qual deseja cadastrar a conta: ")
    if not existe_item(lista_usuarios, "cpf", cpf):
        return lista_contas, "Usuário não cadastrado!"

    numero_conta = gerar_conta_unica(lista_contas)
    lista_contas.append(
        {"agencia": "0001", "numero_conta_corrente": numero_conta, "cpf_titular": cpf}
    )
    return (lista_contas, "Conta cadastrada com sucesso!")


def valor_default(v, default: str = "-") -> str:
    if isinstance(v, str):
        v = v.strip()
    return v if v not in (None, "") else default


def listar_usuarios(lista_usuarios: list[dict], lista_contas: list[dict]) -> str:
    """Gera o texto formatado com os usuários cadastrados e seus dados bancários.

    Percorre a lista de usuários exibindo informações cadastrais e, quando houver,
    as contas correntes associadas. Retorna uma mensagem de status e o conteúdo
    formatado que pode ser utilizado pelo fluxo do menu.

    Args:
        lista_usuarios (list[dict]): Lista de usuários cadastrados.
        lista_contas (list[dict]): Lista de contas cadastradas.

    Returns:
        str: Texto contendo a listagem formatada e uma mensagem de conclusão.
    """

    if not lista_usuarios:
        return "Não existe usuário cadastrado no sistema!"

    headers_tabela_informacoes_cadastrais = (
        f"|{'NOME'.center(41)}|{'CPF'.center(17)}|{'DATA DE NASCIMENTO'.center(22)}|"
    )
    headers_tabela_enderecos_1 = (
        f"|{'LOGRADOURO'.center(40)}|{'NUMERO'.center(18)}|{'BAIRRO'.center(22)}|"
    )
    headers_tabela_enderecos_2 = (
        f"|{'CIDADE'.center(32)}|{'UF'.center(6)}|{''.center(42, '#')}|"
    )
    headers_tabela_contas = f"|{'AGÊNCIA'.center(27)}|{'CONTA CORRENTE'.center(27)}|{'TITULAR DA CONTA (CPF)'.center(26)}|"
    separador_tabela = "-" * 84
    separador_secao_tabela = f"|{''.center(82)}|"

    lista_usuarios_formatada = ""

    if lista_usuarios:

        for i, usuario in enumerate(lista_usuarios, start=1):

            endereco_usuario = usuario.get("endereco") or {}
            cpf_usuario = str(usuario.get("cpf"))
            nome_usuario = str(valor_default(usuario.get("nome_titular")))
            data_nascimento_usuario = str(
                valor_default(usuario.get("data_nascimento_titular"))
            )
            logradouro_usuario = valor_default(endereco_usuario.get("logradouro"))
            numero_endereco_usuario = valor_default(endereco_usuario.get("numero"))
            bairro_endereco_usuario = valor_default(endereco_usuario.get("bairro"))
            cidade_endereco_usuario = valor_default(endereco_usuario.get("cidade"))
            uf_endereco_usuario = valor_default(endereco_usuario.get("uf"))

            lista_usuarios_formatada += f"\n\nUsuário #{i}"
            # print(f"\nUsuário #{i}")
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += (
                f"\n|{'*INFORMAÇÕES CADASTRAIS*'.center(len(separador_tabela) - 2)}|"
            )
            # print(f"|{'*INFORMAÇÕES CADASTRAIS*'.center(len(separador_tabela) - 2)}|")
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n{headers_tabela_informacoes_cadastrais}"
            # print(headers_tabela_informacoes_cadastrais)
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n|{nome_usuario.center(41)}|{cpf_usuario.center(17)}|{data_nascimento_usuario.center(22)}|"
            # print(
            #     f"|{nome_usuario.center(41)}|{cpf_usuario.center(17)}|{data_nascimento_usuario.center(22)}|"
            # )
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n{separador_secao_tabela}"
            # print(separador_secao_tabela)

            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += (
                f"\n|{'*ENDEREÇOS CADASTRADOS*'.center(len(separador_tabela) - 2)}|"
            )
            # print(f"|{'*ENDEREÇOS CADASTRADOS*'.center(len(separador_tabela) - 2)}|")
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n{headers_tabela_enderecos_1}"
            # print(headers_tabela_enderecos_1)
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n|{logradouro_usuario.center(40)}|{numero_endereco_usuario.center(18)}|{bairro_endereco_usuario.center(22)}|"
            # print(
            #     f"|{logradouro_usuario.center(40)}|{numero_endereco_usuario.center(18)}|{bairro_endereco_usuario.center(22)}|"
            # )
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n{headers_tabela_enderecos_2}"
            # print(headers_tabela_enderecos_2)
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)
            lista_usuarios_formatada += f"\n|{cidade_endereco_usuario.center(32)}|{uf_endereco_usuario.center(6)}|{''.center(42, '#')}|"
            # print(
            #     f"|{cidade_endereco_usuario.center(32)}|{uf_endereco_usuario.center(6)}|{''.center(42, '#')}|"
            # )
            lista_usuarios_formatada += f"\n{separador_tabela}"
            # print(separador_tabela)

            if existe_item(lista_contas, "cpf_titular", cpf_usuario):

                lista_usuarios_formatada += f"\n{separador_secao_tabela}"
                # print(separador_secao_tabela)
                lista_usuarios_formatada += f"\n{separador_tabela}"
                # print(separador_tabela)
                lista_usuarios_formatada += (
                    f"\n|{'*DADOS BANCÁRIOS*'.center(len(separador_tabela) - 2)}|"
                )
                # print(f"|{'*DADOS BANCÁRIOS*'.center(len(separador_tabela) - 2)}|")
                lista_usuarios_formatada += f"\n{separador_tabela}"
                # print(separador_tabela)
                lista_usuarios_formatada += f"\n{headers_tabela_contas}"
                # print(headers_tabela_contas)
                lista_usuarios_formatada += f"\n{separador_tabela}"
                # print(separador_tabela)

                for conta in lista_contas:
                    if conta.get("cpf_titular") == cpf_usuario:

                        agencia_conta_usuario = str(valor_default(conta.get("agencia")))
                        numero_conta_usuario = str(
                            valor_default(conta.get("numero_conta_corrente"))
                        )
                        cpf_titular = str(valor_default(conta.get("cpf_titular")))
                        lista_usuarios_formatada += f"\n|{agencia_conta_usuario.center(27)}|{numero_conta_usuario.center(27)}|{cpf_titular.center(26)}|"
                        # print(
                        #     f"|{agencia_conta_usuario.center(27)}|{numero_conta_usuario.center(27)}|{cpf_titular.center(26)}|"
                        # )
                        lista_usuarios_formatada += f"\n{separador_tabela}"
                        # print(separador_tabela)

                        # """
                        # )

                        # Exemplo de apresentação dos elementos da tabela utilizando aspas triplas.
                        # bloco_conta = textwrap.dedent(
                        #     f"""\
                        #     |    {agencia}   |       {conta_corrente}       |         {cpf_titular}          |
                        #     -----------------------------------------------------------------\
                        # """
                        # )
                        # print(bloco_conta)

            else:
                lista_usuarios_formatada += f"\n{separador_secao_tabela}"
                # print(separador_secao_tabela)
                lista_usuarios_formatada += f"\n{separador_tabela}"
                # print(separador_tabela)
                lista_usuarios_formatada += (
                    f"\n|{'*DADOS BANCÁRIOS*'.center(len(separador_tabela) - 2)}|"
                )
                # print(f"|{'*DADOS BANCÁRIOS*'.center(len(separador_tabela) - 2)}|")
                lista_usuarios_formatada += f"\n{separador_tabela}"
                # print(separador_tabela)
                lista_usuarios_formatada += (
                    f"\n|{' Nenhuma conta cadastrada.'.ljust(82)}|"
                )
                # print(f"|{' Nenhuma conta cadastrada.'.ljust(82)}|")
                lista_usuarios_formatada += f"\n{separador_tabela}\n"
                # print(separador_tabela + "\n")

    return f"{lista_usuarios_formatada}\nListagem concluída."


def limpar_tela() -> None:
    """
    Limpa o conteúdo do terminal de acordo com o sistema operacional.
    """
    os.system("cls" if os.name == "nt" else "clear")


def finalizar_app() -> None:
    """
    Exibe uma mensagem de encerramento e finaliza a aplicação.
    """
    exibir_subtitulo("\nEncerrando o programa...\n")


def carregar_tela_inicial() -> None:
    """
    Limpa a tela e exibe o banner e o menu principal da aplicação.
    """
    limpar_tela()
    carregar_nome_programa()
    carregar_menu_principal()


def existe_item(lista_items: list[dict], chave: str, valor) -> bool:
    """
    Verifica se existe na lista algum item cujo valor para a chave informada
    seja igual ao valor fornecido.

    Args:
        lista_items (list[dict]): Lista de dicionários que será pesquisada.
        chave (str): Nome da chave a ser verificada em cada item.
        valor: Valor esperado associado à chave.

    Returns:
        bool: True se algum item corresponder ao critério, False caso contrário.
    """
    if not lista_items:
        return False

    return any(item.get(chave) == valor for item in lista_items)


def carregar_dados_mock(
    lista_usuarios: list[dict], lista_contas: list[dict]
) -> tuple[list[dict], list[dict]]:
    """
    Carrega usuários e contas de exemplo para auxiliar em testes locais.

    A função popula as listas de usuários e contas informadas com dados fixos,
    simulando um cenário já preenchido para facilitar a validação das
    funcionalidades do sistema bancário.

    Args:
        lista_usuarios (list[dict]): Lista de usuários que será populada com dados de teste.
        lista_contas (list[dict]): Lista de contas que será populada com dados de teste.

    Returns:
        tuple[list[dict], list[dict]]: As listas de usuários e contas atualizadas com os dados mock.
    """

    lista_usuarios.extend(
        [
            {
                "cpf": "01234567890",
                "data_nascimento_titular": "24-04-1964",
                "nome_titular": "Sebastiana M. de Carvalho",
                "endereco": {
                    "logradouro": "Rua nova",
                    "numero": "1",
                    "bairro": "Bairro Teste",
                    "cidade": "Cidade teste",
                    "uf": "PE",
                },
            },
            {
                "cpf": "11111111111",
                "data_nascimento_titular": "01-01-2001",
                "nome_titular": "Maria José da Silva",
                "endereco": {
                    "logradouro": "Rua velha",
                    "numero": "2",
                    "bairro": "Bairro Teste 2",
                    "cidade": "Cidade Teste 2",
                    "uf": "PE",
                },
            },
        ]
    )
    lista_contas.extend(
        [
            {
                "agencia": "0001",
                "numero_conta_corrente": "12345-6",
                "cpf_titular": "01234567890",
            },
            {
                "agencia": "0001",
                "numero_conta_corrente": "45789-0",
                "cpf_titular": "01234567890",
            },
        ]
    )

    return lista_usuarios, lista_contas


def main():
    """
    Função principal que inicializa o estado da aplicação e controla
    o loop do menu interativo do sistema bancário.
    """
    carregar_tela_inicial()

    lista_usuarios: list[dict] = []
    lista_contas: list[dict] = []

    # Descomente a linha abaixo apenas para testes locais:
    # carregar_dados_mock(lista_usuarios, lista_contas)

    saldo = 0
    valor_limite_saque = 500
    extrato = ""
    numero_saques = 0
    QTD_LIMITE_SAQUES = 3

    while True:
        opcao = input("Escolha uma opcão: ")

        match opcao:
            case "1":
                limpar_tela()
                lista_usuarios, *_ = exibir_cadastro_usuario_console(
                    cadastrar_usuario, lista_usuarios
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "2":
                limpar_tela()
                # lista_contas, msg = cadastrar_conta(lista_usuarios, lista_contas)
                # print(msg)
                lista_contas, *_ = exibir_cadastro_conta_console(
                    cadastrar_conta, lista_usuarios, lista_contas
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "3":
                limpar_tela()
                # msg = listar_usuarios(lista_usuarios, lista_contas)
                # print(msg)
                exibir_lista_usuarios_console(
                    listar_usuarios, lista_usuarios, lista_contas
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "4":
                limpar_tela()
                saldo, extrato, *_ = exibir_operacao_deposito_console(
                    efetuar_deposito, saldo, extrato
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "5":
                limpar_tela()
                saldo, extrato, numero_saques, *_ = exibir_operacao_saque_console(
                    efetuar_saque,
                    saldo=saldo,
                    extrato=extrato,
                    limite=valor_limite_saque,
                    limite_saques=QTD_LIMITE_SAQUES,
                    numero_saques=numero_saques,
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "6":
                limpar_tela()
                exibir_extrato_console(gerar_extrato, saldo, extrato=extrato)
                # print(f"\n{msg}")
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "7":
                finalizar_app()
                break
            case _:
                carregar_tela_inicial()


if __name__ == "__main__":
    main()
