from PIL import Image
import pytesseract
import io
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import fitz
from threading import Thread

class PdfReader:
    # Create the main window
    window = None
    progressbar = None
    file_button = None
    screenHeight = None
    screenWidth = None
    def __init__(self):
        self.window = tk.Tk()
        
        # Create the main window
        self.screenWidth = self.window.winfo_screenwidth()
        self.screenHeight = self.window.winfo_screenheight()

        x = (self.screenWidth / 2) - (300 / 2)
        y = (self.screenHeight / 2) - (200 / 2)

        self.window.geometry('300x200+%d+%d' % (x, y))
        self.window.title("PDF File/Folder Selector")

        # Create buttons for file and folder selection
        self.file_button = ttk.Button(self.window, text="Select PDF File", command=self.select_pdf_file)

        # Use grid to make the button fill the entire area
        self.file_button.grid(row=0, column=0, sticky="nsew")

        # Configure row and column weights to make the button expand
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Bind events for button hover
        self.file_button.bind('<Enter>', self.on_enter)
        self.file_button.bind('<Leave>', self.on_leave)
        self.progressbar = ttk.Progressbar()

    def on_enter(self, event):
        self.file_button.config(bg='gray')

    def on_leave(self, event):
        self.file_button.config(bg='SystemButtonFace')

    def convert_pdf_to_images(self, pdf_path):
        doc = fitz.open(pdf_path)
        images = []
        for page_number in range(doc.page_count):
            page = doc[page_number]
            image = page.get_pixmap()
            image_path = f"cache/page{page_number + 1}.png"
            image.pil_save(image_path)
            images.append(image_path)
        return images

    def extract_text_from_image(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="por")
        return text

    def handleStartCache(self):
        if os.path.exists("cache"):
            shutil.rmtree("cache")
        os.mkdir("cache")

    def handleFinish(self):
        if os.path.exists("cache"):
            shutil.rmtree("cache")
    
#Replace 'your_pdf_file.pdf' with the path to your PDF file

    def extract_text_from_pdf(self, pdf_path):
        extension = pdf_path[-4:]
        if extension == '.pdf':
            try:
                #self.file_button.config(state=tk.DISABLED)
                self.window.withdraw()
                progress_window = tk.Toplevel()
                progress_window.title(f"Convertendo {pdf_path}...")
                x = (self.screenWidth / 2) - (170 / 2)
                y = (self.screenHeight / 2) - (32/ 2)
                progress_window.geometry('%dx%d+%d+%d' % (170, 32, x, y))
                progress_window.overrideredirect(True)
                progress = tk.IntVar()
                progressbar = ttk.Progressbar(progress_window, variable=progress, length=160)
                self.handleStartCache()    
                image_paths = self.convert_pdf_to_images(pdf_path)
                progressbar.config(maximum=len(image_paths))
                
                

                
                progressbar.pack(padx=5, pady=5)
                progress_window.update_idletasks()
                with io.open(f"{pdf_path[:-4]}.txt", 'w', encoding="utf-8") as output:
                    print("with")
                    for i, image_path in enumerate(image_paths):
                        progress.set(i)
                        progress_window.update_idletasks()
                        print (self.progressbar)
                        print("extracting from:", i, image_path)
                        text_content = self.extract_text_from_image(image_path)
                        output.write(text_content)
                self.progressbar.place_forget()
                self.window.update_idletasks()
                progress_window.destroy()
                self.window.deiconify()
            except Exception as e:
                print(e)
            finally:
                self.handleFinish()
        else:
            print("Arquivo selecionado não é um pdf")

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        
        if file_path:
            # self.window.withdraw()
            # self.file_button.config(state=tk.DISABLED)
            self.window.update_idletasks()
            self.process_pdf_file(file_path)
            # self.file_button.config(state=tk.NORMAL)
            self.window.update_idletasks()
            # self.window.deiconify()

    def process_pdf_file(self, file_path):
        # Add your code to process the selected PDF file here
        print(f"Selected PDF File: {file_path}")
        t = Thread(target=lambda: self.extract_text_from_pdf(file_path))
        t.start()
        # t.join()
    
    def mainloop(self):
        self.window.mainloop()

# # Create the main window
# window = tk.Tk()
# screenWidth = window.winfo_screenwidth()
# screenHeight = window.winfo_screenheight()

# x = (screenWidth / 2) - (300 / 2)
# y = (screenHeight / 2) - (200 / 2)

# window.geometry('300x200+%d+%d' % (x, y))
# window.title("PDF File/Folder Selector")

# # Create buttons for file and folder selection
# file_button = tk.Button(window, text="Select PDF File", command=select_pdf_file)

# # Use grid to make the button fill the entire area
# file_button.grid(row=0, column=0, sticky="nsew")

# # Configure row and column weights to make the button expand
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)

# # Bind events for button hover
# file_button.bind('<Enter>', on_enter)
# file_button.bind('<Leave>', on_leave)

# Start the GUI main loop
app = PdfReader()
app.mainloop()