import pdfplumber
import re

def parse_pdf_text(
        pdf_path : str,
        start_page : int = 0,
        end_page : int = None,
        crop_top: int = 50,
        crop_bottom : int = 75
        ):
    extracted_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages[start_page:end_page]:
            width, height = page.width, page.height
            cropped_page = page.within_bbox((
                0, 
                crop_top, 
                width, 
                height - crop_bottom
            ))
            extracted_text += cropped_page.extract_text() + "\n"
    return extracted_text

def parse_by_sentence(text : str):
    pattern = re.compile(r"(?<!\.)\.(?!\.)(\s|')")
    return re.split(pattern, text)

def parse_by_line(text : str):
    pattern = re.compile(r"(?<!-)\n")
    return re.split(pattern, text)

def main():
    parsed_gatsby = parse_by_sentence(parse_pdf_text("./the-great-gatsby.pdf"))
    for line in parsed_gatsby:
        print(line)
    print(len(parsed_gatsby))
    
if __name__ == '__main__':
    main()