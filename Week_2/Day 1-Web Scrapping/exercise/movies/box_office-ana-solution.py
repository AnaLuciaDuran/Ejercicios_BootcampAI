import pandas as pd
import numpy as np

data = pd.read_csv("movies.csv", header=None)

df = pd.DataFrame (data)
df.head()

#Quiero acomodarlas por ingresos
#df.sort_values(by=[])
def most_succesfull (number_of_movies, max_year, df):

    df =df[df[0] < max_year]
    df = df.sort_values(by=[2],ascending = False)
    return df.iloc[ :number_of_movies]

most_succesfull(3,1975,df)

#Filtering out the movies before given year
#movies_prior_year = df[df[1] < max_year]

#sorting by earnings, in descending order:



#print (df)
#print(data)

"""import csv
import date
# import debugger if needed

#def most_successful(number_of_movies, max_year, file_path):

  # TODO: return the number most successful movies before max_year


#execution

#most_successful(3, 1975, 'File_location_path')"""

