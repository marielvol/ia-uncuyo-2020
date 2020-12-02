#Import the required libraries
import numpy as np
import pandas as pd
import pprint
from numpy import log2 as log
#eps is the smallest representable number
eps = np.finfo(float).eps

#Find the entropy of the whole dataset
def find_entropy(df):
    Class = df.keys()[-1]
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy
  
#Find the entropy of each attribute
def find_entropy_attribute(df,attribute):
  Class = df.keys()[-1]
  target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
  variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cool' in Temp)
  entropy2 = 0
  for variable in variables:
      entropy = 0
      for target_variable in target_variables:
          num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
          den = len(df[attribute][df[attribute]==variable])
          fraction = num/(den+eps)
          entropy += -fraction*log(fraction+eps)
      fraction2 = den/len(df)
      entropy2 += -fraction2*entropy
  return abs(entropy2)

#Find the attribute with the max information gain
def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        #Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]

def get_subtable(df, node,value):
  return df[df[node] == value].reset_index(drop=True)

#Build the decision tree
def buildTree(df,tree=None): 
    Class = df.keys()[-1]
    #Get attribute with maximum information gain
    node = find_winner(df)
    #Get distinct value of that attribute e.g Humidity is node and Normal and High are values
    attValue = np.unique(df[node])
    #Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    #We make loop to construct a tree by calling this function recursively.
    #In this we check if the subset is pure and stops if it is pure.
    for value in attValue:   
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable['play'],return_counts=True)                        
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]
        else:
          tree[node][value] = buildTree(subtable) #Calling the function recursively              
    return tree

#Read the dataset
df = pd.read_csv("tennis.csv")
#Print the dataset
print(df)
#Call the function to build the tree
t = buildTree(df)
#Print the result
pprint.pprint(t)