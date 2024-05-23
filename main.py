import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_file):
    output_dir = os.path.dirname(output_file)
    print(f"Output directory: '{output_dir}'")
    
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pdf_writer = PdfWriter()

    for item in os.listdir(input_folder):
        if item.endswith('.pdf'):
            item_path = os.path.join(input_folder, item)
            pdf_reader = PdfReader(item_path)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(output_file, 'wb') as out_file:
        pdf_writer.write(out_file)

if __name__ == "__main__":
    input_folder = 'C:/Users/manug/Desktop/RPA/mesclador-pdf/arquivos'
    output_file = 'C:/Users/manug/Desktop/RPA/mesclador-pdf/arquivos/merged.pdf'
    merge_pdfs(input_folder, output_file)