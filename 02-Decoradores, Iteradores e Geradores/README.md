# 📚 Desafio: Decoradores, Iteradores e Geradores

Este diretório contém a evolução do sistema bancário desenvolvido no curso da
DIO / Luizalabs, agora com foco em **decoradores**, **iteradores** e **geradores**.
O objetivo desta etapa é ampliar a organização interna do código, reforçar boas
práticas de arquitetura e explorar recursos avançados da linguagem Python. ✨

---

## 🎯 Objetivos Técnicos

- 🧰 Criar um **decorador parametrizado** (`registrar_log`) para registrar início
  e fim das operações no console.
- 🧩 Encapsular a interface com o usuário em funções especializadas,
  separando exibição de regras de negócio.
- 🔁 Implementar **iteradores customizados** (`IteradorContas`) e
  **geradores** (`iterar_usuarios`) para percorrer coleções de maneira eficiente.
- 🏦 Evoluir o sistema bancário: cadastro de usuários, criação de contas,
  depósito, saque e extrato — agora com logs e melhor organização.

---

## 🧱 Principais Componentes

### 🕒 Decoradores e Camada de Exibição

- **`registrar_log`**: decorador parametrizado que imprime timestamps antes e
  depois da execução das funções anotadas.
- Funções `exibir_*`: responsáveis por apresentar as informações ao usuário
  (cadastro, listagem, movimentações e extrato).

---

### 💸 Operações Bancárias

- **`efetuar_deposito` e `efetuar_saque`**: funções que validam valores,
  verificam limites, atualizam saldo e registram transações.
- **`gerar_extrato`**: consolida as operações, organiza por tipo/data e exibe o valor final.

---

### 🔄 Iteradores e Geradores

- **`iterar_usuarios`**: gerador que percorre a lista de usuários, entregando
  pares (índice, usuário) sem criar listas auxiliares.
- **`IteradorContas`**: classe que implementa `__iter__` e `__next__`,
  permitindo iterar diretamente sobre contas vinculadas a um CPF.

---

### 🛠️ Funções Auxiliares

- `valor_default`, `validar_cpf`, `validar_data`, `existe_item`,
  `gerar_conta_unica`: centralizam validações e utilidades do sistema.
- `carregar_dados_mock`: popula dados de teste para facilitar experimentação.

---

## ▶️ Como Executar

No terminal, navegue até o diretório da atividade:

```bash
cd "02-Decoradores, Iteradores e Geradores"
python desafio.py
```

---

## 💬 Notas Finais

Este desafio é parte da trilha de Python e Back-End e demonstra como aplicar
conceitos fundamentais da linguagem para construir aplicações mais robustas,
modulares e fáceis de manter. Logs, geradores e iteradores adicionam clareza,
desempenho e profissionalismo ao projeto. 🚀