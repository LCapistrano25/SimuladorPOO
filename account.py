from client import Client

class Account:
    def __init__(self):
        self.client = Client()
        self.pixKey=""
        self.number=""
        self.agency=""
        self.balance=0
        self.limit=0

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