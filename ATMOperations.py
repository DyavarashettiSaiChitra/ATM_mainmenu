from ATMexcep import DepositError,WithDrawError,InsufficientError
bal=500 #global variable

def deposit():
    damt=float(input("Enter The deposit Amount:"))
    if(damt<0):
        raise DepositError
    else:
        global bal
        bal=damt+bal
        print("Your Account Number XXXXXXXXX159 Credited with INR:{}".format(damt))
        print("Your Total Balance in your Account Number XXXXXXXXX159 is INR:{}".format(bal))

def withdraw():
    global bal
    wdamt=float(input("Enter The withdraw Amount:"))
    if(wdamt<=0):
        raise WithDrawError
    elif((wdamt+500)>bal):
        raise InsufficientError
    else:
        bal=bal-wdamt
        print("Your Account Number XXXXXXXXX159 Debited with INR:{}".format(wdamt))
        print("Your Total Balance in your Account Number XXXXXXXXX159 is INR:{}".format(bal))
def balenq():
    print("Your Total Balance in your Account Number XXXXXXXXX159 is INR:{}".format(bal))
