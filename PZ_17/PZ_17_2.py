import tkinter as tk
from tkinter import messagebox

def SortInc3(A: float, B: float, C: float) -> tuple:
    arr = [A, B, C]
    sorted_arr = []
    num = float('infinity')
    for i in reversed(range(3)):
        for y in range(i+1):
            if arr[y] < num:
                index = y
                num = arr[y]
        sorted_arr.append(num)
        arr.pop(index)
        num = float('infinity')
    return sorted_arr[0], sorted_arr[1], sorted_arr[2]

def sort_numbers():
    try:
        A1 = float(entry_A1.get())
        B1 = float(entry_B1.get())
        C1 = float(entry_C1.get())
        A2 = float(entry_A2.get())
        B2 = float(entry_B2.get())
        C2 = float(entry_C2.get())
        
        sorted1 = SortInc3(A1, B1, C1)
        sorted2 = SortInc3(A2, B2, C2)
        
        result1_var.set(f"Sorted Set 1: {sorted1}")
        result2_var.set(f"Sorted Set 2: {sorted2}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

app = tk.Tk()
app.title("SortInc3 Function")

tk.Label(app, text="Set 1:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(app, text="A1:").grid(row=1, column=0, padx=5, pady=5)
entry_A1 = tk.Entry(app)
entry_A1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(app, text="B1:").grid(row=2, column=0, padx=5, pady=5)
entry_B1 = tk.Entry(app)
entry_B1.grid(row=2, column=1, padx=5, pady=5)

tk.Label(app, text="C1:").grid(row=3, column=0, padx=5, pady=5)
entry_C1 = tk.Entry(app)
entry_C1.grid(row=3, column=1, padx=5, pady=5)

tk.Label(app, text="Set 2:").grid(row=0, column=2, padx=5, pady=5)
tk.Label(app, text="A2:").grid(row=1, column=2, padx=5, pady=5)
entry_A2 = tk.Entry(app)
entry_A2.grid(row=1, column=3, padx=5, pady=5)

tk.Label(app, text="B2:").grid(row=2, column=2, padx=5, pady=5)
entry_B2 = tk.Entry(app)
entry_B2.grid(row=2, column=3, padx=5, pady=5)

tk.Label(app, text="C2:").grid(row=3, column=2, padx=5, pady=5)
entry_C2 = tk.Entry(app)
entry_C2.grid(row=3, column=3, padx=5, pady=5)

sort_button = tk.Button(app, text="Sort", command=sort_numbers)
sort_button.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

result1_var = tk.StringVar()
result2_var = tk.StringVar()

tk.Label(app, textvariable=result1_var).grid(row=5, column=0, columnspan=4, padx=5, pady=5)
tk.Label(app, textvariable=result2_var).grid(row=6, column=0, columnspan=4, padx=5, pady=5)

app.mainloop()
