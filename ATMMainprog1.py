import sys
from ATMMainMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMexcep import DepositError,WithDrawError,InsufficientError
while(True):
    menu()
    try:
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\tDon't Enter alnums,symbols and str Invalid deposit.Try Again")
                except DepositError:
                    print("Don't Try to Enter Negative or Zero Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDon't Enter alnums,symbols and str Invalid deposit.Try Again")
                except WithDrawError:
                    print("Don't Try to Withdraw Negative and Zero amounts.Try Again")
                except InsufficientError:
                    print("Your Account Number xxxxxxxxxxx159 Don't have sufficient Funds.Try Again")
            case 3:
                try:
                    balenq()
                except:pass
            case 4:
                print("Thanks for visiting ")
                sys.exit
            case _:
                print("Your selection of operation is incorrect.Please Try Again")
    except ValueError:
        print("\tDon't Enter alnums,symbols and str as choice")