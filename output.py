import pandas as pd


def df_to_excel(df):
    writer = pd.ExcelWriter('/Users/stepanletyagin/Desktop/BMSTU/6_semestr/Coursework/python_code/output_data/output.xlsx')
    df.to_excel(writer)
    writer.save()

    # DF TO CSV
    # yourdf.to_csv('PythonExport.csv', sep=',')
