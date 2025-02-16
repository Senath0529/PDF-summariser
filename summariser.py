import pdfplumber
from openai import OpenAI

def extract_text_from_pdf(pdf_path): # This function will extract the text from the PDF
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

openai_api_key = "PROVIDE THE OPENAI API KEY HERE"

def summarize_text(text, model="gpt-3.5-turbo"): # This function will summarize the text using the OpenAI API
    client = OpenAI(api_key=openai_api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following research paper in a professional manner:\n\n{text}"
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

def process_research_paper(pdf_path): # This function will extract the text from the PDF and summarize it
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    
    print("Generating summary...")
    summary = summarize_text(text)
    
    return summary

# Example usage
pdf_file = "PROVIDE THE PATH TO THE PDF FILE HERE"
summary = process_research_paper(pdf_file)

print("\n### Summary ###\n", summary)


