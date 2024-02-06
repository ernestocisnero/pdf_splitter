import tkinter as tk
from modules.PDFSplitter import PDFSplitter

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("250x250")
    app = PDFSplitter(root)
    root.mainloop()

