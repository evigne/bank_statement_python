"""
main.py

The program to provide information about the bank transaction
Project started on 3rd June 2018
@author Vigneshwaran Ethirajan

"""
from services.bank_services import enter_details,lookup,deposite,displayAll,withdrawl,netBalance,miniStatement


def main():
    peopleAccount=[]


    running = True
    while running:
        print ("\n\n\t\tBank Works\n\n")
        print ("1)New Entry       2)Look for Account")
        print ("3)Deposit         4)Withdrawl")
        print ("5)Mini-statement  6)Net-Balance")
        print ('7)Display All     8)Eixt')
        choice = int(input("\n\nYour Choice >"))
        if choice==1:
            str(peopleAccount.append(enter_details()))
        elif choice==2:
            lookup(peopleAccount)
        elif choice==3:
            deposite(peopleAccount)
        elif choice==4:
            withdrawl(peopleAccount)

        elif choice==5:
            miniStatement(peopleAccount)

        elif choice==6:
            netBalance()

        elif choice==7:
            displayAll(peopleAccount)

        elif choice==8:
            exit()
        else:
            print ("Wrong Input\nProgram Terminated")
            running=False


if __name__ == "__main__":
    main()
