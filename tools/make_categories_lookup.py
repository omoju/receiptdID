# coding: utf-8

# ## PlateIQ 
# ## Author: Omoju Miller
# ### Item Category Hierachy Classification
# Make Categories Look Up Table

import pickle
import numpy as np
import pandas as pd
import sys


file_in = sys.argv[1]

data = pd.read_pickle(str(file_in))


## Make Category Lookup Table

data_category_lookup = data[['category_0', 'mapped_category_0']]

df_new = data[['category_1', 'mapped_category_1']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)


df_new = data[['category_2', 'mapped_category_2']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)


df_new = data[['category_3', 'mapped_category_3']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)

df_new = data[['category_4', 'mapped_category_4']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)

df_new = data[['category_5', 'mapped_category_5']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)

df_new = data[['category_6', 'mapped_category_6']]
df_new.columns = ['category_0', 'mapped_category_0']
data_category_lookup = data_category_lookup.append(df_new, ignore_index=True)

data_category_lookup.columns = ['category_id', 'category_name']

data_category_lookup = data_category_lookup.drop_duplicates()


print("Writing category look up table out to disk")

data_category_lookup.to_pickle('data/data_category_lookup.dat')