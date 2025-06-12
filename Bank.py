class Bankaccount:
    def __init__(self,holder_name,acc_no,balance):
        self.details={"holder_name":holder_name,"acc_no":acc_no,"balance":balance}
    #holder details
    def holder(self):
        self.acc=int(input("Enter the account number:"))
        if self.acc==123:
            return Bankaccount("Nithesh",self.acc,1000)
        elif self.acc==1234:
            return Bankaccount("Raju",self.acc,1200)
        elif self==12345:
            return Bankaccount("Hari",self.acc,1300)
        else:
            print("Invalid Account Number")
            return None
    #Showing  holder details
    def display(self):
        for n,m,b in [self.details.values()]:
            print(f"Name:{n}\nHolder Name:{m}\nBalance:{b}")
    #Depositing money
    def deposit(self):
        self.dept=int(input("Enter the deposit amount: "))
        self.details["balance"]+=self.dept
        print("Deposit amount:",self.dept)
        print("Availble balance:",self.details["balance"])
    #Based on deposit generating intrest
    def intrest(self):
        self.intrest1=self.details["balance"]*5/100
        print("Intrest:",self.intrest1)
        self.details["balance"]+=self.intrest1
        print("Availble balance:",self.details["balance"])

Bank=Bankaccount("",0,0)
Bank=Bank.holder()

Bank.display()
user_input=input("Do you want to deposit money yes/no:").lower()
while user_input=="yes":
  
  Bank.deposit()
  Bank.intrest()
  break
  

