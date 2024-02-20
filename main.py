import customtkinter
from modules.PDFSplitter import PDFSplitter

customtkinter.set_appearance_mode("dark") # light, system
customtkinter.set_default_color_theme("green") # blue, green, dark-blue 


if __name__ == "__main__":
    root=customtkinter.CTk()
    root.geometry("220x220")
    app = PDFSplitter(root)
    root.mainloop()

