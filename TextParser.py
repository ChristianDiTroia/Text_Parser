import pdfplumber, re, random, os, math
import docx as wd
import concurrent.futures as cf
from enum import StrEnum
from io import BytesIO


class TextParser:

    # File types
    class __ACCEPTED_FILE_TYPES(StrEnum):
        PDF = "pdf"
        DOCX = "docx"
        TXT = "txt"

    def __init__(self, file_path: str):
        file_extension = file_path.split(r".")[-1].lower()
        accepted_file_types = [enum.value for enum in self.__ACCEPTED_FILE_TYPES]
        if not file_extension in accepted_file_types:
            raise ValueError(
                f"Unsupported file type: {file_extension}.\n"
                f"Accepted types are: {accepted_file_types}"
            )

        self.__file_type = file_extension
        self.__text_bytes = self.read_file(file_path)
        self.__lines = []
        self.__next_line = 0
        self.__sentences = []
        self.__next_sentence = 0

    def parse_text(
        self,
        start_page: int = 0,
        end_page: int = None,
    ) -> tuple[list[str], list[str]]:
        """Parse and store each sentence and line from the text"""

        text = ""
        if self.__file_type == self.__ACCEPTED_FILE_TYPES.PDF:
            if not end_page:
                with pdfplumber.open(self.__text_bytes) as pdf:
                    end_page = len(pdf.pages)
            if not start_page:
                start_page = 1

            workers = os.cpu_count() or 4
            pages_per_worker = math.ceil((end_page - start_page) / workers)
            futures = []
            with cf.ProcessPoolExecutor(max_workers=workers) as executor:
                for i in range(workers):
                    worker_start = start_page + (pages_per_worker * i)
                    worker_end = min(worker_start + pages_per_worker, end_page)
                    futures.append(
                        executor.submit(
                            self.extract_pdf_text,
                            self.__text_bytes,
                            worker_start,
                            worker_end,
                        )
                    )
            for future in futures:
                text += future.result()
        elif self.__file_type == self.__ACCEPTED_FILE_TYPES.DOCX:
            text = self.extract_docx_text(self.__text_bytes)
        else:  # txt files only contain across a single page
            text = self.__text_bytes.getvalue().decode(
                encoding="utf-8", errors="replace"
            )

        self.__lines = self.parse_lines(text)
        self.__next_line = 0
        self.__sentences = self.parse_sentences(text)
        self.__next_sentence = 0

    def get_next_line(self) -> str:
        return self.get_next_lines(1)[0]

    def get_next_lines(self, num_lines: int) -> list[str]:
        lines = self.get_lines(self.__next_line, self.__next_line + num_lines)
        self.__next_line = self.__next_line + num_lines
        if self.__next_line >= self.num_lines():
            self.__next_line = 0

        lines_remaining = num_lines - len(lines)
        if lines_remaining > 0:
            lines.extend(self.get_next_lines(lines_remaining))

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
        self.__next_sentence = self.__next_sentence + num_sentences
        if self.__next_sentence >= self.num_sentences():
            self.__next_sentence = 0

        sentences_remaining = num_sentences - len(sentences)
        if sentences_remaining > 0:
            sentences.extend(self.get_next_lines(sentences_remaining))

        return sentences

    def get_sentences(self, start: int, end: int = None):
        return self.__sentences[start:end]

    def num_sentences(self) -> int:
        return len(self.__sentences)

    def shuffle_lines(self, seed: int | float | str | bytes | bytearray | None = None):
        random.seed(seed)
        random.shuffle(self.__lines)

    def shuffle_sentences(
        self, seed: int | float | str | bytes | bytearray | None = None
    ):
        random.seed(seed)
        random.shuffle(self.__sentences)

    ### static variables ###

    # Regex patterns
    __hyphenated_word = re.compile(r"(-|–|—)\n(\w*)(\W)?")
    __newline = re.compile(r"\n")
    __sentence_delimiters = re.compile(r"(?<![\.A-Z])([\.?!][\s\"'’”])")
    __common_titles = re.compile(r"(Mrs|Mr|Ms|Dr|Jr|Sr)(\.)")
    __common_titles_no_period = re.compile(r"(Mrs|Mr|Ms|Dr|Jr|Sr)(\s)")

    ### static methods ###

    @staticmethod
    def read_file(path: str) -> BytesIO:
        with open(path, "rb") as file:
            bytes = file.read()
        return BytesIO(bytes)

    @staticmethod
    def extract_docx_text(
        docx: str | BytesIO,
    ) -> str:
        extracted_text = ""

        doc = wd.Document(docx)
        for paragraph in doc.paragraphs:
            extracted_text += paragraph.text + "\n"

        return extracted_text

    @staticmethod
    def extract_pdf_text(
        pdf: str | BytesIO,
        start_page: int,
        end_page: int,
        top_crop: int = 50,
        bottom_crop: int = 75,
    ) -> str:
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
        return re.sub(TextParser.__hyphenated_word, r"\g<2>\n", text)

    @staticmethod
    def parse_lines(text: str) -> list[str]:
        text = TextParser.concat_hyphenated_words(text)
        lines = []
        for line in re.split(TextParser.__newline, text):
            if line.strip():  # remove blank lines
                lines.append(line)
        return lines

    @staticmethod
    def parse_sentences(text: str) -> list[str]:
        text = TextParser._protect_abbreviations(text)
        split_sentences = re.split(
            TextParser.__sentence_delimiters, text
        )  # returns [sentence, delimiter, sentence, delimiter, ...]
        sentences = []
        # Append each delimiter to reform the original sentences
        for i in range(len(split_sentences)):
            if i == len(split_sentences) - 1:
                sentences.append(split_sentences[i])
            elif i % 2 == 0:  # Sentences are at even indices, delimiters at odd
                sentences.append(split_sentences[i] + split_sentences[i + 1].strip())
        map(lambda s: TextParser._restore_abbreviations(s), sentences)
        return sentences

    ### Private methods ###

    # Removes periods from common title abbreviations to prevent parsing as a sentence
    @staticmethod
    def _protect_abbreviations(text: str) -> str:
        return re.sub(TextParser.__common_titles, r"\g<1>", text)

    # Adds periods to common title abbreviations that are missing them
    @staticmethod
    def _restore_abbreviations(text: str) -> str:
        return re.sub(TextParser.__common_titles_no_period, r"\g<1>. ", text)
