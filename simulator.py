from bank import Bank

class Simulator:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        self.bank.option_client()

simulator = Simulator().run()