#IMPORTS
import pandas as pd
df=pd.read_excel(r"importfile")
check_df=pd.read_excel(r"importfile")
export_file = r"exportfile"

#Set References
obj_type ='obj_type'
obj_id = 'ID'
parent_id = 'Parent ID'
add_img = 'Image ID'

#Convert to Str
df[add_img]=df[add_img].astype(str)
df[obj_type]=df[obj_type].astype(str)

#Split multivalues on ';'
df[add_img]=df[add_img].str.split(';')
df[obj_type]=df[obj_type].str.split(';')

#Pivot Values on ImgID, Obj_Id
df = df.explode([add_img,obj_type])

#Create hashmap
hashmap = df.groupby([add_img, parent_id]).agg({obj_id:lambda x: list(x)})

#Output to Excel
with pd.ExcelWriter(export_file, mode='a') as writer:  hashmap.to_excel(writer, sheet_name='Hashmap2')
