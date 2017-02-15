

# ## Author: Omoju Miller
# ### Item Category Hierachy Classification
# item name match script

# Import libraries
from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import pickle
import sys


from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer



file_in = sys.argv[1]
file_out = sys.argv[2]
print ("Reading in file: {}\n".format(file_in))

#### Load Data
df_ = pd.read_pickle(str(file_in))

n = len(df_)
print ("Read in {0} records".format(n))



# ### Engineered Features
# - Do any word correspond to a thing in the list
#     - dried sundried cranberry -> [Food, Produce, Fruits, Cranberries]
#     - mushroom portabella -> 	[Food, Produce, Mushrooms]
#     
# Words in `item_name` appears in the tree branch where it belongs.
# - Weight occurence by the frequency in the branch


# In[73]:


# Item name appears matches node name in tree branch score
# text to lower
# split text
# stem and compare


def clean_token(item_name):
    # tokenizer, stops, and stemmer
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))  # can add more stop words to this set
    stemmer = SnowballStemmer('english')

    cleaned_tokens = []
    tokens = tokenizer.tokenize(item_name.lower())
    for token in tokens:
        if token not in stop_words:
            if len(token) > 0 and len(token) < 20: # removes non words
                if not token[0].isdigit() and not token[-1].isdigit(): # removes numbers
                    stemmed_tokens = stemmer.stem(token)
                    cleaned_tokens.append(stemmed_tokens)
                    
    return cleaned_tokens


print("Generate item name match score")

## Postpone this for now. set n to 2
## for record_num in range (n):
for record_num in range (n):
    
    score = 0
    
    try:
        cleaned_tokens = clean_token(df_.item_name[record_num])
    except:
        print("Code broke processing this record:{0}".format(record_num))
        cleaned_tokens = ''

    #print(cleaned_tokens)

    for i in range(6):
        for j in range(len(cleaned_tokens)):
            col_name = 'mapped_level_'+str(i)
            try:
              cmpr_token = clean_token(df_.ix[record_num, col_name])
              for k in range(len(cmpr_token)):
                if cleaned_tokens[j] == cmpr_token[k]:
                    #print(cmpr_token[k])
                    score += 1
            except:
              continue
    df_.ix[record_num, 'item_name_match'] = score
    
    
print("Write file out to disk")

df_.to_pickle(str(file_out))





