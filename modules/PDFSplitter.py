import PyPDF2
from tkinter import filedialog
import customtkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification


customtkinter.set_appearance_mode("dark") # light, system
customtkinter.set_default_color_theme("green") # blue, green, dark-blue


class PDFSplitter:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Splitter")

        self.btn_load = customtkinter.CTkButton(master, text="Load PDF", command=self.load_pdf)
        self.btn_load.pack(pady=10)

        self.btn_split = customtkinter.CTkButton(master, text="Split PDF", command=self.split_pdf, state="disabled")
        self.btn_split.pack(pady=10)
        
        self.loadedToast = ToastNotification(
        title="PDF Splitter",
        message="PDF LOADED",
        position=(400, 300, "ne"),
        alert=True,
        duration=1200,
        bootstyle=SUCCESS
        )
        
        self.splittedToast = ToastNotification(
        title="PDF Splitter",
        message="PDF SPLITTED",
        position=(400, 300, "ne"),
        alert=True,
        duration=1200,
        bootstyle=SUCCESS
        )
        
        self.file_path = None

    def load_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            self.btn_split.configure(state="normal")
            self.loadedToast.show_toast()
            
            
    '''
    # creating a pdf reader object 
    reader = PdfReader('E3009873941_053000.pdf') 
    
    # printing number of pages in pdf file 
    print(len(reader.pages)) 
    
    # getting a specific page from the pdf file 
    page = reader.pages[1] 
    
    # extracting text from page 
    text = page.extract_text() 
    if "SC01" in text:
        print("SUCCESS")
    else:
        print("FAILED")

    '''


    def split_pdf(self):
        if self.file_path:
            pdf_reader = PyPDF2.PdfReader(self.file_path)
            
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):              
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])

                output_path = f"page_NAME_{page_num + 1}.pdf"
                with open(output_path, "wb") as output_file:
                    pdf_writer.write(output_file)
                    
            self.splittedToast.show_toast()

