import pandas as pd

#filepaths and col paths to compare
excelsheet1 = file_path
excelsheet1col = "colname"
compareisonxlsheet = file_path
comparesheetcol = "colname"
resultsexl = file_path

#read in data
excel_data=pd.read_excel(r"excelsheet1")
compare_data=pd.read_excel(r"compareisonxlsheet")

#convert to str bc messy data (ex: 12345, 12345F, DFGET12345, 12345 67895, 3456H, 1234567)
compare_col = compare_data[comparesheetcol].astype(str)
excel_data[excelsheet1col]=excel_data[excelsheet1col].astype(str)

#iterate through a for loop and save matches on the specified row value (in this case product SKU) to a dictionary -> excel spreadsheet)
match_status = []
for index, row in excel_data.iterrows():
    for product_sku in row[excelsheet1col].split():
        matched = "No Match"
        match_check = {'SKU': sku_value, "AssetID": row['<ID>'], "Match Status":matched}
        for x in compare_col:
            if x in sku_value:
                matched = "Match"
                match_check["Match Status"]=matched
        match_status.append(match_check)
match_statusdf=pd.DataFrame(match_status)
with pd.ExcelWriter(r'resultsexl',
                    mode='a') as writer:  
    match_statusdf.to_excel(writer, sheet_name='Sheet2')
