import tkinter as tk
from sandbox import find_alias_match, print_format

def search():
    input_string = entry.get()
    output = find_alias_match(input_string, "drugs.json")
    if output == None:
        output = "Nothing was found"
        output_text.config(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, output)
        output_text.config(state=tk.DISABLED)
    else:
        output = print_format(input_string, output)
        output_text.config(state=tk.NORMAL)
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, output)
        output_text.config(state=tk.DISABLED)

# Create tkinter window
window = tk.Tk()
window.title("Alias Search")

#label

label = tk.Label(window, text="TTRU Search Tool")
label.pack(anchor=tk.W, padx=10, pady=10)

# Input field
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Search button
button = tk.Button(window, text="Search", command=search)
button.pack(pady=5)

# Output text
output_text = tk.Text(window, height=20, width=125)
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)

# Start the tkinter event loop
window.mainloop()
