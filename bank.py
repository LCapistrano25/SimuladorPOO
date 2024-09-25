from account import Account
from terminal import Terminal
from client import Client

client = Account()

class Bank:
    def __init__(self):
        self.accounts = []
        self.terminal = Terminal()

    # Criar uma conta
    def create_account(self):
        account = self.terminal.show_create_account()
        self.accounts.append(account)

    def _delete_account(self, p_client=None, p_account=None):
        # Remover conta pelo cliente
        if p_client is not None:
            for account in self.accounts:
                if account.get_client().get_document() == p_client.get_document():
                    self.accounts.remove(account)
                    print("Conta removida com sucesso!")
                    return
                
            print("Cliente não encontrado!")

        # Remover conta diretamente
        if p_account is not None:
            for account in self.accounts:
                if account == p_account:
                    self.accounts.remove(p_account)
                    print("Conta removida com sucesso!")
                    return
            print("Conta não encontrada!")
        
    # Excluir cliente
    def delete_account(self):
        client_or_account = self.handle_options_search()
        if isinstance(client_or_account, Client):
            self._delete_account(p_client=client_or_account)
        else:
            self._delete_account(p_account=client_or_account)

    # Listar todas as contas
    def list_accounts(self):
        for account in self.accounts:
            self.terminal.show_account(account)
    
    # Listar todos os clientes
    def list_client_accounts(self):
        if len([account for account in self.accounts]) == 0:
            print("\nNão há clientes cadastrados!")
            return
        
        for account in self.accounts:
            self.terminal.show_client(account.get_client())

    # Buscar cliente por CPF
    def _search_document_client(self, document):
        for account in self.accounts:
            if account.get_client().get_document() == document:
                return account.get_client()
            
        print('\nCliente não encontrado!')
        return None
    
    # Buscar cliente por Agência e Número
    def _search_account_agency_number(self, agency, number):
        for account in self.accounts:
            if account.get_agency() == agency and account.get_number() == number:
                return account
        print("\nConta não encontrada!")
        return None
    
    # Inserir CPF e buscar
    def handle_document_client(self):
        cpf = self.terminal.validate_document("Digite seu CPF: ", str, is_required=True)
        client = self._search_document_client(cpf)

        if client is not None:
            self.terminal.show_client(client)
            return client
        
        return None
    
    # Inserir Agência e Conta
    def handle_account_agency_number(self):
        agency = self.terminal.validate_input("Digite a agência: ", int, is_required=True)
        number = self.terminal.validate_input("Digite o número da conta: ", int, is_required=True)
        account = self._search_account_agency_number(agency, number)

        if account is not None:
            self.terminal.show_account(account)
            return account
        
        return None

    # Opções de consulta de cliente
    def handle_options_search(self):
        option = self.terminal.show_search_client()

        if option == 1:
            client = self.handle_document_client()

            if client is None:
                return 
            
            return client
        
        elif option == 2:
            account = self.handle_account_agency_number()

            if account is None:
                return
            
            return account
        
        elif option == 3:
            return None
        else:
            print("Opção inválida!")
            return None

    # Interface inicial de cadastro de cliente
    def option_client(self):
        self.terminal.create_standart_clients(self.accounts)

        while True:
            option_clients = self.terminal.show_main_menu()

            if option_clients == 1:
                result = self.handle_options_search()

                if result is not None:
                    self.handle_client(result)

            elif option_clients == 2:
                self.create_account()
            elif option_clients == 3:
                self.delete_account()
            elif option_clients == 4:
                self.list_client_accounts()
            elif option_clients == 5:
                break
            else:
                print("Algo deu errado!")
    
    # Interface de dados do cliente
    def handle_client(self, client):
        while True:
            option = self.terminal.show_client_menu()

            if option == 1:
                self.handle_edit(client)
            elif option == 2:
                self.list_client(client)
            elif option == 3:
                self.handle_deposit(client)
            elif option == 4:
                self.handle_with_draw(client)
            elif option == 5:
                self.handle_transfer(client)
            elif option == 6:
                self.view_extract(client)
            elif option == 7:
                break
            else:
                print(option)
                print("Algo deu errado!")

    # Editar cliente
    def handle_edit(self, client_or_account):
        name = self.terminal.validate_input("Nome: ", str, is_required=True)
        document = self.terminal.validate_input("Documento: ", str, is_required=True)

        if isinstance(client_or_account, Client):
            client_or_account.set_name(name)
            client_or_account.set_document(document)
        else:
            client_or_account.client.set_name(name)
            client_or_account.client.set_document(document)

    # Listar dados do cliente
    def list_client(self, client):
        for account in self.accounts:
            if account.client.get_document() == client.get_document():
                self.terminal.show_account(account)
                return
        else:
            print("Dados não encontrados!")

    # Realizar saque
    def handle_with_draw(self, client):
        account_search = None

        for account in self.accounts:
            if account.get_client() == client:
                account_search = account
                break
        
        while True:
            with_draw = abs(self.terminal.validate_input("Qual o valor do saque? ", float, is_required=True))

            balance = account_search.get_balance()

            if balance < 0.01:
                print(f"Você não tem saldo!\n Seu saldo é de R${balance}.")
                continue

            if float(with_draw) > float(balance):
                print("Você não tem saldo suficiente!")
                continue

            remaining_balance = balance - with_draw

            confirm = self.terminal.validate_options(f"Deseja confirmar o saque no valor de R${with_draw}? ",
                                                     str, ["S", "N"])
            
            if "S" in confirm:
                value = account_search.set_balance(remaining_balance)
                account_search.set_extract("Saque")
                print("Operação concluída!")
                return value
            
            else:
                print("Operação cancelada!")
                return 0

    # Realizar deposito
    def handle_deposit(self, client):
        account_search = None

        for account in self.accounts:
            if account.get_client() == client:
                account_search = account
                break
        
        while True:
            deposit = abs(self.terminal.validate_input("Qual o valor do deposito? ", float, is_required=True))

            balance = account_search.get_balance()

            if float(deposit) < float(0):
                print("O valor não pode ser negativo!")
                continue

            deposit_total = balance + deposit

            confirm = self.terminal.validate_options(f"Deseja confirmar o deposito no valor de R${deposit}? ",
                                                     str, ["S", "N"])
            
            if "S" in confirm:
                value = account_search.set_balance(deposit_total)
                account_search.set_extract("Depósito")
                print("Operação concluída!")
                return value
            
            else:
                print("Operação cancelada!")
                return 0

    def get_my_account(self, client):
        for account in self.accounts:
            if account.get_client() == client:
                return account
        return None
    
    def get_account_by_pix(self, pix_key, my_account):
        for account in self.accounts:
            if my_account.get_pix_key() != pix_key:
                if account.get_pix_key() == pix_key:
                    return account
        return None
    
    def _transfer_finish(self, my_account, account_search, value):
        my_account.set_balance(my_account.get_balance() - value)
        account_search.set_balance(account_search.get_balance() + value)
        print("Transferência realizada com sucesso!")
        return
    
    def _transfer(self, sender_account, recipient_account, value):

        if recipient_account is None:
            print("\nCliente não encontrado!")
            return
        
        option = self.terminal.validate_options(f"Deseja realizar uma transferência para o {recipient_account.get_client().get_name()}? Digite (S) ou (N): ", str, ["S", "N"])
        
        if option == "S":
            value = self.terminal.validate_input("Digite o valor a ser transferido: ", float, is_required=True)

            if  sender_account.get_balance() > value:
                option = self.terminal.validate_options(f"Deseja realizar a transferência no valor de R${value}?  Digite (S) ou (N): ", str, ["S", "N"])

                if option == "S":
                    self._transfer_finish(sender_account, recipient_account, value)
                    sender_account.set_extract("transferencia_rementente", destinatary=recipient_account, sender=sender_account, value_out=value)
                    recipient_account.set_extract("transferencia_destinatario", destinatary=recipient_account, sender=sender_account, value_in=value)
                    return True
                else:
                    print("Operação cancelada!")
                    return False
            else:
                print("Você não tem saldo suficiente!")
                return False
        else:
            print("Operação cancelada!")
            return False

    
    # Realizar transferência
    def handle_transfer(self, client):
        self.terminal.show_client_pix(self.accounts)

        recipient = self.terminal.validate_input("\nPara qual cliente deseja mandar? \nDigite a chave pix: ", str, is_required=True)

        sender_account = self.get_my_account(client)
        recipient_account = self.get_account_by_pix(recipient, sender_account)


        trasicion = self._transfer(sender_account, recipient_account, 0)

        if trasicion:
            return
        
    def view_extract(self, client):
        account = self.get_my_account(client)
        print(account.extract)
        self.terminal.show_extract(account)