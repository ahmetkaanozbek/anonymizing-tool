import os
import PyPDF2

pdf_path = '/Users/kaanozbek/Desktop/denemeler.pdf'  # Path of PDF that will be converted to .txt
input_file = '/Users/kaanozbek/Desktop/deneme/selam.txt'  # Provide your input file name here
output_directory = '/Users/kaanozbek/Desktop/deneme'  # Provide the output directory name here
words_to_replace = ['VIEN&VIENNA Mobilyacılık Tic. Ltd. Şti', 'Batuhan Büyükusta', 'Av. Ali Akarca']  # List the
# words you want to replace
new_word = "ANONYMIZED"  # The word that will be used to replace


def pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


pdf_to_text(pdf_path, input_file)


def replace_words_in_file(input_file, output_directory, words_to_replace):
    # Read the content of the input file
    with open(input_file, 'r') as file:
        file_content = file.read()

    # Replace the words in the content
    for word in words_to_replace:
        file_content = file_content.replace(word, new_word)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Write the modified content to a new file in the output directory
    output_file = os.path.join(output_directory, os.path.basename(input_file))
    with open(output_file, 'w') as file:
        file.write(file_content)

    print(f"File with replaced words saved at: {output_file}")


replace_words_in_file(input_file, output_directory, words_to_replace)
