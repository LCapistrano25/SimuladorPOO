import datetime
from client import Client

class Account:
    def __init__(self):
        self.client = Client()
        self.pixKey=""
        self.number=""
        self.agency=""
        self.balance=0
        self.limit=0
        self.extract=[]

    def set_client(self, client):
        self.client=client
        
    def get_client(self):
        return self.client
    
    def set_pix_key(self, pix_key):
        self.pixKey=pix_key

    def get_pix_key(self):
        return self.pixKey
    
    def set_number(self, number):
        self.number=number

    def get_number(self):
        return self.number
    
    def set_agency(self, agency):
        self.agency=agency

    def get_agency(self):
        return self.agency
    
    def set_balance(self, balance):
        self.balance=balance

    def get_balance(self):
        return self.balance
    
    def set_limit(self, limit):
        self.limit=limit
    
    def get_limit(self):
        return self.limit
    
    def set_extract(self, type, destinatary=None, sender=None, value_in=None, value_out=None):
        extract = {}
        extract_destinatary = {}

        # Dados do extrato do remetente
        extract['date'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extract['client'] = self.client.get_name()
        extract['agency'] = self.get_agency()
        extract['number'] = self.get_number()
        extract['value'] = self.get_balance()
        extract['value_in'] = value_in if value_in is not None else 0
        extract['value_out'] = -value_out if value_out is not None else 0
        extract['type'] = type

        if type == "transferencia_remetente":
            # Dados adicionais do destinatário no extrato do remetente
            extract['destinatary_name'] = destinatary.get_client().get_name()
            extract['destinatary_agency'] = destinatary.get_agency()
            extract['destinatary_number'] = destinatary.get_number()

            # Criando o extrato para o destinatário
            extract_destinatary['date'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extract_destinatary['client'] = destinatary.get_client().get_name()
            extract_destinatary['agency'] = destinatary.get_agency()
            extract_destinatary['number'] = destinatary.get_number()
            extract_destinatary['value'] = destinatary.get_balance()
            extract_destinatary['value_in'] = value_out if value_out is not None else 0  # Valor que entrou na conta do destinatário
            extract_destinatary['value_out'] = 0  # Transferências recebidas não têm valor de saída
            extract_destinatary['type'] = "transferencia_destinatario"
            extract_destinatary['sender_name'] = self.client.get_name()  # Dados do remetente
            extract_destinatary['sender_agency'] = self.get_agency()
            extract_destinatary['sender_number'] = self.get_number()

            # Adicionando o extrato à conta do destinatário
            destinatary.extract.append(extract_destinatary)

        # Adicionando o extrato à conta do remetente
        self.extract.append(extract)
