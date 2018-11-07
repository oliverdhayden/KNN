# random splits?

#nan feilds do I mean or median or runn KNN on those feilds (used them as a test set)
#or just ignore those nans 

import pandas as pd
import numpy as np
import time



#writing to col
#data.iloc[0,15] = 0

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
            #change strings to workable ints
#            unique = []
#            for i in range(0, data[col].size):
#                if data[col][i] not in unique:
#                    unique.append(data[col][i])
#                data.iloc[1][1] = unique.index(data[col][i])
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
#                    print(column[i])
#                data[col][row] = unique.index(data[col][row])
#            uniqueDict = dict(list(enumerate(unique)))
#            print(uniqueDict)
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
#            print(str(row) + "/" + str(data[col].size))
            value = data[col].iloc[row]
            minMax = (value - min) / (max - min)
            data[col].iloc[row] = minMax
    print("finished normalisation")
    data.to_csv("min-max.csv")
    return data.copy()

#this one works
#def createDistances(data):
#    rows, columns = data.shape
#    data[str(columns)] = ""
#    #compare every row to every row as tuples
#    for i in data.itertuples():
##        print(i)
#        distanceMatrix = np.zeros(shape = (rows,2))
#        for j in data.itertuples():
#            #check the index of the rows is not the same
#            distArray = np.zeros(len(i)-2)
#            if i[0] != j[0]:
#                for x in range(1,len(i)-2):
##                    print(i[x])
#                    #difference between two feilds squared
#                    distArray[x] = (i[x]-j[x])**2
#                #sum all the distances then square root
#                distanceSum = distArray.sum()
##                print(distanceSum)
#                distSqrt = np.sqrt(distanceSum)
##                print(distSqrt)
#                #array of index and distance from feild
#                distance = [j[0], distSqrt]
#                distanceMatrix[j[0]] = distance
#                
#        print("------------")
#        print("columns " + str(columns))
#        print("index " + str(i[0]) )
#        print(data.shape)
#        print(str(type(distanceMatrix)))
#        print(distanceMatrix)
#        data.iloc[i[0], columns] = [distanceMatrix]
#    return data

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
                
#        print("------------")
#        print("columns " + str(columns))
#        print("index " + str(i[0]) )
#        print(data.shape)
#        print(str(type(distanceMatrix)))
        
#        print(i[0])
        #set distance to self as negative number
        distanceMatrix[i[0]] = [i[0], -1] 
#        print(distanceMatrix)
#        print("----------")
        #sort closest distance is nearest
        #distanceMatrix.sort(0)
        distanceMatrix = distanceMatrix[distanceMatrix[:, 1].argsort()]
#        print(distanceMatrix)
#        print(str(type(distanceMatrix)))
        #store distacnce matrix in df
        data.iloc[i[0], columns] = [distanceMatrix]
        
    return data

        
        

def main():
    #import csv adult data set
#    col_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    col_names = ['age', 'work_class', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

    data = pd.read_csv("dataSet/adult.data.csv",names=col_names,header=None)
    data = cleanDataFrame(data)
    data = stringToInt(data)
    data = minMaxNormalisation(data)
    #returns 0 for earning over 50k
    #and 1 for under 50k
    data = createDistances(data)
    data = addFoldPoints(data, 5)
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
#dataTest = normaliseCol("0", data)

#def normaliseGender(data):
            
#data["10"]= data["10"].str.strip()
#data[10]= data[10].str.strip()

#data = cleanDataFrame(data)


#print(data["10"][0])
#print(data['10'][0] == "Male" )
#print(type(row["10"][0]))
#data['2'] = data['2'].map({""})
#data['10'] = data['10'].map({"Female": 0, "Male": 1})


#maxAge = findMax("1", data)
#data = normaliseCol("1", data, maxAge)

#for index, row in data.iterrows():
#    print(type(row["10"]))
#    break


#print(maxAge)
print("im done")
# for i in range(0,np.size(testSet,0))
#   for j in range(0,np.size(trainSet,0))
        # caculate distrance
    # sort output
    # cut index<K
        
#for i in range(0, amountOfCuts):
#    data.iloc[range((i)*segment,(i+1)*segment),15] = i
    
        
        