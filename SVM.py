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
from sklearn import svm
import matplotlib.pyplot as plt


FeatureSpace=Fcts.getFeatureSpace("train.csv",10)
print (len(FeatureSpace))

#TestFeatureSpace=["test","document","see","fuck","hello","two","one","function"]
#print (len(FeatureSpace))
#document="hello this is a test document to see if the feature vector function is working properly test hello"

#testfs=Fcts.getFeatureSpace(TestFeatureSpace,1)
#test=Fcts.getFeatureVector(document,testfs,True)

#print (len(testfs))
#for i in range(0,len(test)):
#    print (test[i])

Xvector=[]
Yvector=[]
IN=open("train.csv","r")
IN.readline()
counter=0
CommentVector=[]
for line in IN:
    if(not line):
        break
    counter += 1
    if(counter > 1500):
        break

    line_list=list(line)
    Yvector.append(int(line_list[0]))
    for i in range(2,len(line)):
        if(line[i]==","):
            if(i==2):
                timestamp=None
            else:
                timestamp=line[2:(i-1)]
            Comment="".join(line[(i+1):len(line)])
            break
    CommentVector.append(Comment)
    iFV=Fcts.getFeatureVector(Comment,FeatureSpace,True)
    Xvector.append(iFV)

XvectorT=[]
YvectorT=[]
INT=open("test_readnormal.txt","r")
INT.readline()
counterT=0
for line in INT:
    if(not line):
        break
    counterT += 1
    if(counterT > 1500):
        break

    line_list=list(line)
    YvectorT.append(int(line_list[0]))
    for i in range(2,len(line)):
        if(line[i]==","):
            if(i==2):
                timestamp=None
            else:
                timestamp=line[2:(i-1)]
            Comment="".join(line[(i+1):len(line)])
            break
    CommentVector.append(Comment)
    iFV=Fcts.getFeatureVector(Comment,FeatureSpace,True)
    XvectorT.append(iFV)

insult="your such a dickhead..."
FeatureVector=Fcts.getFeatureVector(insult,FeatureSpace,True)


#clf = svm.LinearSVC()
clf = svm.SVC(probability=True)
clf.fit(Xvector,Yvector)


print (clf.score(Xvector,Yvector))
pred=clf.predict_proba(FeatureVector)

print (pred)
probI=[]
for i in range(0,len(XvectorT)):
    probI.append(clf.predict_proba(XvectorT[i])[0][1])
    #print (probI[0][1])
    #print (clf.predict_proba(Xvector[i]),probI,Yvector[i])
    #print (clf.predict_proba(Xvector[i]),Yvector[i])


xp=[]
yp=[]
totalinsult=0
for p in range(0,100):
    xc=0
    yc=0
    for j in range(0,len(probI)):
        if(YvectorT[j]==1 and p==0):
            totalinsult += 1

        if(probI[j]*100 >= p):
            if(YvectorT[j]==1):
                yc += 1
            else:
                xc += 1
    xp.append(xc/float(len(probI)-totalinsult))
    yp.append(yc/float(totalinsult))
    
plt.plot(xp,yp)
plt.xlim([0.0,1.0])
plt.xlabel("False Positive Rate")
plt.ylim([0.0,1.0])
plt.ylabel("True Positive Rate")
plt.savefig("ROC_test.png")

#area=0
#for p in range(0,100):
#    print (xp[p],yp[p])
  

#print (len(FeatureVector))
#print (len(Yvector))
#print (len(Xvector))
#print (len(Xvector[0]))

#for i in range(0,len(FeatureVector)):
#    print (FeatureVector[i])


