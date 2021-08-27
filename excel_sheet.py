import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

cols = [0]

FileReader = pd.read_excel('/Input Files/input.xlsx', usecols = cols)

case_name = []

names = []

for i in range(len(FileReader)):
    temp_name = []
    temp_name.append(FileReader.iloc[i])
    txt = temp_name[0]
    txt = txt.to_string()
    splited = txt.split()
    name = splited[1]+' '+splited[2]+' '+splited[3]
    case_name.append(name)

for i in range(len(FileReader)):
    temp_name = []
    temp_name.append(FileReader.iloc[i])
    txt = temp_name[0]
    txt = txt.to_string()
    splited = txt.split()
    name = splited[1]+' '+splited[2]
    names.append(name)
    
df = pd.DataFrame({'CASE_NAME': case_name,'Clients': names})
writer = ExcelWriter('/Input Files/output.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()
FileReader2 = pd.read_excel('/Input Files/output.xlsx')
print(FileReader2)