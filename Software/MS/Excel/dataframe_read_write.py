import pandas as pd
import tkinter.filedialog as fd

# read excel, apply function, write excel
def read_write(filename: str, func=None):

    df = pd.read_excel(filename)   # read in dataframe

    # run function if given
    if func is not None:
        df = func(df)

    writer = pd.ExcelWriter(filename, engine='openpyxl')   # create writer
    df.to_excel(writer, index=False)   # to excel
    writer.save()   # save

# example function
def example(df):
    return df.T

if __name__ == '__main__':
    # run
    read_write(fd.askopenfilename(), example)
