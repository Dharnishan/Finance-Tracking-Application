import json
transactions = [] #store transaction in the list

#file handling function to load transactions from a json file
def load_transactions():
    
    try:
        with open("transactions.json","r") as file:#read the contents in the json 
            transactions = json.load(file)
    except FileNotFoundError:
        print("File not found, please try again")#display the message that there is no file
        
        

#function to save transaction to a json file
def save_transactions():
    with open("transactions.json","w") as file: #open a file named transactions and write 
        json.dump(transactions,file,indent=2)#convert transactions data into json format
            

#function to add transaction
def add_transaction():    
    while True:
        try:
            amount = float(input("Enter transaction amount: "))
        except ValueError:
            print("Invalid amount please try again!!")
        else:
            description = input("Enter the transaction description: ")
            transaction_type = input("Enter transaction type (Income/Expense): ")
            transaction_type.capitalize()#capitalize the first letter 
            date = input("Enter transaction date (YYYY-MM-DD): ")
            transactions.append([amount,description,transaction_type,date])
            save_transactions() #save the data 
            print("Transaction added successfully!!")
            break


#function to view all transactions
def view_transactions():
    if not transactions:
        print("No transactions found.")
    else:
        index = 1
        for transaction in transactions:
            print(f"{index}. Amount: {transaction[0]}, Description: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")
            index += 1
            

#function to update a transaction 
def update_transaction():
    view_transactions() #call view transaction to display the data 
    try:
        index = int(input("Enter the index of the transaction to update: "))
        index = index-1
        if 0 <= index < len(transactions):
            while True:
                try:
                    amount = float(input("Enter transaction amount: "))
                except ValueError:
                    print("Invalid amount please try again!!")
                else:
                    description = input("Enter the transaction description: ")
                    transaction_type = input("Enter transaction type (Income/Expense): ")
                    transaction_type.capitalize()
                    date = input("Enter transaction date (YYYY-MM-DD): ")
                    transactions[index] = [amount,description,transaction_type,date]
                    save_transactions()
                    print("Transaction updated successfully.")
                    break

    except ValueError:
        print("Invalid input, try again")

#function to delete a transaction
def delete_transaction():
    view_transactions() #call view_transaction to display 
    index = int(input("Enter the index of the transaction to delete"))
    index -= 1
    if 0 <= index < len(transactions):
        del transactions[index]
        save_transactions()
        print("Transaction Deleted successfully..")
    else:
        print("Invalid index.")

#function to display summary of transactions
def summary_of_transaction():
    total_income = sum(transaction[0] for transaction in transactions if transaction[2]=="Income")#sum the income in transactions which transaction_type="Income"
    total_expense = sum(transation[0] for transation in transactions if transation[2]=="Expense")#sum the expense in transactions which transaction_type="Expense"
    balance = total_income - total_expense
    print(f"Total Income: {total_income}")  
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}")   

#function to display menue 
def display_menu():
    print("\n*****Personal Finance Tracker*****") 
    print("1. Add Transaction....")
    print("2. View Transaction....")
    print("3. Update Transaction....")
    print("4. Delete Transaction....")   
    print("5. Summary of Transaction....")
    print("6. Exit....")

#main function to run the program
def main_program():
    load_transactions() #call the load_transaction function
    while True:
        display_menu()
        input_choice = input("Enter your choice: ")
        if input_choice == "1" :
            add_transaction()
        elif input_choice == "2" :
            view_transactions()
        elif input_choice == "3" :
            update_transaction()
        elif input_choice == "4" :
            delete_transaction()
        elif input_choice == "5" :
            summary_of_transaction()
        elif input_choice == "6" :
            print("Exiting the program!!,Thank You..")
            break                     
        else:
            print("Invalid choice. Please Try again..")

if __name__ =="__main__":
    main_program()

