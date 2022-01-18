from tkinter import filedialog as fd
import codecs
import csv
from pprint import pprint
import pandas as pd


class GalaxyData:

    def __init__(self):

        """fields"""
        self.dataframe_dict = {}
        self.data = {}

        """get file source"""
        print('Select file source...')
        self.filename_source = fd.askopenfilename()

        """x"""
        with codecs.open(self.filename_source, 'rU', 'utf16') as file:
            self.csv_data = csv.reader(file, delimiter=',')
            self.data_raw = [row for row in self.csv_data if row]

        """x"""
        # print('\nDATA\n----\n')
        # pprint(self.data_raw)

        """x"""
        self.group_templates()

        """x"""
        self.to_dataframe_dict()

    def group_templates(self):

        focus_template = None

        for row in self.data_raw:

            if ':TEMPLATE' in row[0]:
                focus_template = row[0].replace(':TEMPLATE=', '')

                print(focus_template)

            if focus_template:

                if focus_template not in self.data:
                    self.data[focus_template] = {'template': None,
                                                 'header': None,
                                                 'data': []}

                if ':TEMPLATE' in row[0]:
                    self.data[focus_template]['template'] = row
                elif ':Tagname' in row[0]:
                    self.data[focus_template]['header'] = row
                else:
                    self.data[focus_template]['data'].append(row[:-1])

    """
    a
    """

    def to_dataframe_dict(self):

        for template, data in self.data.items():
            self.dataframe_dict[template] = pd.DataFrame(data['data'], columns=data['header'])

        pprint(self.dataframe_dict)


def main():
    print('Get file source')
    # gd = GalaxyData()


if __name__ == '__main__':
    main()
