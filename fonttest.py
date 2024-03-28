import tkinter as tk
from tkinter import font

root = tk.Tk()
root.withdraw()  # We don't need the Tk window, but need to initialize the Tkinter environment

font_families = font.families()
sysfont = []
# Print the list of available font families
for family in font_families:
    print(family)
    

root.destroy()  # Clean up the Tk window
