import tkinter as tk

root = tk.Tk()
root.title("The Snack Decider")
root.geometry("400x250")

label = tk.Label(root, text="Hungry? Let fate decide.", 
                 font=("Arial", 14), 
                 wraplength=350) 
label.pack(pady=30)

root.mainloop()

