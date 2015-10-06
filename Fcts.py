#import unicodedata
#import unidecode
import string
import numpy as np
import matplotlib.pyplot as plt

def Read_Data(filename):
        IN=open(filename,"r")
        IN.readline()
        Data_Set=[]
        while True:
                line=IN.readline()
                if(not line):
                        break
                line_list=list(line)
                Flag=int(line_list[0])
                for i in range(2,len(line_list)):
                        if(line_list[i]==","):
                                if(i==2):
                                        timestamp=None
                                else:
                                        timestamp=line_list[2:(i-1)]
                                Comment="".join(line_list[(i+1):len(line_list)])
                                break
                if(timestamp):
                        Year="".join(timestamp[0:4])
                        Month="".join(timestamp[4:6])
                        Day="".join(timestamp[6:8])
                        Hour="".join(timestamp[8:10])
                        Minute="".join(timestamp[10:12])
                        Second="".join(timestamp[12:14])
                else:
                        Year="N/A"
                
                Data_Row=[Flag,Year,Month,Day,Hour,Minute,Second,Comment]
                Data_Set.append(Data_Row)
        return Data_Set
'''
#Not currently used -- not working.
def Unicode_to_ASCII(in_string):
        #table = {
        #       ' ' : '\\xa',
        #       '\n' : None
        #       }
        in_string=unicode(in_string)
        out_string=in_string.encode("utf-8")
        out_string=in_string.encode('ascii',errors='backslashreplace')
        #tbl = string.maketrans('\\xa',' ')
        #out_string=string.translate(tbl)
        return out_string
'''
def Naive_Bayes(Train,Dictionary,Class_Count):
        N_Words=len(Dictionary)
        N_Train=len(Train)
        Count=np.zeros([N_Words,3])
        for i in range(0,N_Train):
                Words=Train[i][7].split()
                T_Count=np.zeros([N_Words,3])
                for j in range(0,len(Words)):
                        Word_Check=Words[j].strip('"')
                        Word_Check=Word_Check.strip('.')
                        Word_Check=Word_Check.lower()
                        if(Word_Check in Dictionary):
                                Dict_Index=Dictionary.index(Word_Check)
                                T_Count[Dict_Index,0]=1
                                if(Train[i][0]==1):
                                        T_Count[Dict_Index,1]=1
                                else:
                                        T_Count[Dict_Index,2]=1
                Count=Count+T_Count

        Prob=np.matrix([Count[:,0]/N_Train,Count[:,1]/Class_Count,Count[:,2]/(N_Train-Class_Count)])
        return Prob

def ROC(Train,Prob,Save,N_Insult):
        N_Train=len(Train)
        Bin_Width=0.01
        Bins=np.arange(start=0.0,stop=1.0+Bin_Width,step=Bin_Width)
        N_Bins=len(Bins)
        False_Positives=np.empty([N_Bins])
        True_Positives=np.empty([N_Bins])
        for i in range(0,N_Bins):
                TP_Count=0
                FP_Count=0
                for j in range(0,N_Train):
                        if(Prob[j]>=Bins[i]):
                                if(Train[j][0]==1):
                                        TP_Count=TP_Count+1
                                else:
                                        FP_Count=FP_Count+1
                True_Positives[i]=TP_Count/float(N_Insult)
                False_Positives[i]=FP_Count/float(FP_Count+N_Train-N_Insult)
        plt.plot(False_Positives,True_Positives)
        plt.xlim([0.0,1.0])
        plt.xlabel("False Positive Rate")
        plt.ylim([0.0,1.0])
        plt.ylabel("True Positive Rate")
        if(Save):
                plt.savefig("ROC.png")
        else:
                plt.show()


def getFeatureSpace(filename,minNumber):
        IN=open(filename,"r")
        Data_Set=[]
        FeatureSpace=[]
        ReducedFeatureSpace=[]
        #Stop_Words=['and','or','is','on','the','at','that']
        Stop_Words=['fffff']
        counter=0
        for line in IN:
                if(not line):
                        break
                counter += 1
                if(counter < 500):
                        continue
                
                if(counter > 1000):
                        break
                for i in range(2,len(line)):
                        if(line[i]==","):
                                if(i==2):
                                        timestamp=None
                                else:
                                        timestamp=line[2:(i-1)]
                                Comment="".join(line[(i+1):len(line)])
                                break
                
                Words=Comment.split()
                for i in range(0,len(Words)):
                        Word_Check=Words[i].strip('"')
                        Word_Check=Word_Check.strip('.')
                        Word_Check=Word_Check.lower()
                        if(Word_Check not in Data_Set and Word_Check not in Stop_Words):
                                Data_Set.append(Word_Check)
                                FeatureSpace.append(0)

                        if(Word_Check in Data_Set):
                                FeatureSpace[Data_Set.index(Word_Check)] += 1

        for i in range(0,len(FeatureSpace)):
                if(FeatureSpace[i] >= minNumber):
                        ReducedFeatureSpace.append(Data_Set[i])
        
        return ReducedFeatureSpace

def getFeatureVector(Document,FeatureSpace,UnitSpace):
        FeatureVector=[0]*len(FeatureSpace)
        Words=Document.split()
        for i in range(0,len(Words)):
                Word_Check=Words[i].strip('"')
                Word_Check=Word_Check.strip('.')
                Word_Check=Word_Check.lower()
                if(Word_Check in FeatureSpace):
                        if(UnitSpace and FeatureVector[FeatureSpace.index(Word_Check)] == 0):
                                FeatureVector[FeatureSpace.index(Word_Check)] += 1
                        elif(not UnitSpace):
                                FeatureVector[FeatureSpace.index(Word_Check)] += 1

        return FeatureVector


def getLineValue(x,y):
        out = -1
        if(x < 0 and y > -1):
                out = 10 - y
        elif(x > -1 and y < 0):
                out = 10 - x
        else:
                out = -1

        return out




        
