def withdraw(balance, request):
    papers = [200,100,50,20,10,5,2,1]
    if request <= balance and request > 0:
        whileRequest = request
        for i in papers:
            j = 0
            while j < whileRequest // i:
                print ("give ", i)
                j = j + 1
            whileRequest = whileRequest - i * (whileRequest // i)
        print balance - request
        return balance - request
    else:
        if request > balance:
            print 'Error !!! Max request = ', balance
        else:
            print 'Invalid Request ', request , ' !!!'
#test  withdraw(balance,request)
balance = 500
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)


