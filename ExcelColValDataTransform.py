#IMPORTS
import pandas as pd
attribute_data=pd.read_excel(r"file_name")
col_to_update = "col_name"
export_file = r"output_filename"

#Check data spread
attribute_data.shape
attribute_data[100:120]
#set updates values for intended values, otherwise keep original value
def update_value(row, col_name):
    value = row[col_name]
    exposure_mapping = {
        'anti-fog': "Anti-Fog",
        'fog-free with foam strip': "Fog-Free With Foam Strip",
        'foam band': "Foam Band",
        'no': "No Fog Resistance",
        'yes':'Fog Resistance'
    }
    for key in exposure_mapping:
        if key in value.lower():
            return exposure_mapping[key]
    return value

#Set col to str type 
attribute_data[col_to_update] = attribute_data[col_to_update].astype(str)
attribute_data[col_to_update] = attribute_data.apply(update_value, args=(col_to_update,),axis=1)

#OUTPUT DATA CHECKS
attribute_data.shape
counts = attribute_data[col_to_update].value_counts()
counts

#write results to Excel
with pd.ExcelWriter(export_file,
                    mode='a') as writer:  
    attribute_data.to_excel(writer, sheet_name='Sheet4')
