# coding: utf-8

# ## PlateIQ 
# ## Author: Omoju Miller
# ### Item Category Hierachy Classification
# Make Categories Script

import pickle
import numpy as np
import pandas as pd
import sys


file_in = sys.argv[1]
file_out = sys.argv[2]

data = pd.read_pickle(str(file_in))

# drop all rows that are all NaNs

data.dropna(how='all', inplace=True)


def get(row, r):
    '''helper function to retrieve item from list'''
    try:
        return row[r]
    except IndexError:
        return np.nan

def my_remove_list_items(list_of_records):
    for r in list_of_records:
        yield get(r, 0), get(r, 1), get(r, 2), get(r, 3), get(r, 4), get(r, 5), get(r, 6)
  

print("{}: Converting item category taxonomy into individual features".format(str(file_in)))

labels = ["level_"+str(i) for i in range(7)]
mapped_level_labels = ["mapped_level_"+str(i) for i in range(7)]

level_df = pd.DataFrame.from_records(my_remove_list_items(data.category), columns = labels)
df = pd.concat([data, level_df], axis=1)
df_mapped_category = pd.DataFrame.from_records(my_remove_list_items(data.mapped_category), columns = mapped_level_labels)

data[[ u'level_0', u'level_1', u'level_2', u'level_3',
       u'level_4', u'level_5', u'level_6']] = df[[ u'level_0', u'level_1', u'level_2', u'level_3',
       u'level_4', u'level_5', u'level_6']]

data[[u'mapped_level_0', u'mapped_level_1', u'mapped_level_2',
u'mapped_level_3', u'mapped_level_4', u'mapped_level_5', u'mapped_level_6']] = df_mapped_category[[u'mapped_level_0', u'mapped_level_1', u'mapped_level_2', 
u'mapped_level_3', u'mapped_level_4', u'mapped_level_5', u'mapped_level_6']]

print("Saving converted datafile: {0} to disk\n".format(str(file_out)))
data.to_pickle(str(file_out))
