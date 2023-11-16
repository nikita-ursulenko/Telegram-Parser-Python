import tkinter as tk
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import tkinter.messagebox
from tkinter import *
import pickle



api_id = 25432944
api_hash = 'ebed7df8f08f651202a7e31b5546abb0'


class Account:
    def __init__(self, name, api_id, api_hash):
        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash

                # Create an instance of the Account class
        account = Account("MyAccount", 25432944, "ebed7df8f08f651202a7e31b5546abb0")

        # Save the account object to a file
        with open("account.pickle", "wb") as file:
            pickle.dump(account, file)

        # Load the account object from the file
        with open("account.pickle", "rb") as file:
            loaded_account = pickle.load(file)

        # Print the data of the loaded account object
        print(loaded_account.name)
        print(loaded_account.api_id)
        print(loaded_account.api_hash)


class Appication:
    def __init__(self, master):
        self.master = master
        self.master.title("Telegram 📨")
        self.accounts = []


        self.button_parser= tk.Button(self.master, text="Parser 🔍", command=self.parser, width=15)
        self.button_parser.pack(padx=10, pady=5)

        self.button_acount= tk.Button(self.master, text="Account 👤", command=self.acount_manage, width=15)
        self.button_acount.pack(padx=10, pady=5)
        
        self.button_acount= tk.Button(self.master, text="Exit 🚪", command=lambda: self.master.destroy(), width=10, fg='red')
        self.button_acount.pack(pady=10)
    
    def parser(self):
        add_account_window = tk.Toplevel(self.master)
        add_account_window.title("Parser")
        x = (add_account_window.winfo_screenwidth() - add_account_window.winfo_reqwidth()) / 2
        y = (add_account_window.winfo_screenheight() - add_account_window.winfo_reqheight()) / 2
        add_account_window.wm_geometry("+%d+%d" % (x, y))
        add_account_window.grab_set()

        label_parser = tk.Label(add_account_window, text="Введите группу:")
        label_parser.pack()

        input_field = tk.Entry(add_account_window)
        input_field.insert(0, "@example")
        input_field.pack()
        
        def clear_input(event):
            if input_field.get() == "@example":
                input_field.delete(0, tk.END)

        input_field.bind("<Button-1>", clear_input)


        async def extract_group_members(client, group_username):
            result = await client(GetParticipantsRequest(
                channel=group_username,
                filter=ChannelParticipantsSearch(''),
                offset=0,
                limit=100,
                hash=0
            ))
            users = []
            for user in result.users:
                if user.username:
                    users.append(user.username)
            with open('ParserTelegram/BaseHealth/{}.txt'.format(group_username), 'w') as file:
                file.write('@')
                file.write('\n@'.join(users))


        async def run_telegram_client(group_username):
            async with TelegramClient('+6283869223408', api_id, api_hash) as client:
                await extract_group_members(client, group_username)


        def start_parsing():
            input_field.focus_displayof()

            if (input_field.get() == "@example"):
                tkinter.messagebox.showwarning(title='Ошибка ввода!❌', message='Введите юзер группы которую хотите спарсить! For example: @example_group')
            
            else:
                group_username = input_field.get()
                input_field.delete(0, tk.END)
                asyncio.run(run_telegram_client(group_username))
                tkinter.messagebox.showinfo(title='Успешно!✅', message='Ваши данные были сохранены в app/ParserTelegram/BaseHealth/'+group_username+'.txt')


        button = tk.Button(add_account_window, text="Спарсить🔍",width=20, command=start_parsing)
        button.pack()

        button_pars = tk.Button(add_account_window, text="🔙",width=10, command=lambda: add_account_window.destroy(), fg='red')
        button_pars.pack(pady=20)




    def acount_manage(self):
        account_manage_window = tk.Tk()
        account_manage_window.title("Account 👥")
        x = (account_manage_window.winfo_screenwidth() - account_manage_window.winfo_reqwidth()) / 2
        y = (account_manage_window.winfo_screenheight() - account_manage_window.winfo_reqheight()) / 2
        account_manage_window.wm_geometry("+%d+%d" % (x, y))
        account_manage_window.grab_set()
        
        label_acount = tk.Label(account_manage_window, text='Имя аккаунта')
        label_acount.pack()

        button_manage_switch = tk.Button(account_manage_window, text="Switch Account🔄",width=20, command=self.userbots_menu)
        button_manage_switch.pack(padx=10, pady=5)
        
        button_manage_close = tk.Button(account_manage_window, text="🔙", command=lambda: account_manage_window.destroy(),width=10, fg='red')
        button_manage_close.pack( pady=20)
        
        

    def userbots_menu(self):
        userbots_menu_window = tk.Tk()
        userbots_menu_window.title("Switch manage")
        x = (userbots_menu_window.winfo_screenwidth() - userbots_menu_window.winfo_reqwidth()) / 2
        y = (userbots_menu_window.winfo_screenheight() - userbots_menu_window.winfo_reqheight()) / 2
        userbots_menu_window.wm_geometry("+%d+%d" % (x, y))

        def on_select(event):
            cur_list = userbots_label2.curselection()
            if cur_list:
                selected_item.set(userbots_label2.get(cur_list))

        def add_user():
            add_user_window = tk.Tk()
            add_user_window.title("Enter user")
            x = (add_user_window.winfo_screenwidth() - add_user_window.winfo_reqwidth()) / 2
            y = (add_user_window.winfo_screenheight() - add_user_window.winfo_reqheight()) / 2
            add_user_window.wm_geometry("+%d+%d" % (x, y))

            label_name = tk.Label(add_user_window, text='Name')
            label_name.pack()
            entry_name = tk.Entry(add_user_window)
            entry_name.pack()

            label_id = tk.Label(add_user_window, text='ID')
            label_id.pack()
            entry_id = tk.Entry(add_user_window)
            entry_id.pack()

            label_hash = tk.Label(add_user_window, text='Hash')
            label_hash.pack()
            entry_hash = tk.Entry(add_user_window)
            entry_hash.pack()

            def on_confirm():
                name = entry_name.get()
                id = entry_id.get()
                hash = entry_hash.get()

                with open("user_data.txt", "a") as file:
                    file.write(f"Name: {name}\nID: {id}\nHash: {hash}\n\n")
                    add_user_window.destroy()


            button_confirm = tk.Button(add_user_window, text="Confirm", command=on_confirm)
            button_confirm.pack()
            
        def on_confirm():
            item = selected_item.get()
            
            print("Selected item:")
            print("Name:", item["name"])
            print("ID:", item["id"])
            print("Hash:", item["hash"])

        selected_item = tk.StringVar()

        userbots_label = tk.Label(userbots_menu_window, text='Your user')
        userbots_label.pack()
        userbots_label2 = Listbox(userbots_menu_window)
        userbots_label2.pack()
        items = [{"name": "Item 1", "id": 1, "hash": "abc123"},
                 {"name": "Item 2", "id": 2, "hash": "def456"},
                 {"name": "Item 3", "id": 3, "hash": "ghi789"},
                 {"name": "Item 4", "id": 4, "hash": "jkl012"},
                 {"name": "Item 5", "id": 5, "hash": "mno345"}]
        for item in items:
            userbots_label2.insert(tk.END, item["name"])

        userbots_label2.bind("<<ListboxSelect>>", on_select)
        userbots_change = tk.Button(userbots_menu_window, text='Delete', command=on_confirm)
        userbots_change.pack()

        userbots_change = tk.Button(userbots_menu_window, text='Add user', command=add_user)
        userbots_change.pack()


        

        



       




root=tk.Tk()
Appication(root)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.mainloop()