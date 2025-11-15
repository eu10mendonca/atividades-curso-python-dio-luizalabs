import functools
import os
import random
import textwrap
import time
from collections.abc import Callable, Iterator
from datetime import datetime
from operator import itemgetter
from typing import Any


def registrar_log(
    *, operacao: str
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Fábrica de decoradores para registrar logs de início e fim de execução.

    O decorador permite registrar no console informações sobre quando determinada
    operação iniciou e terminou, incluindo data e hora. Ele não altera o retorno
    da função decorada, apenas adiciona o comportamento de log.

    Args:
        operacao (str): Nome da operação a ser exibida nos logs.

    Returns:
        Callable[[Callable[..., Any]], Callable[..., Any]]:
            Uma função decoradora que envolve a função original com um wrapper
            responsável por imprimir os logs e repassar o retorno original.
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

    A função encapsula a chamada da função de saque, imprimindo apenas a
    mensagem de feedback ao usuário e retornando a tupla completa com o número
    de saques atualizado, a lista de contas e a mensagem de status.

    Args:
        function (Callable[..., Any]): Função responsável por realizar a
            operação de saque.
        *args: Argumentos posicionais repassados para a função de saque.
        **kwargs: Argumentos nomeados repassados para a função de saque.

    Returns:
        tuple[Any, ...]: Tupla contendo o número de saques atualizado, a lista
            de contas modificada (se aplicável) e a mensagem da operação.
    """
    resultado: tuple = function(*args, **kwargs)
    if resultado:
        print(f"\n" + resultado[2])

    return resultado


@registrar_log(operacao="efetuar_deposito")
def exibir_operacao_deposito_console(
    function: Callable[..., Any], *args, **kwargs
) -> tuple[Any, ...]:
    """Executa a função de depósito, exibe a mensagem de retorno e repassa o resultado.

    A função chama a função de depósito recebida, exibe a mensagem de status da
    operação ao usuário e devolve a tupla contendo a lista de contas
    (possivelmente atualizada) e a mensagem resultante.

    Args:
        function (Callable[..., Any]): Função responsável por realizar a
            operação de depósito.
        *args: Argumentos posicionais repassados para a função de depósito.
        **kwargs: Argumentos nomeados repassados para a função de depósito.

    Returns:
        tuple[Any, ...]: Tupla contendo a lista de contas (atualizada, se o
            depósito for efetuado) e a mensagem da operação.
    """
    resultado = function(*args, **kwargs)
    if resultado:
        print("\n" + resultado[1])

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
    lista de usuários atualizada e a mensagem.

    Args:
        function (Callable[..., Any]): Função responsável por cadastrar o
            usuário.
        *args: Argumentos posicionais repassados para a função de cadastro.
        **kwargs: Argumentos nomeados repassados para a função de cadastro.

    Returns:
        tuple[Any, ...]: Tupla contendo a lista de usuários atualizada e a
            mensagem da operação.
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
    e a mensagem da operação.

    Args:
        function (Callable[..., Any]): Função responsável por cadastrar a conta.
        *args: Argumentos posicionais repassados para a função de cadastro.
        **kwargs: Argumentos nomeados repassados para a função de cadastro.

    Returns:
        tuple[Any, ...]: Tupla contendo a lista de contas atualizada e a
            mensagem da operação.
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


def atualizar_extrato(
    *, extrato: dict[str, list[dict[str, Any]]], operacao: str, valor: float
) -> dict[str, list[dict[str, Any]]]:
    """
    Atualiza o extrato de uma conta adicionando um novo registro de operação.

    Acrescenta ao dicionário `extrato` uma entrada na chave da operação
    (por exemplo: "deposito", "saque"), contendo o valor, a data/hora no
    formato "YYYY-MM-DD HH:MM:SS" e a descrição da operação.

    Args:
        extrato (dict[str, list[dict[str, Any]]]): Estrutura de extrato da conta,
            onde cada chave é o tipo da operação e o valor é a lista de registros.
        operacao (str): Identificador da operação (ex.: "deposito", "saque").
        valor (float): Valor monetário movimentado (positivo).

    Returns:
        dict[str, list[dict[str, Any]]]: O dicionário de extrato atualizado.
    """
    extrato.setdefault(operacao, []).append(
        {
            "valor": valor,
            "data": time.strftime("%Y-%m-%d %H:%M:%S"),
            "descrição": {"deposito": "Depósito", "saque": "Saque"}.get(
                operacao, operacao.title()
            ),
        }
    )
    return extrato


def recuperar_conta(lista_contas: list[dict[str, Any]]) -> dict[str, Any] | str:
    """Recupera uma conta bancária a partir do número informado pelo usuário.

    A função solicita ao usuário um número de conta no formato '12345-6', valida a
    existência dessa conta dentro da lista fornecida e retorna:

      • O dicionário completo da conta, caso ela exista.
      • Uma string contendo a mensagem de erro, caso a conta não seja encontrada
        ou caso não existam contas cadastradas.

    Args:
        lista_contas (list[dict]): Lista contendo todas as contas cadastradas.

    Returns:
        dict | str: O dicionário da conta encontrada ou uma mensagem de erro.
    """

    if not lista_contas:
        return "Não existem contas cadastradas!"

    numero_conta_corrente = str(
        input("Informe o número da conta com o dígito (ex: 12345-6): ")
    )
    conta = next(
        (
            conta
            for conta in lista_contas
            if conta.get("numero_conta_corrente") == numero_conta_corrente
        ),
        None,
    )
    if not conta:
        return "Operação falhou! A conta informada não existe!"

    return conta


def efetuar_deposito(
    lista_contas: list[dict[str, Any]], /
) -> tuple[list[dict[str, Any]], str]:
    """Efetua um depósito em uma conta e atualiza saldo e extrato.

    Solicita ao usuário o número da conta e o valor do depósito, valida a
    entrada e registra a movimentação no extrato da conta.

    Args:
        lista_contas (list[dict]): Lista de contas que será atualizada.

    Returns:
        tuple[list[dict], str]: A lista de contas (com a conta atualizada, se houver)
            e uma mensagem indicando o resultado da operação.
    """

    conta = recuperar_conta(lista_contas=lista_contas)
    if isinstance(conta, str):
        return lista_contas, conta

    try:
        valor = float(input("\nInforme o valor do depósito: "))
    except ValueError:
        return (
            lista_contas,
            "Operação falhou! O valor informado não é numérico.",
        )

    if valor <= 0:
        return (
            lista_contas,
            "Operação falhou! O valor informado é inválido.",
        )
    saldo = conta.get("saldo", 0.0)
    saldo = valor + saldo
    conta["saldo"] = saldo
    extrato: dict[str, list[dict[str, Any]]] = {}
    extrato = conta.get("extrato", extrato)
    conta["extrato"] = atualizar_extrato(
        extrato=extrato, operacao="deposito", valor=valor
    )

    return lista_contas, "Depósito realizado com sucesso!"


def efetuar_saque(
    *,
    limite: float,
    numero_saques: int,
    limite_saques: int,
    lista_contas: list[dict[str, Any]],
) -> tuple[int, list[dict[str, Any]], str]:
    """Efetua um saque em conta, validando limites e atualizando extrato.

    Solicita o número da conta e o valor do saque e valida: saldo suficiente,
    limite por operação e quantidade máxima diária de saques. Em caso de sucesso,
    debita o valor, registra no extrato e incrementa o contador de saques.

    Args:
        limite (float): Valor máximo permitido por operação.
        numero_saques (int): Quantidade de saques já realizados no dia.
        limite_saques (int): Limite diário de saques.
        lista_contas (list[dict]): Lista de contas que será atualizada.

    Returns:
        tuple[int, list[dict], str]: Número de saques atualizado, lista de contas
            (com a conta atualizada) e mensagem de resultado.
    """

    conta = recuperar_conta(lista_contas=lista_contas)
    if isinstance(conta, str):
        return numero_saques, lista_contas, conta

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        return (
            numero_saques,
            lista_contas,
            "Operação falhou! O valor informado não é numérico.",
        )

    saldo = float(conta.get("saldo", 0.0))
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
        extrato: dict[str, list[dict[str, Any]]] = {}
        extrato = conta.get("extrato", extrato)
        conta["extrato"] = atualizar_extrato(
            extrato=extrato, operacao="saque", valor=valor
        )
        conta["saldo"] = saldo
        numero_saques += 1
        msg = "Saque realizado com sucesso!"

    return numero_saques, lista_contas, msg


def gerar_extrato(*, lista_contas: list[dict[str, Any]]) -> str:
    """Gera o extrato textual da conta selecionada.

    Solicita o número da conta, consolida os registros do extrato por tipo de
    operação, ordena por data/hora e monta uma string formatada com as
    movimentações e o saldo atual.

    Args:
        lista_contas (list[dict]): Lista de contas onde o extrato será consultado.

    Returns:
        str: Texto do extrato ou mensagem de erro quando a conta não existe.
    """

    conta = recuperar_conta(lista_contas=lista_contas)
    if isinstance(conta, str):
        return conta

    extrato_completo: list[dict[str, Any]] = []
    extrato = conta.get("extrato")
    msg = " EXTRATO ".center(70, "=")
    if not extrato:
        msg += "\nSem movimentações.\n"
    else:
        for tipo_transacao, lista_transacoes in extrato.items():
            for registro in lista_transacoes:

                registro_completo: dict = registro.copy()
                registro_completo["tipo"] = tipo_transacao
                extrato_completo.append(registro_completo)

        extrato_ordenado = sorted(extrato_completo, key=itemgetter("data"))

        for registro in extrato_ordenado:
            data_registro = f"\n{registro.get('data')}"
            tipo_operacao_registro = f"{registro.get('tipo')}"
            valor_operacao = (
                f"R$ +{registro.get('valor'):.2f}"
                if tipo_operacao_registro == "deposito"
                else f"R$ -{registro.get('valor'):.2f}"
            )
            valor_operacao = f"{valor_operacao:>21}"

            msg += "\n"
            msg += "-" * 70
            msg += data_registro
            msg += "|".center(10)
            msg += tipo_operacao_registro.upper().center(10)
            msg += "|".center(10)
            msg += valor_operacao

    saldo = float(conta.get("saldo", 0.0))
    str_saldo = f"Saldo: R$ {saldo:.2f}"
    msg += "\n\n\n"
    msg += f"{str_saldo:>70}"
    msg += "\n" + "".center(70, "=") + "\n"

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


def cadastrar_usuario(
    lista_usuarios: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], str]:
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


def gerar_conta_unica(lista_contas: list[dict[str, Any]]) -> str:
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
    lista_usuarios: list[dict[str, Any]], lista_contas: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], str]:
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
        {
            "agencia": "0001",
            "numero_conta_corrente": numero_conta,
            "cpf_titular": cpf,
            "extrato": {},
            "saldo": float(0.00),
        }
    )
    return (lista_contas, "Conta cadastrada com sucesso!")


def valor_default(v, default: str = "-") -> str:
    """Normaliza valores textuais para exibição em tabelas.

    Remove espaços de uma string (se aplicável) e retorna um valor padrão quando
    o valor for vazio ou None.

    Args:
        v: Valor a normalizar (geralmente str).
        default (str): Valor a ser usado quando `v` estiver vazio.

    Returns:
        str: Valor normalizado ou o padrão informado.
    """
    if isinstance(v, str):
        v = v.strip()
    return v if v not in (None, "") else default


def iterar_usuarios(
    lista_usuarios: list[dict[str, Any]],
) -> Iterator[tuple[int, dict[str, Any]]]:
    """Itera pelos usuários cadastrados enumerando cada registro.

    Args:
        lista_usuarios (list[dict]): Coleção de usuários cadastrados.

    Yields:
        tuple[int, dict[str, Any]]: Um par com o índice iniciado em 1 e o
            dicionário do usuário correspondente.
    """

    for i, usuario in enumerate(lista_usuarios, start=1):
        yield i, usuario


class IteradorContas:
    """Iterador simples para percorrer a lista de contas cadastradas.

    A classe encapsula o controle de índice para permitir iteração explícita
    sobre a coleção de contas, preservando o estado entre chamadas subsequentes
    de `next`.

    Attributes:
        lista_contas (list[dict[str, Any]]): Contas a serem percorridas.
        indice (int): Posição atual na lista, iniciada em 0.
    """

    def __init__(self, lista_contas: list[dict[str, Any]]) -> None:
        self.lista_contas: list[dict[str, Any]] = lista_contas
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.lista_contas):
            raise StopIteration
        conta = self.lista_contas[self.indice]
        self.indice += 1
        return conta


def listar_usuarios(
    lista_usuarios: list[dict[str, Any]], lista_contas: list[dict[str, Any]]
) -> str:
    """Gera e retorna o texto formatado contendo os usuários cadastrados e suas contas.

    A função percorre todos os usuários cadastrados, exibe seus dados pessoais,
    endereço e, quando existente, lista todas as contas bancárias associadas ao CPF.
    A montagem da tabela é formatada em blocos ASCII para apresentação no console.

    Args:
        lista_usuarios (list[dict]): Lista de usuários cadastrados.
        lista_contas (list[dict]): Lista de contas vinculadas aos usuários.

    Returns:
        str: Texto formatado contendo a listagem completa seguida de uma mensagem
             de conclusão da operação.
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

        for i, usuario in iterar_usuarios(lista_usuarios):

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
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += (
                f"\n|{'*INFORMAÇÕES CADASTRAIS*'.center(len(separador_tabela) - 2)}|"
            )
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n{headers_tabela_informacoes_cadastrais}"
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n|{nome_usuario.center(41)}|{cpf_usuario.center(17)}|{data_nascimento_usuario.center(22)}|"
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n{separador_secao_tabela}"

            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += (
                f"\n|{'*ENDEREÇOS CADASTRADOS*'.center(len(separador_tabela) - 2)}|"
            )
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n{headers_tabela_enderecos_1}"
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n|{logradouro_usuario.center(40)}|{numero_endereco_usuario.center(18)}|{bairro_endereco_usuario.center(22)}|"

            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n{headers_tabela_enderecos_2}"
            lista_usuarios_formatada += f"\n{separador_tabela}"
            lista_usuarios_formatada += f"\n|{cidade_endereco_usuario.center(32)}|{uf_endereco_usuario.center(6)}|{''.center(42, '#')}|"
            lista_usuarios_formatada += f"\n{separador_tabela}"

            if existe_item(lista_contas, "cpf_titular", cpf_usuario):

                lista_usuarios_formatada += f"\n{separador_secao_tabela}"
                lista_usuarios_formatada += f"\n{separador_tabela}"
                lista_usuarios_formatada += (
                    f"\n|{'*DADOS BANCÁRIOS*'.center(len(separador_tabela) - 2)}|"
                )
                lista_usuarios_formatada += f"\n{separador_tabela}"
                lista_usuarios_formatada += f"\n{headers_tabela_contas}"
                lista_usuarios_formatada += f"\n{separador_tabela}"

                for conta in IteradorContas(lista_contas):
                    if conta.get("cpf_titular") == cpf_usuario:

                        agencia_conta_usuario = str(valor_default(conta.get("agencia")))
                        numero_conta_usuario = str(
                            valor_default(conta.get("numero_conta_corrente"))
                        )
                        cpf_titular = str(valor_default(conta.get("cpf_titular")))
                        lista_usuarios_formatada += f"\n|{agencia_conta_usuario.center(27)}|{numero_conta_usuario.center(27)}|{cpf_titular.center(26)}|"
                        lista_usuarios_formatada += f"\n{separador_tabela}"

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
    lista_usuarios: list[dict[str, Any]], lista_contas: list[dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
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

    lista_usuarios: list[dict[str, Any]] = []
    lista_contas: list[dict[str, Any]] = []

    # Descomente a linha abaixo apenas para testes locais:
    carregar_dados_mock(lista_usuarios, lista_contas)

    valor_limite_saque = 500
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
                lista_contas, *_ = exibir_operacao_deposito_console(
                    efetuar_deposito, lista_contas
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "5":
                limpar_tela()
                numero_saques, *_ = exibir_operacao_saque_console(
                    efetuar_saque,
                    limite=valor_limite_saque,
                    numero_saques=numero_saques,
                    limite_saques=QTD_LIMITE_SAQUES,
                    lista_contas=lista_contas,
                )
                input("Pressione qualquer tecla para retornar ao menu principal...")
                carregar_tela_inicial()
            case "6":
                limpar_tela()
                exibir_extrato_console(gerar_extrato, lista_contas=lista_contas)
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
