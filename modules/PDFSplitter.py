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
        
        self.main_label = customtkinter.CTkLabel(master,text="SPLIT PDF", font=("Helvetica",18))
        self.main_label.pack(pady=10)

        self.btn_load = customtkinter.CTkButton(master, text="Load PDF", command=self.load_pdf)
        self.btn_load.pack(pady=10)

        self.btn_split = customtkinter.CTkButton(master, text="Split PDF", command=self.split_pdf, state="disabled")
        self.btn_split.pack(pady=10)
        
        self.numberSC = 0;
        self.numberPA = 0;
        self.numberBM = 0;
        
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
        
        self.notFoundToast = ToastNotification(
        title="NOT FOUND",
        message="None of SC, PA, or BM was found in the file.",
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


    def split_pdf(self):
        if self.file_path:
            pdf_reader = PyPDF2.PdfReader(self.file_path)
            title = pdf_reader.metadata.title # get rid of the _00 at the edn of the filename. use split method
            title = title.split("_")
            
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):   
                
                if "SC01" in pdf_reader.pages[page_num].extract_text():
                    print("SUCCESS")
                    self.numberSC +=1
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                    output_path = f"{title}-SC0{self.numberSC}.pdf"
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)
                        
                elif "PA01" in pdf_reader.pages[page_num].extract_text():
                    print("SUCCESS")
                    self.numberPA+=1
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                    output_path = f"{title}-PA0{self.numberPA}.pdf"
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file) 
                        
                elif "BM01" in pdf_reader.pages[page_num].extract_text():
                    print("SUCCESS")
                    self.numberBM+=1
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                    output_path = f"{title}-BM0{self.numberBM}.pdf"
                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)    
                else:
                    print("None of SC, PA, or BM was found in the file.")   
            self.splittedToast.show_toast()

