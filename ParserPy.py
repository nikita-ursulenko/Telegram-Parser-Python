import tkinter as tk
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import tkinter.messagebox

api_id = 20039660
api_hash = 'af1e7864e33cb41a2cfbed1f9b990326'


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

def clear_input(event):
    if input_field.get() == "@example":
        input_field.delete(0, tk.END)
    

async def run_telegram_client(group_username):
    async with TelegramClient('+6283869223408', api_id, api_hash) as client:
        await extract_group_members(client, group_username)

def start_parsing():
    input_field.focus_displayof()

    if (input_field.get() == "@example"):
        tkinter.messagebox.showwarning(title='Ошибка ввода!', message='Введите юзер группы которую хотите спарсить! For example: @example_group')
    
    else:
        group_username = input_field.get()
        input_field.delete(0, tk.END)
        asyncio.run(run_telegram_client(group_username))
        tkinter.messagebox.showinfo(title='Успешно!', message='Ваши данные были сохранены в /Users/banasea/Documents/TON/app/ParserTelegram/BaseHealth/'+group_username+'.txt')

root = tk.Tk()
root.title("Parser Telegram")

label = tk.Label(root, text="Введите группу:")
label.pack()

input_field = tk.Entry(root)
input_field.insert(0, "@example")
input_field.pack()
input_field.bind("<Button-1>", clear_input)
whyWork = input_field.focus_set()

button = tk.Button(root, text="Спарсить", command=start_parsing)
button.pack()

root.mainloop()
