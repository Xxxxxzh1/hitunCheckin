#!usr/local/bin/python3

import tkinter as tk
from tkinter import ttk
import hitunCheckin as hitun


root = tk.Tk()
root.title('Hitun Checkin')
root.geometry('300x250')


def check():
    outMessage = ''
    inputUsername = userName.get()
    inputPassWord = passWord.get()
    outMessage = hitun.checkIn(inputUsername, inputPassWord)
    tk.Label(root, text=outMessage, fg='blue', width=20, height=1, anchor='c').grid(row=3, column=1)


tk.Label(root, text='username:', anchor='c').grid(row=0)
userName = tk.Entry(root, fg='black', bg='LightYellow')
userName.grid(row=0, column=1)

tk.Label(root, text='password:', anchor='c').grid(row=1)
passWord = tk.Entry(root, fg='black', bg='LightYellow', show='*')
passWord.grid(row=1, column=1)

exitButton = ttk.Button(root, text='Exit', command=root.quit)
exitButton.grid(row=2, column=0)

checkinButton = ttk.Button(root, text='Checkin', command=check)
checkinButton.grid(row=2, column=1)

root.mainloop()
