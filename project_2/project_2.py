# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 13:22:24 2021

@author: Minhazur.Rahman
"""

import  geopandas as gpd

county_df = gpd.read_file('cb_2018_us_county_500k/cb_2018_us_county_500k.shp')
cities_df = gpd.read_file('cities/citiesx010g.shp')