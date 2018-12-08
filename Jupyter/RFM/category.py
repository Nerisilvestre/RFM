#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def classifier(row):
    if rfm2['r_cat'].between(4,5) & rfm2['fm_cat'].between(4,5):
        return 'Champion'
    else:
        return 'nada'
    

