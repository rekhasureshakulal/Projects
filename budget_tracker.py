try:
    class Transactions:
   
        def __init__(self,transaction_type,amount,income_source =None,expenses = None):
            self.type = transaction_type
            self.amount = amount
            self.source = income_source
            self.expenses = expenses

    class incomeExpenseTracker():
        def __init__(self):
            self.transactions_list=[]

        def add_income(self,source,amount):
            transaction =Transactions("Income",amount,source) 
            self.transactions_list.append(transaction)
            print(f"\n{source} added Successfully!")
            

        def add_expences(self,expense,amount) :
            transaction  = Transactions("Expenses",-amount ,expenses=expense) 
            self.transactions_list.append(transaction)
            print(f"\n{expense} added Successfully!")
            

        def view_tansactions(self):
            if not self.transactions_list:
                print("There is no Transaction to display : ") 
            else:
                print("Transactions are :")
                for transaction in self.transactions_list:
                    if transaction.type ==  "Income":
                        print(f"Income(Credit): {transaction.source} :  amount : Rs. {transaction.amount}")
                    elif transaction.type == "Expenses":
                        print (f"Expenses on (Debit) :{transaction.expenses}  :  Amount :  Rs. {transaction.amount}")
        def view_balance(self):
            balance = sum(transaction.amount for transaction in self.transactions_list )
            print("Current balance is : Rs",balance)


        def run(self):
            print("Welcome To Income Expense Tracker ")
            while True:
                print("****************************************************************")
                
                # print("\n")
                print("MENU IS : ")
                print('Add Income :             1')
                print('Add Expenses :           2')
                print('View Transactions :      3')
                print('View Balance :           4')
                print('Exit :                   5')
                # print("\n")
                print("******************************************************************")

                choice = int(input("Enter your option :"))
                if choice==1:
                    source = input("Enter the Source of Income ,Ex :Salary,Farming Business etc : ")
                    if(source.isdigit( )):
                        print ("Please enter a valid name of source of  income.")
                    else:
                        amount = float(input("Enter the Amount : "))                
                        self.add_income(source,amount)
                
                elif choice==2:
                    expense = (input ("Enter The Category Of Your Expence (Ex  : Food,Transportation etc.) : "))
                    if(expense.isdigit()):
                        print( "Please Enter Valid Name Of Expenses .")
                    else:
                        amount = float(input("Enter The Amount : "))                
                        self.add_expences(expense,amount)            
                                                
                elif choice==3:                   
                    self.view_tansactions()
                elif choice==4:              
                    self.view_balance()               
                else:
                    print("Exiting Program..")
                    exit()
                    break
except Exception as e:
    print("An error occurred:",e)   
if __name__ == '__main__':
    app = incomeExpenseTracker()
    app.run()





                