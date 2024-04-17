import tkinter as tk
from sandbox import find_alias_match, print_format

def search():
    input_string = entry.get()
    output = find_alias_match(input_string, "drugs.json")
    output = print_format(output)
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)

# Create tkinter window
window = tk.Tk()
window.title("Alias Search")

# Input field
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Search button
button = tk.Button(window, text="Search", command=search)
button.pack(pady=5)

# Output text
output_text = tk.Text(window, height=10, width=50)
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)

# Start the tkinter event loop
window.mainloop()
