from PIL import Image
import os
from PyPDF2 import PdfWriter, PageObject


def images_to_pdf(image_paths, pdf_output):
    pdf_writer = PdfWriter()
    for image_path in image_paths:
        image = Image.open(image_path)
        width, height = image.size
        po = PageObject().create_blank_page(width=width, height=height)
        pdf_page = pdf_writer.add_page(page=po)
        pdf_page.merge_page(image.convert("RGB"))
        image.close()
    with open(pdf_output, "wb") as f:
        pdf_writer.write(f)


def main():
    image_folder = "images"  # Change this to the folder containing your images
    pdf_output = "output.pdf"  # Change this to the desired output PDF file name

    # Get a list of image files in the folder
    image_files = [
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.endswith((".png", ".jpg", ".jpeg"))
    ]

    # Merge images into PDF
    images_to_pdf(image_files, pdf_output)
    print("PDF created successfully!")
    # print(image_files)


if __name__ == "__main__":
    main()
