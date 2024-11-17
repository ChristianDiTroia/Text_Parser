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
        for page in pdf.pages[start_page-1:end_page]:
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
    pattern = re.compile(r"(?<!\.)\.(?:\s|’)")
    return re.split(pattern, text)

def parse_by_line(text : str):
    hyphen_newline_pattern = re.compile(r"(-\n\w*(\s|\.)\s)")
    line_pattern = re.compile(r"(?<!-)\n")
    # Concatenate words that span across lines to the same line
    for match in re.finditer(hyphen_newline_pattern, text):
        text = text[:match.end() - 1] + "\n" + text[match.end():] # Replace whitespace after each match with \n
        matched_str = match.group(0)
        print(matched_str)
        # text = text.replace(matched_str, matched_str.replace("\n", ""))
    return re.split(line_pattern, text)

def main():
    parsed_gatsby = parse_by_sentence(parse_pdf_text("./the-great-gatsby.pdf"))
    for line in parsed_gatsby:
        print(line)
    print(len(parsed_gatsby))
    
if __name__ == '__main__':
    main()