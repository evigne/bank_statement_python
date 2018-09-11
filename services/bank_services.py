
from models.bank import Bank
import random

def enter_details():
    name = input("Enter The Account Holder's Name:")
    phone = input("Enter The Phone Number:")
    acc_no = str(random.randrange(1, 99999999999, 2))
    print ("Your Account number is ",acc_no)
    global deposit
    global withdrawl
    deposit = int(input("Enter Amount for initial deposit:"))
    return Bank(name,acc_no,deposit,phone)

def deposite(people):
    global deposit
    acc_no=input("Enter the account number to deposit:")
    for person in people:
        if acc_no in person.getAcc_no():
            dep = int(input("Enter New Deposit:"))
            # deposit = deposit + dep
            #netbalance = deposit-withdrawl
            person.setDeposit(dep)
            break
        #break
    else:
        print ("No Account found")

def withdrawl(people):
    global withdrawl
    acc_no=input("Enter the account number to withdraw:")
    for person in people:
        if acc_no in person.getAcc_no():
            withdrawl=int(input("How much you want to withdraw:"))
            person.setWithdrawl(withdrawl)
        #break
    else:
         print ("No Account Found")

def miniStatement(people):
    acc_no=input("Enter the account number for ministatement:")
    for person in people:
        if acc_no in person.getAcc_no():
            print ('Name:{}\nAcc.No:{}'.format(person.getName(),acc_no))
            for i in person.getStatement():
                print (i)
            print("Net Balance:", person.getNetbalance())
        #break
    else:
         print ('Account Not Found')



def netBalance():
    pass
def lookup(people):
    pass
def displayAll(people):
    print("Showing all contacts:")
    for person in people:
        print(person)