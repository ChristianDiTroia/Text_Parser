import pdfplumber, re, random
from io import BytesIO


class text_parser:

    def __init__(self, pdf_path: str):
        self.pdf = self.read_pdf(pdf_path)
        self.__lines = ""
        self.__next_line = 0
        self.__sentences = ""
        self.__next_sentence = 0

    def parse_text(
        self,
        start_page: int = 0,
        end_page: int = None,
        top_crop: int = 50,
        bottom_crop: int = 75,
    ) -> tuple[list[str], list[str]]:
        text = self.extract_pdf_text(
            self.pdf, start_page, end_page, top_crop, bottom_crop
        )
        """Parse and store each sentence and line from the text"""
        self.__lines = self.parse_lines(text)
        self.__sentences = self.parse_sentences(text)
        return (self.__lines, self.__sentences)

    def get_next_line(self) -> str:
        return self.get_next_lines(1)[0]

    def get_next_lines(self, num_lines: int) -> list[str]:
        lines = self.get_lines(self.__next_line, self.__next_line + num_lines)
        self.__next_line = self.__next_line + num_lines % self.num_lines()
        return lines

    def get_lines(self, start: int = None, end: int = None) -> list[str]:
        return self.__lines[start:end]

    def num_lines(self) -> int:
        return len(self.__lines)

    def get_next_sentence(self) -> str:
        return self.get_next_sentences(1)[0]

    def get_next_sentences(self, num_sentences: int) -> list[str]:
        sentences = self.get_sentences(
            self.__next_sentence, self.__next_sentence + num_sentences
        )
        self.__next_sentence = (
            self.__next_sentence + num_sentences
        ) % self.num_sentences()
        return sentences

    def get_sentences(self, start: int, end: int = None):
        return self.__sentences[start:end]

    def num_sentences(self) -> int:
        return len(self.__sentences)

    def shuffle_lines(self, seed: int = None):
        random.seed(seed)
        random.shuffle(self.__lines)

    def shuffle_sentences(self, seed: int = None):
        random.seed(seed)
        random.shuffle(self.__sentences)

    ### static variables ###

    # TODO patterns here

    ### static methods ###

    @staticmethod
    def read_pdf(pdf_path: str) -> BytesIO:
        with open(pdf_path, "rb") as file:
            bytes = file.read()
        return BytesIO(bytes)

    @staticmethod
    def extract_pdf_text(
        pdf: str | BytesIO,
        start_page: int,
        end_page: int,
        top_crop: int,
        bottom_crop: int,
    ) -> str:
        """Returns all the text in a given pdf within the cropped bounds as a string"""
        extracted_text = ""
        with pdfplumber.open(pdf) as pdf:
            for page in pdf.pages[start_page - 1 : end_page]:
                width, height = page.width, page.height
                cropped_page = page.within_bbox(
                    (0, top_crop, width, height - bottom_crop)
                )
                extracted_text += cropped_page.extract_text() + "\n"
        return extracted_text

    # Concatenates words that are hyphenated across line breaks
    @staticmethod
    def concat_hyphenated_words(text: str) -> str:
        hyphenated_word = re.compile(r"(-|–|—)\n(\w*)(\s|\.)?")
        return re.sub(hyphenated_word, r"\g<2>\n", text)

    @staticmethod
    def parse_lines(text: str) -> list[str]:
        text = text_parser.concat_hyphenated_words(text)
        newline = re.compile(r"\n")
        return re.split(newline, text)

    @staticmethod
    def parse_sentences(text: str) -> list[str]:
        sentence_delimiters = re.compile(r"(?<!\.|[A-Z])[\.?!](?:\s|[\"'’”])")
        text = text_parser.__protect_abbreviations(text)
        text = text_parser.__restore_abbreviations(text)
        return re.split(sentence_delimiters, text)

    ### Private methods ###

    # Removes periods from common title abbreviations to prevent parsing as a sentence
    @staticmethod
    def __protect_abbreviations(text: str) -> str:
        common_titles = re.compile(r"(Mrs|Mr|Ms|Dr|Jr|Sr)(\.)")
        return re.sub(common_titles, r"\g<1>", text)

    # Adds periods to common title abbreviations that are missing them
    @staticmethod
    def __restore_abbreviations(text: str) -> str:
        common_titles_no_period = re.compile(r"(Mrs|Mr|Ms|Dr|Jr|Sr)(\s)")
        return re.sub(common_titles_no_period, r"\g<1>. ", text)
