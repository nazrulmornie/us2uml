import tkinter as tk

def greet():
    name = name_entry.get()
    greeting = f"Hello, {name}!"
    greeting_label.config(text=greeting)

window = tk.Tk()

window.title("User stories to UML Use Case Diagram")
window.geometry("700x500")

name_label = tk.Label(window, text="Enter your name")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

greet_button = tk.Button(window, text="Greet", command=greet)
greet_button.pack()

greeting_label = tk.Label(window, text="")
greeting_label.pack()

window.mainloop()