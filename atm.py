class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []
        self.papers = {200 : 10, 100 : 20, 50 : 30, 20 :  40, 10 : 50, 5 : 60, 2 : 70, 1 : 0}

    def show_withdrawals(self):
        for index_withdrawal, withdrawal in enumerate(self.withdrawals_list):
            print("The withdrawal process " + str(index_withdrawal + 1) + ": has been withdrawn " + str(withdrawal) + " USD")
        print("Sold papers = " + str(self.papers))
        print("==========================================")
        print("Total withdrawals " + str(sum(self.withdrawals_list)))
        print("==========================================")
        print()
    """def charge(self):
        for ind,val in self.papers.items():"""

    def give_p_monny(self, request):
        while_request = request
        give = []
        for i in self.papers.keys():
            j = 0
            if self.papers[i] > 0:
                while j < while_request // int(i):
                    give.append(i)
                    j = j + 1
                while_request = while_request - int(i) * (while_request // int(i))
        return {"sold" : while_request, "give" : give}

    def papers_process(self,request):
        sold = self.give_p_monny(request)
        if sold["sold"] != 0:
            papers = (200,100,50,20,10,5,2,1)
            manque_papers = []
            double_paper = 0
            for i in papers:
                j= 0
                while j < sold["sold"] // i:
                    if double_paper != i:
                        manque_papers.append(i)
                    double_paper = i
                    j += 1
            return manque_papers
        else:
            for p in sold['give']:
                for i in self.papers.keys():
                    if i == p:
                        self.papers[i] = self.papers[i] - 1
            return 0

    def withdraw(self, request):
        lines = "=========================================="
        print("Welcome to " + str(self.bank_name))
        print("Current balance = " + str(self.balance))
        print(lines)
        if self.balance >= request > 0:
            sold = self.papers_process(request)
            if sold == 0:
                result = self.give_p_monny(request)
                for val in result['give']:
                    print ("give " + str(val)  + " USD")
                self.balance -= request
                print(lines)
                self.withdrawals_list.append(request)
            else:
                for paper in sold:
                    print(" Papers " + str(paper) + " USD not find, Change request ")
                print(lines)
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

atm1.withdraw(215)
atm1.withdraw(223)
atm1.show_withdrawals()

atm2.withdraw(100)
atm2.withdraw(2000)
atm2.show_withdrawals()

atm3.withdraw(456)
atm3.withdraw(0)
atm3.withdraw(20545)
atm3.withdraw(1000)
atm3.show_withdrawals()