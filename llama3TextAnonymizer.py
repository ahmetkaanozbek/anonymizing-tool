import json
import ollama
import os
import PyPDF2

pdf_path = '/Users/kaanozbek/Desktop/sample.pdf'  # Path of PDF that will be converted to .txt
input_file = '/Users/kaanozbek/Desktop/converted_files/sample2.txt'  # Provide your input file name here
output_directory = '/Users/kaanozbek/Desktop/converted_files'  # Provide the output directory name here
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

# Now read the content of the text file and store it in the 'content' variable
with open(input_file, 'r', encoding='utf-8') as txt_file:
    content = txt_file.read()

prompt = """You are an AI assistant that identifies names of people and companies in a legal text that should be 
anonymized. Your answer should not contain anything other than the JSON format of anonymized information. For 
example, the JSON format in your answer should look like this: 
{ 
"people": [], 
"companies": [] 
}
Here is the text: """

response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': prompt + content
    },
])

json_str = response['message']['content']

# Verify the output of the llama3
print(json_str)


def extract_keys(json_str):
    data = json.loads(json_str)
    keys_array = []
    for key in data.keys():
        keys_array.extend(data[key])
    return keys_array


words_to_replace = extract_keys(json_str)


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
