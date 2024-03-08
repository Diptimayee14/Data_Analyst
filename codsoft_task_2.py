import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window       
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")

entry = tk.Entry(root, font=("Segoe UI", 20), justify = "right")
entry.pack(fill=tk.BOTH, expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("Clear",)
]

# Create and pack widgets
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    
    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Segoe UI", 20), relief=tk.GROOVE)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

# Run the Tkinter event loop
root.mainloop()



        