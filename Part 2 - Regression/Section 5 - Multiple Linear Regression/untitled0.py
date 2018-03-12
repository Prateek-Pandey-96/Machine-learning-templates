# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 22:19:42 2017

@author: bhupe
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing data set
dataset=pd.read-csv('50_Startups.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
