import pandas as pd
import pdfplumber

print("✅ Pandas and PDFPlumber are working!")

# Test creating a DataFrame
df = pd.DataFrame({"Item": ["Burger", "Fries", "Drink"], "Price": [5.99, 2.99, 1.50]})
print(df)

# Test extracting text from a PDF (replace 'invoice.pdf' with an actual file)
pdf_path = "../data/raw_invoices/sample_invoice.pdf"
try:
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        print("\nExtracted Text from PDF:\n", text)
except:
    print("\n⚠️ No PDF file found, but everything else is working!")