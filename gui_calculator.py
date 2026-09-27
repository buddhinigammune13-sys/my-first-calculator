import tkinter as tk
import re

def button_click(item):
    """Appends the clicked button's text to the display."""
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    """Clears the entire display."""
    display_var.set("")

def button_backspace():
    """Removes the last character from the display."""
    current = display_var.get()
    display_var.set(current[:-1])

def button_equal():
    """Evaluates the math expression using BODMAS."""
    expr = display_var.get()
    
    try:
        # Fix implicit multiplication for BODMAS 
        # e.g., turns "5(6)" into "5*(6)" and "(2)(3)" into "(2)*(3)"
        expr = re.sub(r'(\d)\(', r'\1*(', expr)
        expr = re.sub(r'\)(\d)', r')*\1', expr)
        expr = re.sub(r'\)\(', r')*(', expr)

        # eval() automatically respects BODMAS order of operations
        result = str(eval(expr))
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Error: Div by Zero")
    except Exception:
        display_var.set("Error")

# 1. Setup the main window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("350x500")
root.configure(bg="#f0f0f0")
root.minsize(300, 450)

# 2. Configure the grid to be responsive
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.grid_rowconfigure(0, weight=0)
for i in range(1, 6): 
    root.grid_rowconfigure(i, weight=1)

# 3. Create the display variable and entry widget
display_var = tk.StringVar()
display = tk.Entry(
    root, 
    textvariable=display_var, 
    font=('Arial', 24, 'bold'), 
    bg="white", 
    bd=0, 
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=15, padx=10, sticky="nsew")

# 4. Define the updated button layout
# Replaced '00' with '⌫' (Backspace) and reorganized the top row
buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

# 5. Generate and place the buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 16, 'bold'), command=button_equal, bg="#4CAF50", fg="white", bd=0)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 16, 'bold'), command=button_clear, bg="#f44336", fg="white", bd=0)
    elif text == '⌫':
        btn = tk.Button(root, text=text, font=('Arial', 16, 'bold'), command=button_backspace, bg="#ff9800", fg="white", bd=0)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 16, 'bold'), command=lambda t=text: button_click(t), bg="#ffffff", bd=0)
    
    btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

# 6. Start the application
root.mainloop()