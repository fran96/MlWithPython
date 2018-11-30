# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 23:11:26 2018

@author: Fran
"""

import pandas as pd
wine = pd.read_csv('winedata.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])

wine.head()
wine.describe().transpose()
