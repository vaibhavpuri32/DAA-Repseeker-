from ukkonen import SuffixTree
from modules import CheckSubString
from test import cal_freq


D=[]
l=[]
r=[]
def RepSeeker(S,L,Fm):
	f=cal_freq(S,L)
	if (f[0]>=Fm):
		l.append(0)
	n=len(S)
	for i in range(1,n-L):
		if(f[i]>=Fm):
			if(f[i]!=f[i-1]):
				l.append(i)
			if(f[i]!=f[i+1]):
				r.append(i+L-1)

	# print("hello!!")
	# print(l)
	# print(r)
	#print(len(l))
	for i in range(0,len(l)):
		D.append((l[i],r[i]))
	sum=len(D)
	print("Starting Check")
	Check(f,L,S,D,sum)
	print("Starting Extend")
	Extend(f,L,S,D,sum,Fm)
	print("Starting Classify")
	Classify(f,L,S,D,sum,Fm)
	return max(map(lambda x:len(x), D))


def Check(f,L,S,D,sum):
	print("started check",sum)
	tree = SuffixTree(S)
	tree.build_suffix_tree()
	for i in range(0,sum):
		print(">>>>>check",i)
		P = []
		strD=S[D[i][0]:D[i][1]+1]
		a = CheckSubString(tree, strD, findall=True)

		fD=len(a.check())
		if(f[l[i]])!=fD:
			print("HEYY")
			for j in range(0,(D[i][1]-D[i][0])-L):
				print("$$",j)
				tree2 = SuffixTree(S)
				tree2.build_suffix_tree()
				n=len(S)
				for z in range(0,n-L+1):
					print("!!!",z)
					string=S[l[i]+z:l[i]+z+L+1]
					print(string)
					b = CheckSubString(tree2, string, findall=True)
					P.append(b.check())
					print(b.check())
					
			for k in range(0,(D[i][1]-D[i][0]+1)-L):
				print("??",k)
				for m in range(0,f[l[i]]):
					print("@@",m)
					if(P[k+1][m]!=P[k][m]+1):
						l.append(l[i]+k+1)
						r.append(l[i]+k+L-1)
						sum=sum+1

def merop(S,D,i):
	l1=l[i]
	r1=r[i]
	l2=l[i+1]
	r2=r[i+1]
	len1=r1-l1+1
	len2=r2-l2+1
	print("STRING A:",D[i]," ",S[D[i][0]:D[i][1]+1])
	print("STRING B:",D[i+1]," ",S[D[i][0]:D[i][1]+1])
	if((r2-l1+1)<=(len1+len2)):
		strC=S[l2:r1+1]
		print(strC)
		lenC=len(strC)
		perc_overlap=lenC/(r2-l1+1)*100
		return perc_overlap
	else:
		return 0


def fre(S,D,i,Fm):
	l1=l[i]
	r1=r[i]
	l2=l[i+1]
	r2=r[i+1]
	len1=r1-l1+1
	len2=r2-l2+1
	strAuB=S[l1:r2+1]
	tree = SuffixTree(S)
	tree.build_suffix_tree()
	a = CheckSubString(tree, strAuB, findall=True)
	fD=len(a.check())
	if(fD>=Fm):
		return 1
	else:
		return 0


	
def Extend(f,L,S,D,sum,Fm):
	#print("VALUE OF SUM IN EXTEND:",sum)
	i=0
	while(i<sum-1):
		if(merop(S,D,i)>=25 and fre(S,D,i,Fm)):
			D[i]=(l[i],r[i+1])
			i=i-1
			sum-=1
		i+=1

def Classify(f,L,S,D,sum,Fm):
	classes=[]
	for i in range(0,sum):
		classes.append(S[D[i][0]:D[i][1]+1])
		print(">>>>>>>>>>>>>>")
		print(classes[i])
		# print("<<<<<<<<<<<<<<")


with open('data.txt','r') as f:
	mainstring=f.read()


	
print(RepSeeker(mainstring,20,3))