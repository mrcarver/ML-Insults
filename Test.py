import re
#import enchant 
from ROOT import gROOT, TCanvas, TF1, TH1F

#print 'Start Reading training file'

train = open("train.txt","r")

#dictionary = enchant.Dict("en_US")

#dictionary.check("Hello")

#dictionary.check("hello")


h1 = TH1F('h1','h1',100,0,1000)
h1.SetLineColor(1)
h1.SetLineWidth(2)
h2 = TH1F('h2','h2',100,0,1000)
h2.SetLineColor(2)
h2.SetLineWidth(2)

t1 = TH1F('t1','t1',25,-1,24)
t1.SetLineColor(1)
t1.SetLineWidth(2)
t2 = TH1F('t2','t2',25,-1,24)
t2.SetLineColor(2)
t2.SetLineWidth(2)

u1 = TH1F('u1','u1',1000,0,1000)
u1.SetLineColor(1)
u1.SetLineWidth(2)
u2 = TH1F('u2','u2',1000,0,1000)
u2.SetLineColor(2)
u2.SetLineWidth(2)

uw1 = TH1F('uw1','uw1',1000,0,1000)
uw1.SetLineColor(1)
uw1.SetLineWidth(2)
uw2 = TH1F('uw2','uw2',1000,0,1000)
uw2.SetLineColor(2)
uw2.SetLineWidth(2)

k1 = TH1F('k1','k1',20,0,20)
k1.SetLineColor(1)
k1.SetLineWidth(2)
k2 = TH1F('k2','k2',20,0,20)
k2.SetLineColor(2)
k2.SetLineWidth(2)

w1 = TH1F('w1','w1',20,0,20)
w1.SetLineColor(1)
w1.SetLineWidth(2)
w2 = TH1F('w2','w2',20,0,20)
w2.SetLineColor(2)
w2.SetLineWidth(2)

counter = 0


for line in train:
	counter = counter + 1
	#if counter > 3:
		#break
		
	

	#print 'new line'
	#print line
	#print '\n\n'

	hour = -1
	upperCase = 0
	upperWord = 0
	fuck = 0
	shit = 0
	words = 0
	
	for word in line.split():
		words += 1.0 
		nu = 0
		for l in word:
		   if l.isupper():
			   nu += 1
		   
		if nu == len(word):
		   upperWord += 1
			
	
	#if re.match("(.*)(F|f)(U|u)(C|c)(K|k)(.*)",line):
		#fuck += 1
		
	if re.match("(.*)(S|s)(H|h)(I|i)(T|t)(.*)",line):
		shit += 1
	
	
	for l in line:
		if l.isupper():
			upperCase += 1
	
	#print len(line)
	
	for i in range(0,len(line)):
		i = int(i),
		if re.match("(.*)(F|f)(U|u)(C|c)(K|k)(.*)",line[i[0]:i[0]+4]):
			fuck += 1

	
	if re.match('(.*)Z,""(.*)',line):
		hour = line[2:16],
		hour = int(hour[0][8:10])
	
	#######################	
	####fill histograms####
	#######################
	if (re.match("0,(.*)",line)):
	   h1.Fill(len(line)),
	   t1.Fill(hour),
	   u1.Fill(upperCase),
	   k1.Fill(fuck),
	   w1.Fill(words),
	   uw1.Fill(upperWord)
	
	
	
	if (re.match("1,(.*)",line)):
	   h2.Fill(len(line)),
	   t2.Fill(hour),
	   u2.Fill(upperCase)
	   k2.Fill(fuck),
	   w2.Fill(words),
	   uw2.Fill(upperWord)
	
	
	
	
	
		
		
#c1 = TCanvas('c1','c1',2)
#h1.DrawNormalized()
#h2.DrawNormalized("same")
#c1.SaveAs("plot.root")

c2 = TCanvas('c2','c1',2)
uw1.DrawNormalized()
uw2.DrawNormalized("same")
c2.SaveAs("plot.root")
