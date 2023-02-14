# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:35:37 2023

@author: Elkin Gutierrez
"""

import requests
import pydataxm
import pandas as pd
import json


url = 'http://servapibi.xm.com.co/hourly'
myobj = {"MetricId": "Gene",
         "StartDate":"2022-09-01",
         "EndDate":"2022-09-30",
         "Entity": "Recurso"}

x = requests.post(url, json = myobj)
data = x.text


result = json.loads(data)
result = pd.json_normalize(result['Items'])


df = pd.DataFrame(result)

df.head()
