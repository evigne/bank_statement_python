from _datetime import datetime

class Bank(object):
    #constructor
    def __init__(self,name,acc_no,deposit,phone):
        self.name=name
        self.acc_no=acc_no
        self.deposit=deposit
        self.phone=phone
        self.withdrawl=0
        self.netbalance=self.deposit - self.withdrawl
        self.statements=[]

    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getAcc_no(self):
        return self.acc_no
    def getDeposit(self):
        return self.deposit
    def getWithdrawl(self):
        return self.withdrawl
    def getStatement(self):
        return self.statements
    def getNetbalance(self):
        return self.netbalance


    def setDeposit(self,newDeposit):
        self.deposit=self.deposit+newDeposit
        dep_str = '{} => {} Deposit'.format(datetime.now(), newDeposit)
        self.statements.append(dep_str)
        self.netbalance=self.deposit - self.withdrawl


    def setWithdrawl(self,newWithdrawl):
        self.withdrawl=self.withdrawl+newWithdrawl
        wit_str = '{} => {} Withdraw'.format(datetime.now(),newWithdrawl)
        self.statements.append(wit_str)
        self.netbalance=self.deposit-self.withdrawl


    def __str__(self):
        return "Name=" + self.name + \
               "\nPhone=" + str(self.phone) + \
               "\nAccount No.=" + str(self.acc_no) + \
               "\nTotal Deposit="+str(self.deposit)+\
               "\nTotal Withdrawl="+str(self.withdrawl)+\
               "\nNet Balance="+str(self.netbalance)+\
               "\nStatement="+str(self.statements)+"]"
