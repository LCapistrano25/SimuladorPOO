# Sistema Bancário Simples

Este simulador tem como foco principal estudar as estruturas de uma Programação Orientada a Objetos (POO). Trata-se de um projeto de sistema bancário básico que aplica os principais pilares da POO, como encapsulamento, classes e objetos, para gerenciar contas, clientes e transações financeiras.

## 🚀 Funcionalidades

O sistema oferece uma interface de terminal completa para as seguintes operações:

- **Gestão de Clientes:**
  - Cadastro de novos clientes e contas.
  - Edição de dados cadastrais (nome e documento).
  - Exclusão de clientes/contas.
  - Listagem de todos os clientes cadastrados.
- **Operações Bancárias:**
  - **Depósito:** Adição de saldo à conta.
  - **Saque:** Retirada de valores (respeitando o limite e saldo).
  - **Transferência:** Envio de valores entre contas cadastradas.
  - **Extrato:** Visualização detalhada de todas as transações realizadas.
- **Busca e Consulta:**
  - Localização de clientes por CPF.
  - Localização de contas por Agência e Número.
- **Interface Visual:**
  - Feedback visual colorido no terminal utilizando a biblioteca `colorama`.

## 📂 Estrutura do Projeto

O projeto está organizado nos seguintes módulos:

- **[simulator.py](simulator.py):** O ponto de entrada da aplicação. Inicializa o simulador e inicia o loop principal.
- **[bank.py](bank.py):** Contém a classe `Bank`, responsável pela lógica de negócio, gerenciamento da lista de contas e coordenação das operações.
- **[client.py](client.py):** Define a classe `Client`, que armazena informações básicas do usuário (nome e documento).
- **[account.py](account.py):** Define a classe `Account`, que gerencia o saldo, limite, chaves PIX e o histórico de transações (extrato).
- **[terminal.py](terminal.py):** Gerencia toda a interação com o usuário, incluindo menus, exibição de dados e validação de entradas.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Colorama:** Para estilização do terminal.

## 🔧 Como Executar

1. Certifique-se de ter o Python instalado.
2. Instale a dependência `colorama`:
   ```bash
   pip install colorama
   ```
3. Execute o simulador:
   ```bash
   python simulator.py
   ```

---
Projeto desenvolvido para fins de estudo de Programação Orientada a Objetos.
