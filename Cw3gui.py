import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")

    def create_widgets(self):
        # Frame for table and scrollbar
        table_frame = ttk.Frame(self.root)
        table_frame.pack(pady=10)

        # Treeview for displaying transactions
        self.tree = ttk.Treeview(table_frame, columns=("Category", "Amount", "Date", "Type"), show = "headings")
        self.tree.heading("Category", text="Category", command=lambda: self.sort_by_column("Category"))
        self.tree.heading("Amount", text="Amount", command=lambda: self.sort_by_column("Amount"))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_by_column("Date"))
        self.tree.heading("Type", text="Type", command=lambda: self.sort_by_column("Type"))
        self.tree.pack(side="left", fill="both",expand=True)

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set) 

        # Search bar and button
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=5)
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=5)
        search_button = ttk.Button(search_frame, text="Search", command=self.search_transactions)
        search_button.pack(side="left")

        
        

    def load_transactions(self, filename):
        try:
            with open("transactions.json","r") as file:#read the contents in the json 
                transactions = json.load(file)
        except FileNotFoundError:
            print("File not found, please try again")#display the message that there is no file
            transactions = []
        return transactions    

    def display_transactions(self, transactions):
        # Remove existing entries
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add transactions to the treeview
        for category, transactions_list in transactions.items():
            for transaction in transactions_list:
                # Use get() to safely retrieve values with a default value of ""
                description = transaction.get("Category", "")
                amount = transaction.get("Amount", "")
                date = transaction.get("Date", "")
                type_ = transaction.get("Type", "")
                self.tree.insert("", "end", values=(category, amount, date, type_))
        

    def search_transactions(self):
        # Placeholder for search functionality
        query = self.search_entry.get().lower()
        results = {}

        for category, transaction_list in self.transactions.items():
            # Use list comprehension to filter transactions
            category_results = [transaction for transaction in transaction_list
                                if query in str(transaction.get("Amount", "")).lower() or
                                query in str(transaction.get("Date", "")).lower() or
                                query in transaction.get("Type", "").lower() or
                                query in category.lower()]

            if category_results:
                results[category] = category_results

        self.display_transactions(results)

        pass

    def sort_by_column(self, col):
        # Placeholder for sorting functionality
        data =[(self.tree.set(child, col), child) for child in self.tree.get_children()]
        data.sort(reverse=False)
        for index, (val,child) in enumerate(data):
            self.tree.move(child,'',index) 
        self.tree.heading(col, command=lambda: self.sort_by_column(col))
        pass

def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()
