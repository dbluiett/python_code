# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import random
import sys
import pandas as pd
import numpy as np

# test dictionary of dictionaries similar to json file
swe_dict = {"mem111":"Desi","mem112":"Laura"}
test_dict = dict({"SWE":swe_dict,"NDNYC":{"mem111":"Desi","mem113":"Megan"}})
test_dict.update({"Chambers":{"mem112":"Jacob","mem113":"Megan"}})
this_member = {"connections":{"mem111":"Desi","mem112":"Jacob","mem113":"Megan"}}

def add_attribute (category, attribute, name):
    attribute_list = category.keys()
    if attribute in attribute_list:
        category[attribute].update(name)
    else:
        category.update({attribute:name})

def category_list (category):
    my_dict={}
    for key in category.keys():
        count = len(category[key])
        my_dict.update({key:count})
    return my_dict

def get_group_info (category, attribute, member):
    if len(member["connections"])<len(category[attribute]):
        small=member["connections"]
        large = category[attribute]
    else:
        small= category[attribute]
        large= member["connections"]
    in_group = []
    for friend in small.keys():
        if friend in large.keys():
            in_group.append(large[friend])
    return print("SubCategory: {} /n Total Members: {} /n Connections: {}".format(attribute, len(in_group), in_group))

""" need to figure out how to print the name of a dictionary instead of the 
full text
"""
 
        



