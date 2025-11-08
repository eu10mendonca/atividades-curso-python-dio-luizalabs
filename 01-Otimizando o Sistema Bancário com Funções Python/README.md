# Desafio: Otimizando o Sistema Bancário com Funções Python

Este projeto é a solução do desafio **"Otimizando o Sistema Bancário com Funções Python"**,
proposto na trilha de Python da DIO / Luizalabs.

A partir de uma versão inicial totalmente baseada em um único laço `while` e variáveis
globais, o objetivo foi **refatorar** o sistema para uma arquitetura mais organizada,
modular e escalável.

---

## Objetivos Atendidos

- Separar operações em funções específicas:
  - `efetuar_deposito`
  - `efetuar_saque`
  - `exibir_extrato`
- Utilizar:
  - parâmetros somente posicionais (`/`) no depósito;
  - parâmetros somente nomeados (`*`) no saque;
  - combinação posicional + nomeado no extrato.
- Implementar:
  - cadastro de usuário;
  - cadastro de conta corrente;
  - vinculação entre usuário e conta via CPF;
  - prevenção de CPFs duplicados;
  - validações de entrada.

---

## Funcionalidades Implementadas

### ✅ Depósito

- Função: `efetuar_deposito(saldo, extrato, /)`
- Lê o valor do depósito via entrada do usuário.
- Valida:
  - número válido;
  - valor maior que zero.
- Atualiza:
  - saldo;
  - extrato (com alinhamento à direita dos valores).
- Retorna: novo saldo, extrato atualizado e mensagem da operação.

### ✅ Saque

- Função:
  `efetuar_saque(*, saldo, extrato, limite, numero_saques, limite_saques)`
- Regras:
  - valor numérico válido;
  - saldo suficiente;
  - valor até o limite por saque;
  - respeita limite diário de saques.
- Atualiza saldo, extrato e contador de saques.
- Retorna: novo saldo, extrato atualizado, número de saques e mensagem.

### ✅ Extrato

- Função: `exibir_extrato(saldo, /, *, extrato)`
- Monta e retorna uma string formatada contendo:
  - cabeçalho,
  - movimentações (depósitos/saques),
  - saldo final alinhado à direita.
- Impressão é feita pelo `main`, mantendo separação entre lógica e interface.

### ✅ Cadastro de Usuário

- Função: `cadastrar_usuario(lista_usuarios)`
- Coleta:
  - CPF,
  - nome,
  - data de nascimento (`dd-mm-yyyy`),
  - endereço (logradouro, número, bairro, cidade, UF).
- Valida:
  - CPF com 11 dígitos numéricos (`validar_cpf`);
  - data válida (`validar_data`);
  - CPF não duplicado (`existe_item`).
- Armazena usuários em `lista_usuarios` como dicionários.

### ✅ Cadastro de Conta Corrente

- Função: `cadastrar_conta(lista_usuarios, lista_contas)`
- Regras:
  - só permite conta para CPF já cadastrado;
  - agência fixa `"0001"`;
  - número da conta gerado por `gerar_conta_unica`, garantindo unicidade;
  - vínculo pelo campo `cpf_titular`.
- Armazena contas em `lista_contas`.

### ✅ Listagem de Usuários

- Função: `listar_usuarios(lista_usuarios, lista_contas)`
- Gera uma saída tabular formatada com:
  - dados cadastrais;
  - endereços;
  - contas associadas ao CPF, quando existirem.
- Retorna uma string pronta para exibição.

---

## Arquivo Principal

Todo o sistema está concentrado em:

```text
01-Otimizando o Sistema Bancário com Funções Python/
└── desafio.py