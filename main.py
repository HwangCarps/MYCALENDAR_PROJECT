import tkinter as tk
from ui.calendar_ui import create_calendar_ui

def main():
    root = tk.Tk()
    root.title("MyRoute Calendar")
    root.geometry("800x600")

    create_calendar_ui(root)

    root.mainloop()

if __name__ == "__main__":
    main()