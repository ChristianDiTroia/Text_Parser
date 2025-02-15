from io import BytesIO
import pdfplumber
import re

class pdf_parser():

    def __init__(self, pdf_path: str):
        self.pdf = self.__read_pdf(pdf_path)
        self.parsed_sentences = ''
        self.parsed_lines = ''

    def __read_pdf(pdf_path: str):
        with open(pdf_path, 'rb') as file:
            bytes = file.read()
        return BytesIO(bytes) # read bytes into memory buffer and return the buffer
    
    def __parse_pdf_text(
            pdf_bytes: BytesIO,
            start_page: int = 0,
            end_page: int = None,
            crop_top: int = 50,
            crop_bottom: int = 75
            ):
        extracted_text = ""
        with pdfplumber.open(pdf_bytes) as pdf:
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
    def __protect_abbreviations(self, text: str) -> str:
        common_titles = re.compile(r"Mrs(\.\s?)|Mr(\.\s?)|Ms(\.\s?)|Dr(\.\s?)|Jr(\.\s?)|Sr(\.\s?)")
        return re.sub(common_titles, '\\1', text)

    def parse_sentences(self, text: str) -> list[str]:
        sentence_delimiters = re.compile(r"(?<!\.|[A-Z])[\.?!](?:\s|[\"'’”])")
        text = self.__protect_abbreviations(text)
        self.parsed_sentences = re.split(sentence_delimiters, text)

    # Concatenates words that are hyphenated across line breaks
    def __concat_hyphenated_words(self, text : str) -> str:
        hyphenated_word = re.compile(r"(-|–|—)\n(\w*)(\s|\.)?")
        return re.sub(hyphenated_word, r"\g<2>\n", text)

    def parse_lines(self, text: str) -> list[str]:
        text = self.__concat_hyphenated_words(text)
        newline = re.compile(r"\n")
        self.parsed_sentences = re.split(newline, text)