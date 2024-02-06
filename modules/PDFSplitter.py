import PyPDF2
import tkinter as tk
from tkinter import filedialog


class PDFSplitter:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Splitter")

        self.btn_load = tk.Button(master, text="Load PDF", command=self.load_pdf)
        self.btn_load.pack(pady=10)

        self.btn_split = tk.Button(master, text="Split PDF", command=self.split_pdf, state=tk.DISABLED)
        self.btn_split.pack(pady=10)

        self.file_path = None

    def load_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            self.btn_split["state"] = tk.NORMAL
            print(f"PDF Loaded: {self.file_path}")

    def split_pdf(self):
        if self.file_path:
            pdf_reader = PyPDF2.PdfReader(self.file_path)
            num_pages = len(pdf_reader.pages)

            for page_num in range(num_pages):
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(pdf_reader.pages[page_num])

                output_path = f"page_{page_num + 1}.pdf"
                with open(output_path, "wb") as output_file:
                    pdf_writer.write(output_file)

            print(f"PDF Split into {num_pages} pages.")

