money = 2000
request = 1918
papers = [200,100,50,20,10,5,2,1]
if request <= money and request > 0:
    result = 0
    for i in papers:
        j = 0
        while j < request // i: 
            print ("give ", i)
            result += i
            j = j + 1
        request = request - i * (request // i)
# verification
    print(' Total = ',result)

else:
    if request > money:
        print('Error !!! Max request = ', money)
    else:
        print('Invalid Request ', request , ' !!!')