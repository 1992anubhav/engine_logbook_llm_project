# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 15:26:44 2025

@author: H479938--ANUBHAV
"""

import os
import json
from pathlib import Path
import shutil
 
# define paths
base_path = Path("C:/BITS_WILP/SEM4/Dissertation/Dataset/TestData")
metadata_path = base_path.joinpath("RTS_key")
image_path = base_path.joinpath("RTS")
# define metadata list
metadata_list = []
 
# parse metadata
for file_name in metadata_path.glob("*.json"):
  with open(file_name, "r") as json_file:
    # load json file
    data = json.load(json_file)
    # create "text" column with json string
    text = json.dumps(data)
    # add to metadata list if image exists
    if image_path.joinpath(f"{file_name.stem}.jpg").is_file():
      metadata_list.append({"text":text,"file_name":f"{file_name.stem}.jpg"})
      # delete json file
 
# write jsonline file
with open(image_path.joinpath('metadata.jsonl'), 'w') as outfile:
    for entry in metadata_list:
        json.dump(entry, outfile)
        outfile.write('\n')
 
# remove old meta data
#shutil.rmtree(metadata_path)