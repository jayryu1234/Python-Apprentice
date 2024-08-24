"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk

# Create a window object
window = Tk()     # Create a window object

# Hide the window, hint: use the withdraw method
window.withdraw() # Hide the window; we just want to see pop ups
# Ask the user for the first number   
add1 = simpledialog.askinteger("#1", "What's the first number?") 
# Ask the user for the second number
add2 = simpledialog.askinteger("#2", "What's the second number?") 
# Display the sum of the two numbers 
message = add1 + add2
messagebox.showinfo('What you are', message)
# Keep the window open

window.mainloop()  # Keeps the window open

