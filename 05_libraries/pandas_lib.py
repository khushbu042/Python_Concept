# Pandas is a Python library.
# Pandas is used to analyze data.
# two main tbings are there first is Series and another one is DataFrame
import pandas as pd


data =[2,4,6,8,10]
print(type(data))
data_series  = pd.Series(data)
print(type(data_series))

# Creating and initializing a nested list
age = [['Aman', 95.5, "Male"], ['Sunny', 65.7, "Female"],
       ['Monty', 85.1, "Male"], ['toni', 75.4, "Male"]]

# Creating a pandas dataframe
df = pd.DataFrame(age, columns=['Name', 'Marks', 'Gender'])

# # Printing dataframe
print(df)
print(age)
