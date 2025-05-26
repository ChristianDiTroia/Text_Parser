import pdfplumber
from re import compile
from sys import stderr
from concurrent.futures import ProcessPoolExecutor as PPE
from functools import partial

FILENAME = "./the-great-gatsby.pdf"


# return a list of all lines that contain a match of the regular expression
def extract(filename, page):
    result = []
    try:
        with pdfplumber.open(filename) as pdf:
            for line in pdf.pages[page].extract_text().split("\n"):
                result.append(line)
    except Exception as e:
        print(e, file=stderr)
    return result


def main(filename):
    lines = []
    with PPE() as ppe, pdfplumber.open(filename) as pdf:
        for future in ppe.map(partial(extract, filename), range(len(pdf.pages))):
            lines.extend(future)
    return lines


if __name__ == "__main__":
    text = main(FILENAME)
    print(len(text))

### not the best solution - saves about 50% time, however, is running concurrently and not in parallel
