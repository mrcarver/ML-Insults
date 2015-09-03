## Insult Detection Kaggle Competition!
import Fcts
import numpy as np

Dictionary=[]

Train_Set=Fcts.Read_Data("train.csv")
N_Train=len(Train_Set)
Word_Count=[]
Insult_Count=0
for i in xrange(0,N_Train):
	Words=Train_Set[i][7].split()
	for j in xrange(0,len(Words)):
		k=0
		Word_Check=Words[j].strip('"')
		Word_Check=Word_Check.strip('.')
		Word_Check=Word_Check.lower()
		if(Word_Check not in Dictionary):
			Dictionary.append(Word_Check)
	if(Train_Set[i][0]==1):
		Insult_Count=Insult_Count+1

Word_Count=np.zeros([len(Train_Set),len(Dictionary)])
NB_Prob=Fcts.Naive_Bayes(Train_Set,Dictionary,Insult_Count)
Num_Right=0
False_Positive=0
for i in xrange(0,N_Train):
#for i in xrange(0,1):
	Words=Train_Set[i][7].split()
	Prob_Sum=0.0
	for j in xrange(0,len(Words)):
		Word_Check=Words[j].strip('"')
		Word_Check=Word_Check.strip('.')
		Word_Check=Word_Check.lower()
		Word_Index=Dictionary.index(Word_Check)
		Ind_Prob=NB_Prob[1,Word_Index]*(Insult_Count/float(N_Train))/(NB_Prob[1,Word_Index]*(Insult_Count/float(N_Train))+NB_Prob[2,Word_Index]*(1-Insult_Count/float(N_Train)))
		Prob_Sum=Prob_Sum+(np.log(1-Ind_Prob)-np.log(Ind_Prob))
	if(Prob_Sum>40.0):
		Insult_Prob=0.0
	elif(np.isinf(Prob_Sum)):
		Insult_Prob=0.0
	elif(np.isneginf(Prob_Sum)):
		Insult_Prob=1.0
	else:
		Insult_Prob=1/(1+np.exp(Prob_Sum))
	if(round(Train_Set[i][0])==Insult_Prob):
		Num_Right=Num_Right+1
	if((Train_Set[i][0]>=0.5) and (Insult_Prob==0)):
		False_Positive=False_Positive+1

print Num_Right/float(N_Train)
print False_Positive/float(N_Train)
