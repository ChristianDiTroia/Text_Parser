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

# Removes periods from common titles to prevent parsing as a sentence
def protect_abbreviations(text: str) -> str:
    common_titles = re.compile(r"Mrs(\.\s?)|Mr(\.\s?)|Ms(\.\s?)|Dr(\.\s?)|Jr(\.\s?)|Sr(\.\s?)")
    return re.sub(common_titles, '\\1', text)

def parse_by_sentence(text: str) -> list[str]:
    sentence_delimiters = re.compile(r"(?<!\.|[A-Z])[\.?!](?:\s|[\"'’”])")
    text = protect_abbreviations(text)
    return re.split(sentence_delimiters, text)

def concat_hyphenated_words(text: str) -> str:
    hyphens = [r'-', r'–', r'—']
    for hyphen in hyphens:
        hyphenated = re.compile(hyphen + r"\n")
        text = re.sub(hyphenated, hyphen, text)
    return text

def parse_by_line(text: str) -> list[str]:
    text = concat_hyphenated_words(text)
    newline = re.compile(r"\n")
    return re.split(newline, text)

def main():
    parsed_gatsby = parse_by_sentence(parse_pdf_text('./the-great-gatsby.pdf'))
    for line in parsed_gatsby:
        print(line)
    print(len(parsed_gatsby))
    
if __name__ == '__main__':
    main()