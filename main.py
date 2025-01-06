from pdfminer.high_level import extract_text
from json_helper import InputData as input

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    return extract_text(pdf_path)

def save_to_file(file_path, data):
    """Save data to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

# Step 1: Extract text from the PDF
pdf_path = '22.pdf'
text = extract_text_from_pdf(pdf_path)

# Step 2: Process text using the LLM
llm = input.llm()
data = llm.invoke(input.input_data(text))

# Step 3: Save the processed data to a file
output_file = 'output22.json'  # You can change the extension to .txt if preferred
save_to_file(output_file, data)

print(f"Data has been saved to {output_file}")
