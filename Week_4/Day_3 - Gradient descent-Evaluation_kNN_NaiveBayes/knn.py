import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

print(2+2)
"""
1-Create a new file named knn.py (you might want to use PyCharm).
2-Inside the file create a class named KNN that can take diferent
parameters as input (e.g k, distance, etc.). Create the init
function to initialise the instances of your class;
3-Create a fit function that takes as input the X 2-D array of training
data and y 1-D array of training labels and processes this data to
train the model;
4-Create a predict function that takes as input the X 2-D array of
testing data and output the y 1-D array of predicted labels for the
testing data.
Note: you can create any other auxiliary function that you might need
inside your function. Remember the importance of the self parameter
when working with a class."""

# KNN its going to be the grades of students
class KNN:
    st_name= ""
    math = 100.0
    spanish = 100.0
    science = 100.0
    def description(self):
        desc_str = "%s has a %s in math %s in spanish and %s in science." % (self.st_name, self.math, self.spanish,self.science)
        return desc_str

# now the students
student1 = KNN()
student1.st_name = "Rosa"
student1.math = 89
student1.spanish = 70
student1.science = 93

student2 = KNN()
student2.st_name = "Margarita"
student2.math = 95
student2.spanish = 100
student2.science = 92

student3 = KNN()
student3.st_name = "Clavel"
student3.math = 70
student3.spanish = 65
student3.science = 82

# test code
print(student1.description())
print(student2.description())
print(student3.description())