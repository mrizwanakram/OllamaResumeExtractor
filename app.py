from flask import Flask, request, jsonify
from pdfminer.high_level import extract_text
from json_helper import InputData as input
import json  # Import for parsing JSON strings

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    return extract_text(pdf_path)

# API Route for POST request
@app.route('/extract-resume', methods=['POST'])
def extract_resume():
    """
    Endpoint to extract resume data.
    Accepts a PDF file via POST request and returns the extracted JSON data.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    # Get the file from the request
    file = request.files['file']
    
    # Save the file temporarily
    temp_pdf_path = 'temp_resume.pdf'
    file.save(temp_pdf_path)
    
    try:
        # Step 1: Extract text from the PDF
        text = extract_text_from_pdf(temp_pdf_path)

        # Step 2: Process text using the LLM
        llm = input.llm()
        raw_data = llm.invoke(input.input_data(text))
        
        # Step 3: Parse the raw JSON string into a dictionary
        data = json.loads(raw_data)  # Convert JSON string to Python dictionary

        # Step 4: Return the extracted data as JSON
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
