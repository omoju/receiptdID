
# coding: utf-8


# ## Author: Omoju Miller
# ### Item Category Hierachy Classification
# Data Conversion Script

import pickle
import numpy as np
import pandas as pd
import json
import sys


file_in = sys.argv[1]
file_out = sys.argv[2]
print ("Reading in file: {}\n".format(file_in))

#### Load Data

df = pd.read_csv(str(file_in), sep='\t', names=['jsonValue'])
n = len(df)
print ("Read in {0} records".format(n))

# In[37]:

convertJson = lambda x: json.loads(x)


# In[38]:


print ("Convert to json")
df = df.jsonValue.apply(convertJson)




# In[42]:


col_name = ["mapped_category",
            "item_id",
            "price_stddev",
            "primary_unit",
            "price_mean",
            "category",
            "vendor_id",
            "item_name"]
data = pd.DataFrame(index=df.index, columns = col_name)


n = len(data)
cols = col_name
for i in range(n):
    for col in cols:
        data.iloc[i][col] = df.iloc[i][col]


        
print ("Convert to pandas")

# Save dataframes to file

print ("Saving dataframe to disk\n")

data.to_pickle(str(file_out))



