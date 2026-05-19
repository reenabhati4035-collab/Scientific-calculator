import tkinter as tk
import math

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("520x700")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# ---------------- GLOBAL HISTORY ----------------
history_list = []

# ---------------- ENTRY FIELD ----------------
entry = tk.Entry(root, width=30, font=("Arial", 26),
                 bd=5, relief=tk.FLAT, justify="right",
                 bg="#2b2b2b", fg="white", insertbackground="white")
entry.pack(pady=15, padx=10, fill="both")

# ---------------- HISTORY BOX ----------------
history_box = tk.Text(root, height=6, font=("Arial", 12),
                      bg="#111", fg="lightgreen", bd=0)
history_box.pack(fill="both", padx=10, pady=5)

# ---------------- FUNCTIONS ----------------

def update_history(expr, result):
    history_list.append(f"{expr} = {result}")
    history_box.delete("1.0", tk.END)
    for item in history_list[-5:]:
        history_box.insert(tk.END, item + "\n")

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def safe_eval(expr):
    """
    Safer evaluation using restricted namespace
    """
    allowed = {
        "math": math,
        "sqrt": math.sqrt,
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": math.log10,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }
    return eval(expr, {"__builtins__": None}, allowed)

def calculate():
    try:
        expr = entry.get()

        # user-friendly replacements
        expr = expr.replace("π", "pi")
        expr = expr.replace("√", "sqrt")

        result = safe_eval(expr)

        update_history(expr, result)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def key_input(event):
    entry.insert(tk.END, event.char)

# ---------------- BUTTON FRAME ----------------
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sin',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('cos',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('tan',3,4),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('log',4,4),
    ('(',5,0), (')',5,1), ('√',5,2), ('π',5,3), ('e',5,4),
]

# ---------------- CREATE BUTTONS ----------------
for (text, row, col) in buttons:

    if text == '=':
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14), bg="#ff9500", fg="white",
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, width=6, height=2,
                        font=("Arial", 14),
                        bg="#333", fg="white",
                        activebackground="#555",
                        command=lambda t=text: click(t))

    btn.grid(row=row, column=col, padx=4, pady=4)

# ---------------- EXTRA BUTTONS ----------------
extra_frame = tk.Frame(root, bg="#1e1e1e")
extra_frame.pack(pady=10)

tk.Button(extra_frame, text="C", width=10, bg="red", fg="white",
          command=clear).grid(row=0, column=0, padx=5)

tk.Button(extra_frame, text="⌫", width=10, bg="#444", fg="white",
          command=backspace).grid(row=0, column=1, padx=5)

# ---------------- KEYBOARD SUPPORT ----------------
root.bind("<Key>", key_input)
root.bind("<Return>", lambda e: calculate())

# ---------------- RUN APP ----------------
root.mainloop()
