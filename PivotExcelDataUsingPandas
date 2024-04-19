#This code pivots data from two different columns by combining them and pivoting on both together, as well as expands the data from ';' delimited to single value cells

#IMPORTS
import pandas as pd
df=pd.read_excel(r"input_file_path")
check_df=pd.read_excel(r"input_file_path"")
export_file = r"input_file_path"

#Data Exploration
df.shape
df.columns

#Set Ref
obj_type ='obj_type'
obj_id = 'obj_id'
obj2_id = 'obj2_id'

#Split cells based on ';'
df[obj2_id]=df[obj2_id].str.split(';')
df[obj_type]=df[obj_type].str.split(';')

#pivot data based on 2 cols combined
df = df.explode([obj2_id,obj_type])

with pd.ExcelWriter(export_file, mode='a') as writer:  df.to_excel(writer, sheet_name='PivotedData')
