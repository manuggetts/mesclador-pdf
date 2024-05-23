import PyPDF2
import os

def merge_pdfs(input_folder, output_file):
    merger = PyPDF2.PdfMerger()

    lista_arquivos = os.listdir(input_folder)
    lista_arquivos.sort()

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(".pdf"):
            arquivo_path = os.path.join(input_folder, arquivo)
            merger.append(arquivo_path)

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file, "wb") as merged_pdf:
        merger.write(merged_pdf)

    print(f"Arquivos mesclados em {output_file}")

if __name__ == "__main__":
    input_folder = "arquivos"
    output_file = "PdfMesclado.pdf"
    merge_pdfs(input_folder, output_file)