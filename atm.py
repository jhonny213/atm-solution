class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def show_withdrawals(self):
        for index_withdrawal, withdrawal in enumerate(self.withdrawals_list):
            print("The withdrawal process " + str(index_withdrawal + 1) + ": has been withdrawn " + str(withdrawal) + " USD")
        print("==========================================")
        print("Total withdrawals " + str(sum(self.withdrawals_list)))
        print("==========================================")
        print()

    def give_p_monny(self, request):
        papers = [200, 100, 50, 20, 10, 5, 2, 1]
        while_request = request
        for i in papers:
            j = 0
            while j < while_request // i:
                print("give " + str(i) + " USD")
                j = j + 1
            while_request = while_request - i * (while_request // i)

    def withdraw(self, request):
        lines = "=========================================="
        print("Welcome to " + str(self.bank_name))
        print("Current balance = " + str(self.balance))
        print(lines)
        if self.balance >= request > 0:
            self.give_p_monny(request)
            self.balance -= request
            print(lines)
            self.withdrawals_list.append(request)
            return self.balance
        else:
            if request > self.balance:
                print("Error Request = " + str(request) + ", Can't give you all this money !!")
                print(lines)
                return self.balance
            else:
                print("Invalid Request = " + str(request) + " !!!")
                print(lines)

"""test class ATM"""

balance1 = 500
balance2 = 1000
balance3 = 20000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")
atm3 = ATM(balance3, "Tasleef Bank")

atm1.withdraw(277)
atm1.withdraw(147)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(2000)
atm2.show_withdrawals()

atm3.withdraw(456)
atm3.withdraw(0)
atm3.withdraw(20545)
atm3.withdraw(1000)
atm3.show_withdrawals()