from pypdf import PdfReader
import unicodedata
import re

def remove_control_characters(string: str):
    return "".join(ch for ch in string if unicodedata.category(ch)[0]!="C")

def parse_pdf_lines(
        pdf : str, 
        start_page : int = 0, 
        end_page : int = None, 
        remove_patterns : list[str] = None):
    pdf_reader = PdfReader(pdf)
    compiled_remove_patterns = [re.compile(pattern) for pattern in remove_patterns]
    lines = []
    for page in pdf_reader.pages[start_page:end_page]:
        txt = remove_control_characters(page.extract_text())
        for pattern in compiled_remove_patterns:
            txt = re.sub(pattern, "", txt, 1)
        lines.extend(map(lambda s : s.strip(), re.split("\.", txt)))
    return lines

def main():
    gatsby_lines = parse_pdf_lines(
        './the-great-gatsby.pdf', 
        start_page=2,
        remove_patterns=["Free eBooks at Planet eBook.com", "The Great Gatsby", "Chapter \d+"]
    )
    for line in gatsby_lines:
        print(line)
    
if __name__ == '__main__':
    main()