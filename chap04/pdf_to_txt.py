import os
import pymupdf

pdf_file_path = r"C:\llm_agent\chap04\data\식물자원분야 - 다시, 광합성을 생각한다.pdf"

doc = pymupdf.open(pdf_file_path)

full_text = ''

for page in doc:
    text = page.get_text()
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

txt_file_path = f"output/{pdf_file_name}.txt"

with open(txt_file_path, "w", encoding="utf-8") as f:
    f.write(full_text)