#IMPORTS
import pandas as pd
attribute_data=pd.read_excel(r"fileinput")
export_file = r"fileoutput"

colkeyword_searchcols = "colkeyword" 
col_to_update = "coltoupdate"
keywords = ['key','red']

#Exploratory Analysis
attribute_data.shape
#check the nulls of the col
attribute_data[attribute_data[col_to_update].isnull()]
def search_and_set_keyword(df, keywords, search_cols, col_to_update):
    for i,row in df.iloc[:,search_cols].iterrows():
        for keyword in keywords:
            for val in row:
                val = str(val)
                if keyword in val:
                    df.at[i, col_to_update] = keyword
    return df
  
  def missing_values(df, keywords, col_to_update, colkeyword_searchcols):
    searchcols_index = [x for x, col in enumerate(attribute_data.columns) if colkeyword_searchcols.lower() in col.lower()]
    missing_df = df[df[col_to_update].isnull()]
    df = search_and_set_keyword(missing_df,keywords,searchcols_index, col_to_update)
    #rint('df',df)
    #write results to Excel
    with pd.ExcelWriter(export_file, mode='a') as writer:  df.to_excel(writer, sheet_name='Sheet8')
      
missing_values(attribute_data, keywords, col_to_update, colkeyword_searchcols)
