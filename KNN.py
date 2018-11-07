# random splits?

#nan feilds do I mean or median or runn KNN on those feilds (used them as a test set)
#or just ignore those nans 

#add to report
#   We chose to give NAN vaules its own category.

import pandas as pd
import numpy as np
import time

#add fold points
def addFoldPoints(data, amountOfCuts):
    rows, columns = data.shape
    data[str(columns)] = ""
    segment = np.floor(np.size(data,0)/amountOfCuts)
    foldPoint = 0
    count = segment

    for i in range(0,np.size(data,0)):
        if(i<=count):
            data.iloc[i,columns] = foldPoint
            if(i == count):
                count = count + segment
                foldPoint += 1
    return data

#remove spaces and lowercase data
def cleanDataFrame(data):
    #iterate over cols
    for col in data:
        #check type of col is string
        if(type(data[col][0]) == str):
            #remove spaces
            data[col] = data[col].str.strip()
            #make all lowercase
            data[col] = data[col].str.lower()
    return data

def stringToInt(data):
    for col in data:
        unique = []
        uniqueDict = {}
        if(type(data[col][0]) == str):
            for row in range(0, len(data[col])):
                if data[col][row] not in unique:
                    unique.append(data[col][row])
                    uniqueDict[data[col][row]] = len(uniqueDict)
            data[col] = data[col].map(uniqueDict)     
    print("stringToInt complete")
    return data


#need to ignore lable col and fold column some how
def minMaxNormalisation(data):
    for col in data:
        min = data[col].min()
        max = data[col].max()
        print(col + "/ 14")
        for row in range(0, data[col].size):
            value = data[col].iloc[row]
            minMax = (value - min) / (max - min)
            data[col].iloc[row] = minMax
    print("finished normalisation")
    data.to_csv("min-max.csv")
    return data.copy()


def createDistances(data):
    rows, columns = data.shape
    data[str(columns)] = ""
    #compare every row to every row as tuples
    for i in data.itertuples():
        distanceMatrix = np.zeros(shape = (rows,2))
        for j in data.itertuples():
            distArray = np.zeros(len(i)-2)
            #check the index of the rows is not the same
            if i[0] != j[0]:
                for x in range(1,len(i)-2):
                    #difference between two feilds squared
                    distArray[x] = (i[x]-j[x])**2
            #sum all the distances then square root
            distanceSum = distArray.sum()
            distSqrt = np.sqrt(distanceSum)
            #distance array of index and distance from feild
            distance = [j[0], distSqrt]
            distanceMatrix[j[0]] = distance
        #set distance to self as negative number
        distanceMatrix[i[0]] = [i[0], -1] 
        #sort closest distance is nearest
        distanceMatrix = distanceMatrix[distanceMatrix[:, 1].argsort()]
        #store distacnce matrix in df
        data.iloc[i[0], columns] = [distanceMatrix]
        
    return data

        
        

def main():
    #import csv adult data set
    col_names = ['age', 'work_class', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

    data = pd.read_csv("adult.data.small.csv",names=col_names,header=None)
    data = cleanDataFrame(data)
    data = stringToInt(data)
    data = minMaxNormalisation(data)
    #returns 0 for earning over 50k
    #and 1 for under 50k
    data = createDistances(data)
#    data = addFoldPoints(data, 5)
    data.to_csv("distance.csv")


    return data

datatest = pd.read_csv('adult.data.messing.csv')
print("hello, I have started at")
startTime = time.asctime( time.localtime(time.time()) )
print(startTime)
print("----------")
data = main()
finishTime = time.asctime( time.localtime(time.time()) )
print("-----------")
print("Started at: " + startTime)
print("Finished at: " + finishTime)
print("im done")
    
        
        