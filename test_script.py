from help_func.helper_functions import add_list
import pandas as pd


df = pd.DataFrame([1,2,3,4])
series = pd.Series([5,6,7,8])
name = 'new column'

#y = (df, series,name)

print(add_list(df, series, name))





