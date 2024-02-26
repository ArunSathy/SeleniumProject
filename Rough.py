import pandas as pd
import openpyxl
from tkinter import filedialog
import os
#
#
# base_file=filedialog.askopenfilename(title='Select the Input file',filetypes=(("Excel Files","*.xlsx"),("CSV Files","*.csc"),("All Files","*.*")))
# excel_data=pd.read_excel(base_file,sheet_name='Translate')
#
# for i in excel_data.index:
#     entry=excel_data.loc[0]
#     print(entry)

# for i in excel_data.index:
#     data={'Translated Text':[i]}
#     df=pd.DataFrame(data)
#     output_file=filedialog.askopenfilename(title='Select the Input file',filetypes=(("Excel Files","*.xlsx"),("CSV Files","*.csc"),("All Files","*.*")))
#     with pd.ExcelWriter(output_file) as write:
#         df.to_excel(write,sheet_name='Translated text')


# x=[1,2,3,4,5,6]
# for i in x:
input_file=filedialog.askopenfilename(title='Select the Input file',filetypes=(("Excel Files","*.xlsx"),("CSV Files","*.csc"),("All Files","*.*")))
wb=openpyxl.load_workbook(input_file)
ws=wb['Translate']

# print(ws['A2'].value)

