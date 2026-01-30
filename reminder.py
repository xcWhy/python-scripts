import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Reminder App")

# ------------------ VARIABLES (STATE) ------------------

title_var = tk.StringVar()
time_var = tk.IntVar(value=5)

# ------------------ FUNCTIONS (LOGIC) ------------------

def start_reminder():
    title = title_var.get()
    description = desc_text.get("1.0", tk.END).strip()
    seconds = time_var.get()

    if not title or seconds <= 0:
        messagebox.showwarning("Oops", "Please enter a title and time.")
        return

    status_label.config(text=f"Reminder set for {seconds} seconds")

    root.after(seconds * 1000, lambda: show_reminder(title, description))


def show_reminder(title, description):
    messagebox.showinfo(title, description)
    status_label.config(text="No active reminder")

# ------------------ UI ------------------

tk.Label(root, text="Reminder Title").pack()
tk.Entry(root, textvariable=title_var).pack()

tk.Label(root, text="Description").pack()
desc_text = tk.Text(root, height=4, width=30)
desc_text.pack()

tk.Label(root, text="Time (seconds)").pack()
tk.Spinbox(root, from_=1, to=3600, textvariable=time_var).pack()

tk.Button(root, text="Set Reminder", command=start_reminder).pack(pady=10)

status_label = tk.Label(root, text="No active reminder")
status_label.pack()

root.mainloop()
