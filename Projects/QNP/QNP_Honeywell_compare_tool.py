import os
from pprint import pprint
import re


class Abstract:

    def __init__(self, filename):

        self.filename = filename


class Manager:

    def __init__(self):

        self.data_source_files = []

        self.data_reference_files = []

        self.controller_complete = []

        self.controller_incomplete = []




    def run(self):

        # get all files from folder `data_source` - make folder if doesn't exist
        self.data_source_files = self.get_files("data_source")

        #print(self.data_source_files)

        # get all files from folder `data_reference` - make folder if doesn't exist
        self.data_reference_files = self.get_files("data_reference")

        #print(self.data_reference_files)

        self.data_source_eval()
        self.data_source_process()
        self.data_reference_eval()
        self.data_reference_process()


    def data_source_eval(self):
        """x"""
        ...
        # how many pairs
        # get all unique names

        print('\nfinding complete controller files:')

        for controller in [file.split(".", 1)[0] for file in self.data_source_files
                           if file.split(".", 1)[-1].lower() in ['.pth', 'obt']]:

            # check if `.opt` and `.pth` files both there

            if controller + '.obt' in self.data_source_files \
                    and controller + '.pth' in self.data_source_files:

                print(f'\t+ {controller}')

                self.controller_complete.append(controller)

            else:

                self.controller_incomplete.append(controller)

            print(f'\n\t:: found {len(self.controller_complete)} controller' + ['s', ''][len(self.controller_complete) == 1])

            # display incomplete controllers
            if self.controller_incomplete:

                print('incomplete controllers:\n\t' + '\n\t'.join(self.controller_incomplete))

        #

    def data_source_process(self):
        """x"""

        for controller in self.controller_complete:

            obt = Obt(controller + '.obt')
            pth = Pth(controller + '.pth')





    def data_reference_eval(self):
        """x"""
        ...


    def data_reference_process(self):
        """x"""
        ...


    @staticmethod
    def get_files(directory):
        if not os.path.exists(directory):
            os.mkdir(directory)
            print(f'!\tadd data to `{directory}` folder')
            input('\tsend any key to continue...')

        print(f'\nloading in files from `{directory}` folder:')

        # get all files but omit files which start with `~`
        # these are hidden files
        files = [file for file in os.listdir(directory) if not file.startswith('~')]

        print(f'\t:: found {len(files)} file' + ['s', ''][len(files) == 1])

        return files


class DataSource:
    """Data source"""
    def __init__(self, obt_filename, pth_filename):

        self.obt = Obt(obt_filename)

        self.pth = Pth(pth_filename)


class Obt(Abstract):
    """.obt file"""

    def __init__(self, filename):
        super().__init__(filename)

        data = {}


        with open('data_source/' + filename, 'r') as file:
            #data = file.readlines()

            for line in file.readlines():

                #data.append([item for item in line.split(' ') if item])

                line = [item for item in line.split(' ') if item]

                if len(line) > 5:

                    if line[3] not in data:
                        data[line[3]] = {}

                    data[line[3]][line[4]] = line[5]

        pprint(data)

        #print(list(set([len(item) for item in data])))


class Pth(Abstract):
    """.pth file"""

    def __init__(self, filename):
        super().__init__(filename)
        ...

        #data = []

        data = {}

        with open('data_source/' + filename, 'r') as file:
            # data = file.readlines()

            for line in file.readlines():

                line = [item for item in line.split(' ') if item]

                if len(line) == 4:

                    if line[2] not in data:
                        data[line[2]] = {}

                    data[line[2]][line[3]] = line[4]




                #data.append([item for item in line.split(' ') if item])

        # pprint([i for i in data if len(i) == 4])



def main():

    # create a new manager
    manager = Manager()

    # run the manager
    manager.run()


if __name__ == "__main__":
    main()
