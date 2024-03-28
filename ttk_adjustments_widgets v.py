import tkinter as tk
from tkinter import ttk, font


from colorlist import *
# Function to update the button's style based on user selections
def update_style():
    # Create a unique style name for the button
    style_name = "Dynamic.TButton"
    style.configure(style_name, background=color_var.get(), font=(font_var.get(), 10), borderwidth=size_var.get())
    listbox.config(font=(font_var.get(), 10), bg=color_var.get(), borderwidth=size_var.get())
    style_name = "Dynamic.TButton"
    label_style_name = "Dynamic.TLabel"
    entry_style_name = "Dynamic.TEntry"
    checkbutton_style_name = "Dynamic.TCheckbutton"
    radiobutton_style_name = "Dynamic.TRadiobutton"
    style.configure("Dynamic.TLabel", background=color_var.get(), font=(font_var.get(), 10))
    label.configure(style="Dynamic.TLabel")
    style.configure("Dynamic.TEntry", font=(font_var.get(), 10))
    entry.configure(style="Dynamic.TEntry")
    text.config(font=(font_var.get(), 10), borderwidth=size_var.get())
    style.configure("Dynamic.TCheckbutton", font=(font_var.get(), 10))
    checkbutton.configure(style="Dynamic.TCheckbutton")
    style.configure("Dynamic.TCheckbutton", font=(font_var.get(), 10))
    checkbutton.configure(style="Dynamic.TCheckbutton")

    style.configure("Dynamic.TRadiobutton", font=(font_var.get(), 10))
    radiobutton1.configure(style="Dynamic.TRadiobutton")
    radiobutton2.configure(style="Dynamic.TRadiobutton")

    style.configure("Dynamic.TRadiobutton", font=(font_var.get(), 10))
    radiobutton1.configure(style="Dynamic.TRadiobutton")
    radiobutton2.configure(style="Dynamic.TRadiobutton")

    # Configure styles
    style.configure(style_name, background=color_var.get(), font=(font_var.get(), 10), borderwidth=size_var.get())
    style.configure(label_style_name, background=color_var.get(), font=(font_var.get(), 10))
    style.configure(entry_style_name, font=(font_var.get(), 10))
    style.configure(checkbutton_style_name, font=(font_var.get(), 10))
    style.configure(radiobutton_style_name, font=(font_var.get(), 10))
    
    # Apply styles to widgets
    test_button.configure(style=style_name)
    label.configure(style=label_style_name)
    entry.configure(style=entry_style_name)
    checkbutton.configure(style=checkbutton_style_name)
    radiobutton1.configure(style=radiobutton_style_name)
    radiobutton2.configure(style=radiobutton_style_name)
    
    # Direct config for widgets that don't use ttk styles
    text.config(font=(font_var.get(), 10), bg=color_var.get(), borderwidth=size_var.get())

# Initialize main window
root = tk.Tk()
root.title("TTK Theme Tester")
fontlist=[]
font_families = font.families()
for family in font_families:
    fontlist = [f for f in font_families]
    
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

color_combobox = ttk.Combobox(controls_frame, textvariable=color_var, values=colors)
color_combobox.pack()
color_combobox.bind('<<ComboboxSelected>>', lambda e: update_style())

# Combobox for font selection
font_var = tk.StringVar(value="Arial")

font_combobox = ttk.Combobox(controls_frame, textvariable=font_var, values=fontlist)
font_combobox.pack()
font_combobox.bind('<<ComboboxSelected>>', lambda e: update_style())

# Test Button to apply the dynamic styles
style = ttk.Style()
test_button = ttk.Button(root, text="Test Button")
test_button.pack(pady=20)
radio_var = tk.StringVar(value="1")
radiobutton1 = ttk.Radiobutton(root, text="Option 1", value="1", variable=radio_var)
radiobutton2 = ttk.Radiobutton(root, text="Option 2", value="2", variable=radio_var)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)
check_var = tk.BooleanVar()
checkbutton = ttk.Checkbutton(root, text="Check this", variable=check_var)
checkbutton.pack(pady=5)
text = tk.Text(root, height=5, width=50)
text.pack(pady=5)
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var)
entry.pack(pady=5)

label = ttk.Label(root, text="This is a label")
label.pack(pady=5)


listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.pack(pady=5)
root.mainloop()
