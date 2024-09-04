# ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from Convert_Currency import convert_currency
from Config import conversion_rates

def create_ui(root):
    # Set up variables
    from_currency_var = tk.StringVar(value='GEL')
    to_currency_var = tk.StringVar(value='USD')
    result_var = tk.StringVar()

    def handle_convert():
        try:
            amount = float(amount_entry.get())
            from_currency = from_currency_var.get()
            to_currency = to_currency_var.get()
            converted_amount = convert_currency(amount, from_currency, to_currency)
            result_var.set(f'{converted_amount:.2f} {to_currency}')
        except ValueError:
            result_var.set('Invalid input ')

    def clear_fields():
        amount_entry.delete(0, tk.END)
        result_var.set('')
        from_currency_var.set('GEL')
        to_currency_var.set('USD')

    # Create the UI components
    amount_label = tk.Label(root, text="Amount:")
    amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    from_currency_label = tk.Label(root, text="From:")
    from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values= list(conversion_rates.keys()), state="readonly")
    from_currency_menu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    to_currency_label = tk.Label(root, text="To:")
    to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values= list(conversion_rates.keys()), state="readonly")
    to_currency_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    convert_button = tk.Button(root, text="Convert", command=handle_convert)
    convert_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    clear_button = tk.Button(root, text="Clear", command=clear_fields)
    clear_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    result_label = tk.Label(root, text="Converted Amount:")
    result_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    result_display = tk.Label(root, textvariable=result_var)
    result_display.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    # Make the columns responsive
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    return amount_entry
