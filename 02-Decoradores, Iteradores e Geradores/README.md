# 📚 Desafio: Decoradores, Iteradores e Geradores

Este diretório contém a evolução do sistema bancário desenvolvido no curso da
DIO / Luizalabs, agora com foco em **decoradores, iteradores e geradores**.
Além de manter todas as funcionalidades do módulo anterior, a aplicação foi
refatorada para explorar padrões avançados da linguagem e deixar o fluxo mais
organizado e observável. ✨

---

## 🎯 Objetivos Técnicos

- 🧰 Criar um **decorador parametrizado** (`registrar_log`) para registrar início
  e fim das principais operações no console.
- 🧩 Encapsular a interface com o usuário em funções específicas, mantendo a
  camada de regras de negócio isolada.
- 🔁 Exercitar o uso de **iteradores customizados** (`IteradorContas`) e
  **geradores** (`iterar_usuarios`) para percorrer coleções de forma eficiente.
- 🏦 Reaproveitar e evoluir o sistema bancário com validações, cadastros e
  movimentações completas (depósito, saque e extrato).

---

## 🧱 Principais Componentes

### 🕒 Decoradores e Camada de Exibição

- `registrar_log`: decorador parametrizado que imprime timestamps antes e depois
  da execução das operações.
- Funções `exibir_*`: concentram toda a saída do terminal (cadastro, listagem,
  operações bancárias e extrato) e reutilizam o decorador para logar o fluxo.

### 💸 Operações Bancárias

- `efetuar_deposito` e `efetuar_saque`: validam valores, limites diários e
  atualizam saldo/extrato.
- `gerar_extrato`: organiza as movimentações por data, calcula saldo e monta a
  saída formatada exibida no console.

### 🔄 Iteradores e Geradores

- `iterar_usuarios`: gerador que enumera usuários de forma preguiçosa, evitando
  estruturas auxiliares ao formatar a listagem.
- `IteradorContas`: classe que implementa o protocolo de iteração para percorrer
  contas e relacioná-las ao CPF do titular.

### 🛠️ Suporte e Utilidades

- `valor_default`, `validar_cpf`, `validar_data`, `existe_item` e
  `gerar_conta_unica`: funções auxiliares que centralizam validações e
  normalizações.
- `carregar_dados_mock`: permite pré-carregar usuários/contas para facilitar
  testes locais.

---

## ▶️ Execução

```bash
cd 02-Decoradores, Iteradores e Geradores
python desafio.py