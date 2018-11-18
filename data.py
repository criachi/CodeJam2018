#!/bin/python3
import numpy as np

import pandas as pd
from sodapy import Socrata
import sys

client = Socrata("data.cityofchicago.org",
                  "pFaJ3zjsqdOjW49ZfhjKGs1V5",
                  username="neil.lupe@gmail.com",
                    password="WLNKvLCnWJQX4ZN")



#date = input().split(" ")

#ftime = date[0] + "T" + time[1]

ftime = input("Enter a date between 2013 and 2017 - YYYY-MM-DD: ")+"T"+ input("Enter a time in 24H format HH:MM:SS: ")
results_list = client.get("wrvz-psew", trip_start_timestamp=ftime)

results_df = pd.DataFrame.from_records(results_list)



'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(results_df)'''

reduced = results_df.loc[:,['trip_total','trip_seconds','pickup_community_area','pickup_centroid_latitude','pickup_centroid_longitude']]#,'trip_start_timestamp','dropoff_centroid_latitude','dropoff_centroid_longitude','trip_end_timestamp']]




reduced = reduced.dropna()





'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(reduced)'''

reduced.to_csv(path_or_buf="{}".format("out.csv"))
