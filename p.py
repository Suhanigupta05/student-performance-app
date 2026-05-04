import pandas as pd


""" Created this dict as we want to give ml model data to understand as it learns through examples."""
data = {
    "study_hours": [1,2,3,4,5,6,7,8,9,10],
    "attendance": [50,55,60,65,70,75,80,85,90,95],
    "marks": [35,40,45,50,55,65,70,75,85,95]
}

df = pd.DataFrame(data) # a table structure in pandas to store data like EXcEL SHEET inside python
df.to_csv("data.csv",index=False) # saves datasets to file so model can read it and learn from it. index=False means we dont want to save the index column 
#of the dataframe to the csv file.


