import tkinter as tk
from tkinter import ttk

# Function to update the button's style based on user selections
def update_style():
    # Create a unique style name for the button
    style_name = "Dynamic.TButton"
    style.configure(style_name, background=color_var.get(), font=(font_var.get(), 10), borderwidth=size_var.get())
    test_button.configure(style=style_name)

# Initialize main window
root = tk.Tk()
root.title("TTK Theme Tester")

# Configure the ttk theme to use
current_theme = ttk.Style().theme_use()

# Create a frame for the controls
controls_frame = ttk.Frame(root)
controls_frame.pack(pady=20)

# Dropdown to select theme
theme_var = tk.StringVar(value=current_theme)
themes = ttk.Style().theme_names()
theme_combobox = ttk.Combobox(controls_frame, textvariable=theme_var, values=themes)
theme_combobox.pack()
theme_combobox.bind('<<ComboboxSelected>>', lambda e: ttk.Style().theme_use(theme_var.get()))

# Slider for changing the border size
size_var = tk.IntVar(value=1)
size_slider = ttk.Scale(controls_frame, from_=1, to=10, orient="horizontal", variable=size_var, command=lambda e: update_style())
size_slider.pack()

# Combobox for background color selection
color_var = tk.StringVar(value="white")
colors = ["white", "red", "green", "blue", "yellow"]
color_combobox = ttk.Combobox(controls_frame, textvariable=color_var, values=colors)
color_combobox.pack()
color_combobox.bind('<<ComboboxSelected>>', lambda e: update_style())

# Combobox for font selection
font_var = tk.StringVar(value="Arial")
fonts = ["Arial", "Helvetica", "Times", "Courier"]
font_combobox = ttk.Combobox(controls_frame, textvariable=font_var, values=fonts)
font_combobox.pack()
font_combobox.bind('<<ComboboxSelected>>', lambda e: update_style())

# Test Button to apply the dynamic styles
style = ttk.Style()
test_button = ttk.Button(root, text="Test Button")
test_button.pack(pady=20)

# Update the style initially to apply default settings
update_style()

root.mainloop()
