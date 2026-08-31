############## TABLE GENERATOR ##########
# GUi

import tkinter as tk
from tkinter import messagebox, ttk

def generate_table():
    # Clear previous output
    output_box.delete("1.0", tk.END)
    
    user_input = entry_number.get().strip()
    
    # Check for empty input
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a number.")
        return
        
    # Validate and perform math
    try:
        n = int(user_input)
        table_text = f"=== Multiplication Table for {n} ===\n\n"
        for i in range(1, 11):
            table_text += f"{n}  x  {i:2d}  =  {n * i}\n"
        
        output_box.insert(tk.END, table_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Error: Please enter a valid whole number.")

# Window setup
root = tk.Tk()
root.title("Table Generator")
root.geometry("380x420")
root.resizable(False, False)

# Header
title_label = ttk.Label(root, text="Multiplication Table Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=15)

# Input Row
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Enter Number:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

entry_number = ttk.Entry(input_frame, width=10, font=("Arial", 10))
entry_number.pack(side=tk.LEFT, padx=5)
entry_number.focus() # Automatically places the cursor in the text box

# Generate Button
btn_generate = ttk.Button(root, text="Generate Table", command=generate_table)
btn_generate.pack(pady=10)

# Pressing 'Enter' on the keyboard triggers the button automatically
root.bind('<Return>', lambda event: generate_table())

# Display Box
output_box = tk.Text(root, width=32, height=13, font=("Consolas", 10))
output_box.pack(pady=10, padx=15)

# Run GUI application loop
root.mainloop()
#  This program generates a multiplication table for a given number.
