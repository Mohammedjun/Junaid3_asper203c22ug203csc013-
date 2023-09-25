User_Id="##@@"
Password=123
print("Welcome To MK_BANK")
print("Enter Your Credentials To Login:")
Enter_Id=input("Enter User_Id:")
Enter_Pass=int(input("Enter User Password:"))

if(User_Id==Enter_Id and Password==Enter_Pass):

    class Bank_Account():
        Bank_Name="TN_BANK"
        Branch="TamilNadu"
        def _customer(self,acc_no,name,balance):
            self.acc_no=acc_no
            print("Customer's Account Number:",self.acc_no)
            self.name=name
            print("Account_Holder's Name:",self.name)
            self.balance=balance
            print("Clear Balance:",balance)

    
        def _transaction(self,deposit,withdraw,balance):              
            self.deposit=deposit
            self.withdraw=withdraw
            Enter_dep=float(input("Enter Amount in INR To Add:"))
            if(Enter_dep>=1):
                self.deposit=deposit+Enter_dep
                print(self.deposit)
                print("Now your avail Balance:",self.deposit)
                self.deposit=balance    
            Enter_with=float(input("Enter Amount in INR To Withdraw:"))
            if(Enter_with>=0):
                self.withdraw=balance-Enter_with
                print(self.withdraw)
                print("Your Available Balance is:",self.withdraw)
            else:
                return Bank_Account._customer(321,"Tamil",1000)

            
else:
    print("Invalid User_id and Password")

    print("gonna kick you")
    print("I gonna make you work...hahaha..")
    print("To Run The Code...")
    print("(bank._customer()")
    print("bank._transaction())")
    print("call the above function")
    exit     
bank=Bank_Account()
bank=Bank_Account()
bank._customer(321,"Tamil",1000)
print("""If you want to deposit then enter the amount,else let you be remind as 0""")
print("""If you want to withdraw then enter the amount,else let you be remind as 0""")
bank._transaction(1000,0,1000)              
