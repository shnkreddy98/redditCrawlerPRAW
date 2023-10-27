import os
import pandas as pd

file_names = os.listdir("data")

df = pd.DataFrame()
count = 0

for file in file_names:
	print(f"concating file {count} of 750")
	temp_df = pd.read_csv("data/"+file, encoding='latin-1')
	df = pd.concat([df, temp_df], axis = 0)
	count += 1

df.to_csv("merged_data.csv")
