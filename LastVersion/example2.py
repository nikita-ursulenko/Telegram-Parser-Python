import os
import json
import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AccountManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write("[]")

    def add_account(self, account):
        accounts = self.get_all_accounts()
        accounts.append(account.__dict__)
        self._save_to_file(accounts)

    def delete_account(self, account):
        accounts = self.get_all_accounts()
        accounts = [a for a in accounts if a.username != account.username]
        self._save_to_file(accounts)

    def update_account(self, account):
        accounts = self.get_all_accounts()
        for i, a in enumerate(accounts):
            if a.username == account.username:
                accounts[i] = account.__dict__
                break
        self._save_to_file(accounts)

    def get_all_accounts(self):
        with open(self.filename, 'r') as f:
            accounts = json.load(f)
        return [Account(**a) for a in accounts]

    def _save_to_file(self, accounts):
        with open(self.filename, 'w') as f:
            json.dump(accounts, f, default=lambda o: o.__dict__)

class Application(tk.Tk):
    def __init__(self, account_manager):
        super().__init__()
        self.account_manager = account_manager

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="left", fill="both", expand=True)

        self._update_listbox()

        self.username_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_entry.pack()

        self.password_entry = tk.Entry(self, textvariable=self.password_var)
        self.password_entry.pack()

        self.add_button = tk.Button(self, text="Add", command=self.add_account)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_account)
        self.delete_button.pack()

        self.update_button = tk.Button(self, text="Update", command=self.update_account)
        self.update_button.pack()

    def add_account(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showerror("Error", "Username and password are required!")
            return

        account = Account(username, password)
        self.account_manager.add_account(account)
        self._update_listbox()
        self.username_var.set("")
        self.password_var.set("")

    def delete_account(self):
        account = self._get_selected_account()
        if account:
            self.account_manager.delete_account(account)
            self._update_listbox()

    def update_account(self):
        account = self._get_selected_account()
        if account:
            account.username = self.username_var.get()
            account.password = self.password_var.get()
            self.account_manager.update_account(account)
            self._update_listbox()

    def _update_listbox(self):
        self.listbox.delete(0, tk.END)
        for account in self.account_manager.get_all_accounts():
            self.listbox.insert(tk.END, f"User: {account.username}\nPassword: {account.password}")

    def _get_selected_account(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select an account first!")
            return None

        index = selection[0]
        accounts = self.account_manager.get_all_accounts()
        return accounts[index]

if __name__ == '__main__':
    account_manager = AccountManager("accounts.json")
    app = Application(account_manager)
    app.mainloop()


