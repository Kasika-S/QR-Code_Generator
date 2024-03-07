from tkinter.ttk import Label
import qrcode
import tkinter as tk
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter.ttk as ttk
from tkinter import filedialog
from reportlab.pdfgen import canvas

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
style = Style(theme='flatly')
style.theme_use()


def generate_qr_code():
    # Get the text entered by the user
    text = text_entry.get()

    # Create code from the text
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    #     Display the QR Code in the GUI
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.img = img_tk

    # Enable the "Print QR as PDF" button
    pdf_button.config(state="normal")


def print_qr_as_pdf():
    # Get the generated QR code image
    img = qrcode.make(text_entry.get())
    img = img.resize((300, 300))

    # Ask the user for a file path to save the PDF
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if file_path:
        # Create a PDF and add the QR code image
        pdf = canvas.Canvas(file_path)
        pdf.drawInlineImage(img, 100, 500)  # Adjust the position as needed
        pdf.save()


# Create a text input field for the text
text_label = ttk.Label(master=root, text="Enter text or URL:")
text_label.pack(pady=10)
text_entry = ttk.Entry(master=root, width=50)
text_entry.pack()

# Create a button to generate the QR Code
generate_button = ttk.Button(master=root, text="Generate QR Code",
                             command=generate_qr_code, style='sucesss.TButton')
generate_button.pack(pady=10)

# Create a button to print the QR Code as PDF (initially disabled)
pdf_button = ttk.Button(master=root, text="Print QR as PDF",
                        command=print_qr_as_pdf, style='success.TButton', state="disabled")
pdf_button.pack(pady=10)

# Create label to display the QR code
qr_label = ttk.Label(master=root)
qr_label.pack()

root.mainloop()
