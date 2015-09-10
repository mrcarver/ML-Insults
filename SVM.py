###################################################################################################################
##                                                                                                               ##
##  Main function for classifying comments as insulting or non-insulting to users within an internet forum       ##
##  setting.  This code is meant to solve the Insult Detection Kaggle competition, which can be found at         ##
##  https://www.kaggle.com/c/detecting-insults-in-social-commentary.  Currently, this code contains the          ##
##  following methods for categorization:                                                                        ##
##           X Naive Bayes Rule                                                                                  ##
##                                                                                                               ##
###################################################################################################################

import Fcts
import numpy as np

#FeatureSpace=Fcts.getFeatureSpace("train.csv",20)
#print (len(FeatureSpace))

TestFeatureSpace=["test","document","see","fuck","hello","two","one","function"]
print (len(TestFeatureSpace))
document="hello this is a test document to see if the feature vector function is working properly test hello"

FeatureVector=Fcts.getFeatureVector(document,TestFeatureSpace,False)

print (len(FeatureVector))

for i in range(0,len(FeatureVector)):
    print (FeatureVector[i])


