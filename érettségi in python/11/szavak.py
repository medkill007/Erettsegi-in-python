y=list(input("1. feladat Adjon meg egy szót:  "))
x=False
for i in range(len(y)):
	if y[i]=="a" or y[i]=="e" or y[i]=="i" or y[i]=="o" or y[i]=="u":
		x=True
if x==True:
	print("Van benne magánhangzó.")
else:
	print("Nincs benne magánhangzó.")
#2.feladat
read1=open("szoveg.txt","r")
read2=[x.strip("\n") for x in read1]
read3=[list(x) for x in read2]
read1.close()
x=0
y=[]
for i in range(len(read3)):
	if len(read3[i])>x:
		x=len(read3[i])
for i in range(len(read3)):
	if len(read3[i])==x:
		y.append(read2[i])
print("2.feladat  Leghosszabb szavak %idb karakteres és %idb található pl: %s"%(len(list(y[0])),len(y),y[0]))
#3.feladat
x=0
for i in range(len(read3)):
	x1=x2=0
	for o in range(len(read3[i])):
		if read3[i][o]=="a" or read3[i][o]=="e" or read3[i][o]=="i" or read3[i][o]=="o" or read3[i][o]=="u":
			x1+=1
		else:
			x2+=1
	if x1>x2:
		x+=1
print("3.feladat %i/%i : %.2f%%"%(x,len(read3),(x/len(read3)*100)))
#4.feladat
kar5=[]
for i in range(len(read3)):
	if len(read3[i])==5:
		kar5.append(read3[i])
x=list(input("4.feladat  Adjon egy 3 karakteres szórészletet!  "))
szo=[]
if len(x)!=3:
	print("\nEz nem 3 karakter")
for i in range(len(read3)):
	for o in range(len(read3[i])-2):
		if read3[i][o]==x[0] and read3[i][o+1]==x[1] and read3[i][o+2]==x[2] and len(read3[i])==5:
			szo.append(read2[i])
print(" ".join(szo))
#5.feladat
