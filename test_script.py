from helper_functions.add_list import add_list
import pandas as pd


df = pd.DataFrame({"a":[1,2,3,4]})
series = pd.Series([5,6,7,8])
name = "b"


new_df = add_list(df, series, name)
print(new_df)





