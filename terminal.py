from colorama import init, Fore, Style
from client import Client
from account import Account

# Inicializa o colorama
init(autoreset=True)

class Terminal:
    def __init__(self):
        print(Fore.YELLOW + "\nTerminal criado")

    def validate_input(self, description, type, is_required=True):
        while True:
            try:
                value = type(input(Fore.CYAN + description))

                if is_required and value is None:
                    print(Fore.RED + "Valor requerido")
                else:
                    return value

            except ValueError:
                print(Fore.RED + "Opção inválida")

    def validate_options(self, description, type, options):
        while True:
            try:
                value = type(input(Fore.CYAN + description))

                if value in options:
                    return value
                else:
                    print(Fore.RED + "Opção inválida")
            except ValueError:
                print(Fore.RED + "Opção inválida")

    def validate_document(self, description, type, is_required):
        return self.validate_input(description, type, is_required=is_required)

    def show_create_client(self):
        client = Client()

        print(Fore.GREEN + "\nCadastrar cliente\n")

        name = self.validate_input("Insira o nome do cliente: ", str)
        client.set_name(name)

        document = self.validate_input("Insira o documento do cliente: ", str)
        client.set_document(document)

        return client

    def show_create_account(self):
        account = Account()

        client = self.show_create_client()
        account.set_client(client)

        print(Fore.GREEN + "\nCadastrar conta\n")

        pix_key = self.validate_input("Insira o pix: ", str)
        account.set_pix_key(pix_key)

        number = self.validate_input("Insira o número da conta: ", str)
        account.set_number(number)

        agency = self.validate_input("Insira a agência da conta: ", str)
        account.set_agency(agency)

        balance = self.validate_input("Insira o saldo da conta: ", float, is_required=False)
        account.set_balance(balance)

        limit = self.validate_input("Insira o limite da conta: ", float, is_required=False)
        account.set_limit(limit)

        return account

    def show_main_menu(self):
        print(Fore.BLUE + "\nMenu\n")

        print(Fore.YELLOW + "1 - Buscar cliente")
        print(Fore.YELLOW + "2 - Cadastrar cliente")
        print(Fore.YELLOW + "3 - Excluir cliente")
        print(Fore.YELLOW + "4 - Listar clientes")
        print(Fore.YELLOW + "5 - Sair\n")

        opcao = self.validate_options("Escolha uma opção: ", int, [1, 2, 3, 4, 5])

        return opcao

    def show_client(self, client):
        print(Fore.GREEN + f"\nDADOS DO CLIENTE - {client.get_name().upper()}\n")
        print(Fore.WHITE + "Nome cliente: ", client.get_name())
        print(Fore.WHITE + "Documento cliente: ", client.get_document())

    def show_account(self, account):
        print(Fore.GREEN + "\nDADOS CONTA\n")
        print(Fore.WHITE + "Pix: ", account.get_pix_key())
        print(Fore.WHITE + "Número: ", account.get_number())
        print(Fore.WHITE + "Agência: ", account.get_agency())
        print(Fore.WHITE + "Saldo: ", account.get_balance())
        print(Fore.WHITE + "Limite: ", account.get_limit())
        self.show_client(account.get_client())

    def show_search_client(self):
        print(Fore.BLUE + "\nBUSCAR CLIENTE")

        print(Fore.YELLOW + "\n1 - CPF: ")
        print(Fore.YELLOW + "2 - Agência e Conta: ")
        print(Fore.YELLOW + "3 - Sair\n")

        option = self.validate_options("Escolha uma opção: ", int, [1, 2, 3])

        return option

    def show_client_menu(self):
        print(Fore.BLUE + "\nSEJA BEM VINDO AO MENU CLIENTE\n")
        print(Fore.YELLOW + "1 - Editar dados")
        print(Fore.YELLOW + "2 - Dados da conta")
        print(Fore.YELLOW + "3 - Deposito")
        print(Fore.YELLOW + "4 - Saque")
        print(Fore.YELLOW + "5 - Transferir")
        print(Fore.YELLOW + "6 - Voltar\n")

        option = self.validate_options("Escolha uma opção: ", int, [1, 2, 3, 4, 5, 6])
        return option

    def show_client_pix(self, accounts):
        print(Fore.BLUE + "\nContas disponíveis\n")
        for account in accounts:
            print(Fore.WHITE + f"{account.client.get_name()} - {account.get_pix_key()}")

    def create_standart_clients(self, accounts):
        # Cria um cliente inicial para teste
        client = Client()
        client.set_name("Leonardo")
        client.set_document("71362743119")

        account = Account()
        account.set_client(client)
        account.set_agency(5556)
        account.set_balance(1500)
        account.set_number(5555)
        account.set_limit(5000)
        account.set_pix_key("71362743119")

        accounts.append(account)

        client_2 = Client()
        client_2.set_name("Daniel")
        client_2.set_document("71362743118")

        account_2 = Account()
        account_2.set_client(client_2)
        account_2.set_agency(5559)
        account_2.set_balance(2500)
        account_2.set_number(5559)
        account_2.set_limit(50000)
        account_2.set_pix_key("71362743118")

        accounts.append(account_2)
