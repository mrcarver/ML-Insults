import unicodedata
import unidecode
import string
import numpy as np

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
		for i in xrange(2,len(line_list)):
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

#Not currently used -- not working.
def Unicode_to_ASCII(in_string):
	#table = {
	#	' ' : '\\xa',
	#	'\n' : None
	#	}
	in_string=unicode(in_string)
	out_string=in_string.encode("utf-8")
	out_string=in_string.encode('ascii',errors='backslashreplace')
	#tbl = string.maketrans('\\xa',' ')
	#out_string=string.translate(tbl)
	return out_string

def Naive_Bayes(Train,Dictionary,Class_Count):
	N_Words=len(Dictionary)
	N_Train=len(Train)
	Count=np.zeros([N_Words,3])
	for i in xrange(0,N_Train):
		Words=Train[i][7].split()
		T_Count=np.zeros([N_Words,3])
		for j in xrange(0,len(Words)):
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
