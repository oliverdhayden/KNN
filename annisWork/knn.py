# Data Mining Coursework 1 ==============================
# To build a kNN model on the training set & evaluate performance measured:
# confusion matrix, precision, sensitivity (recall) & specivity <=50k

import pandas as pd
import numpy as np

# 1 Handle Data ==============================

# Specifying column names
col_names = ['age', 'work_class', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

# Import dataset
data = pd.read_csv("adult.data.csv", 
                   names=col_names,
                   header=None)

# strip white space    
data['sex'].str.strip()

data['sex'].replace(['Female','Male'],[0,1],inplace=True)
    

# Label data
label = data.iloc[:,-2].values


# Normalise Data
# (x-min(x))/(max(x)-min(x))

normalized_data = (data['age']-data['age'].min())/(data['age'].max()-data['age'].min())

data['sex'] = data['sex'].map({" Female": 0, " Male": 1})

normalized_data2 = (data['sex']-data['sex'].min())/(data['sex'].max()-data['sex'].min())



# Split data

data["fold"] = ""
amountOfCuts = 5
segment = np.floor((np.size(data,0))/amountOfCuts)



data.iloc[0,15] = 0

# for i in range(0,data.size(data,0)):
  #  df = pd.DataFrame(df[i]), columns=['newCol'])
    

# 2 Calculate Similarity ==============================



# 3 Locate Neighbour ==============================



# 4 Prediction ==============================




# 5 Accuracy ==============================



# Export 2 cols showing each value of k and accuracy of 5CV for that k (display best K & accuracy)
# data.to_csv('grid.results.txt')