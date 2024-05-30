'''
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу
'''
import tkinter as tk
from tkinter import ttk


class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['foreground']
        self._is_placeholder = True

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

        self._add_placeholder()

    def _clear_placeholder(self, event=None):
        if self._is_placeholder:
            self.delete(0, tk.END)
            self['foreground'] = self.default_fg_color
            self._is_placeholder = False

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['foreground'] = self.placeholder_color
            self._is_placeholder = True


def sign_up():
    print("Sign Up button clicked")


root = tk.Tk()
root.title("Contact Us")
root.geometry("230x500")
root.resizable(False, False)

# Изменение цвета фона всего окна
root.configure(bg='lightgray')
style = ttk.Style()

style.configure('Custom.TFrame', background='lightgray')

frame = ttk.Frame(root, padding="10 10 10 10", style='Custom.TFrame')
frame.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

title_frame = tk.Frame(root, bg='darkgray')
title_frame.grid(column=0, row=0, sticky=(tk.W, tk.E))

title_label = tk.Label(title_frame, text="Contact Us", font=('Helvetica', 18, 'bold'), bg='darkgray', fg='black')
title_label.pack(padx=50, pady=15, fill=tk.X)

style.configure("Custom.TLabel", background='lightgray')

ttk.Label(frame, text="First Name", style="Custom.TLabel").grid(column=1, row=1, sticky=tk.W, pady=(2, 0))
first_name = PlaceholderEntry(frame, placeholder="First Name")
first_name.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(frame, text="Last Name", style="Custom.TLabel").grid(column=1, row=3, sticky=tk.W, pady=(2, 0))
last_name = PlaceholderEntry(frame, placeholder="Smith")
last_name.grid(column=1, row=4, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(frame, text="Email", style="Custom.TLabel").grid(column=1, row=5, sticky=tk.W, pady=(2, 0))
email = PlaceholderEntry(frame, placeholder="Email address")
email.grid(column=1, row=6, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(frame, text="Website", style="Custom.TLabel").grid(column=1, row=7, sticky=tk.W, pady=(2, 0))
website = PlaceholderEntry(frame, placeholder="www.example.com")
website.grid(column=1, row=8, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(frame, text="Password", style="Custom.TLabel").grid(column=1, row=9, sticky=tk.W, pady=(2, 0))
password = PlaceholderEntry(frame, placeholder="8-10 characters", show="*")
password.grid(column=1, row=10, sticky=(tk.W, tk.E), pady=(0, 10))

ttk.Label(frame, text="Password Confirmation", style="Custom.TLabel").grid(column=1, row=11, sticky=tk.W, pady=(2, 0))
password_confirmation = PlaceholderEntry(frame, placeholder="Type your password again", show="*")
password_confirmation.grid(column=1, row=12, sticky=(tk.W, tk.E), pady=(0, 10))

sign_up_button = ttk.Button(frame, text="Sign Up", command=sign_up, width=9)
sign_up_button.grid(column=1, row=13, sticky=tk.W, pady=(10, 0))

for child in frame.winfo_children():
    child.grid_configure(padx=5)

root.mainloop()