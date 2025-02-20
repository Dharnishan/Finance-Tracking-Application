from Cw3gui import main
import json
transactions = {} #store transaction in the dictionary

#file handling function to load transactions from a json file
def load_transactions():
    
    try:
        with open("transactions.json","r") as file:#read the contents in the json 
            transactions = json.load(file)
    except FileNotFoundError:
        print("File not found, please try again")#display the message that there is no file
        return {}
        

#function to save transaction to a json file
def save_transactions():
    with open("transactions.json","w") as file: #open a file named transactions and write 
        json.dump(transactions,file,indent=2)#convert transactions data into json format

#function to read bulk data from file
def read_bulk_transactions_from_file(filename): 
    global transactions
    try:
        with open(filename, "r") as file:  #open a file and read
            lines = file.readlines()
            for line in lines:
                t_data = line.strip().split(",") #split the line by ,
                if len(t_data)==4:
                    amount,description,transaction_type,date = t_data
                    if description not in transactions:
                        transactions[description] = []
                        transactions[description].append({"Amount": float(amount), "Type":transaction_type.capitalize(), "Date": date})
    except FileNotFoundError:
        print("File not found.")
    save_transactions() #save transaction details into json file    
    print("File read successfully!!")        

#function to add transaction
def add_transaction():
    description = ""
    while True:
        description = input("Enter the description: ")
        if description == "" :
            print("Transaction description can't be null pelese enter the description!!")
        else:
            break    
    while True:
        try:
            amount = float(input("Enter transaction amount: "))
        except ValueError:
            print("Invalid amount please try again!!")
        else:
            while True:
                transaction_type = input("Enter transaction type please (Income/Expense): ").capitalize()#capitalize the first letter
                if transaction_type in ['Income','Expense']:
                    break
                else:
                    print("Invalid transaction type please enter(Income/expense)")
            date = input("Enter transaction date (YYYY-MM-DD): ")
            if description in transactions:
                transactions[description].append({"Amount":amount, "Type":transaction_type, "Date":date})
            else:
                transactions[description]=[{"Amount":amount, "Type":transaction_type, "Date":date}]
            save_transactions() #save the data 
            print("Transaction added successfully!!")
            break


#function to view all transactions
def view_transactions():
    if not transactions:
        print("No transactions found.")
    else:
        for description,transaction in transactions.items():
            print(f"{description}:")
            index = 1
            for trans in transaction:
                print(f"{index}.Amount:{trans['Amount']}, Transaction_type:{trans['Type']}, Date:{trans['Date']}")
                index = index + 1
            

#function to update a transaction 
def update_transaction():
    view_transactions()  # call view transaction to display the data
    description = input("Enter the description: ")
    try:
        if description in transactions: # Prompt the user to enter the index of the transaction to update
            index = int(input("Enter the index of the transaction to update: "))
            if 1 <= index <= len(transactions[description]):
                while True:
                    try:
                        amount = float(input("Enter transaction amount: "))
                        transaction_type = input("Enter transaction type (Income/Expense): ").capitalize()
                        if transaction_type not in ['Income', 'Expense']:
                            raise ValueError("Invalid transaction type. Please enter (Income/Expense)")
                        date = input("Enter transaction date (YYYY-MM-DD): ")
                        transactions[description][index-1] = {"Amount": amount, "Type": transaction_type, "Date": date}
                        save_transactions()
                        print("Transaction updated successfully.")
                        break
                    except ValueError as error:
                        print(error)
    except ValueError:
        print("Invalid input, try again")


#function to delete a transaction
def delete_transaction():
    view_transactions() #call view_transaction to display
    description = input("Enter the description: ")
    if description in transactions:
        try:
            index = int(input("Enter the index of the transaction to delete: "))
            if 1 <= index <= len(transactions[description]):  #Check if the index is within the valid range
                del transactions[description][index-1] #Delete the transaction from the transactions dictionary
                save_transactions()
                print("Transaction Deleted successfully..")
            else:
                print("Invald index.")
        except ValueError:
            print("Invalid index.")
    else:
        print("Category not found")



#function to display summary of transactions

def summary_of_transaction():
    total_expense = 0
    total_income = 0
    balance = 0
    for transaction in transactions.values():   #Iterate through each transaction in the transactions dictionary
        for trans in transaction:
            if trans['Type'] == "Expense":
                total_expense += trans['Amount']
            else:
                total_income += trans['Amount']
    balance = total_income - total_expense            
    print(f"Total Expense: {total_expense}")
    print(f"Total Income: {total_income}")
    print(f"Total Balance: {balance}")



       

#function to display menue 
def display_menu():
    print("\n*****Personal Finance Tracker*****") 
    print("1. Add Transaction....")
    print("2. View Transaction....")
    print("3. Update Transaction....")
    print("4. Delete Transaction....")   
    print("5. Summary of Transaction....")
    print("6. Read Bulk Transaction from file....")
    print("7. Display GUI....")
    print("8. Exit....")

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
            filename = input("Enter the file name....") 
            read_bulk_transactions_from_file(filename) 
        elif input_choice == "7":
            main()

        elif input_choice == "8" :
            print("Exiting the program!!,Thank You..")
            break                     
        else:
            print("Invalid choice. Please Try again..")

if __name__ =="__main__":
    main_program()

