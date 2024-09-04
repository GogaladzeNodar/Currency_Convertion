import tkinter as tk
from User_Interface import create_ui

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Currency Exchange Rate Calculator")

    # Create the UI
    create_ui(root)

    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()