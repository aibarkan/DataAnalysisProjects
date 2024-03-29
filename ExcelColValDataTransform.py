#IMPORTS
import pandas as pd
attribute_data=pd.read_excel(r"file_name")
col_to_update = "col_name"
export_file = r"output_filename"
attribute_data.shape

attribute_data[100:120]
def update_value(row, col_name):
    value = row[col_name].lower()
    exposure_mapping = {
        'low to mod': "Low to Moderate Exposure",
        'light to mod': "Low to Moderate Exposure",
        'low to high': "Low to High Exposure",
        "moderate to heavy": "Moderate to High Exposure",
        "moderate to high": "Moderate to High Exposure",
        "heavy" : "High Exposure",
        "high" : "High Exposure",
        'no' : "No Exposure",
        'light': 'Low Exposure',
        'moderate':'Moderate Exposure',
        'yes':'Some Exposure'
    }
    if value == "low":
        return 'Low Exposure'
    for key in exposure_mapping:
        if key in value:
            return exposure_mapping[key]
    return "N/A"
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
