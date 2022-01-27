from tkinter import filedialog as fd
from lxml import etree
from googletrans import Translator
from pprint import pprint


__author__ = "Jaun van Heerden"

import re

REGEX = re.compile(r'((?:[a-z]|[A-Z])(?:[a-z]+|[A-Z]+))', re.UNICODE)
REGEX_QUOTES = re.compile(r'(?<==")[^\"\d]{2,}(?=\")')


def detect_and_translate(translator, text, lang):
    detect = translator.detect(text)
    if detect.lang != lang:
        translated = translator.translate(text, src='de', dest='en')
        return translated
    return


# TODO find replace largest to smallest so that no substrings are replaced first

def main():
    # path = fd.askdirectory()

    translator = Translator()

    print('Select <xml> file to translate EN-DE...')

    file = fd.askopenfilename()

    # Quoted items
    with open(file, 'r') as f:

        quoted = list(set(REGEX_QUOTES.findall(f.read())))

        result = translator.translate('\n'.join(quoted), src='de').text.split('\n')

        result_zipped = [i for i in list(zip(quoted, result)) if i[0].lower() != i[-1].replace(' ', '').lower()]

        pprint(result_zipped)


    # XML text
    root = etree.parse(file)

    texts = list(set([i.text for i in root.iter()]))

    print(texts)



    for elem in root.iter():
        if elem.text is not None:
            for find in REGEX.findall(elem.text):
                if result := detect_and_translate(translator, find, 'en'):
                    print(find, f'\t|\t[{result.text}]')



if __name__ == "__main__":

    main()

    input('\nSend <ENTER> to exit...')