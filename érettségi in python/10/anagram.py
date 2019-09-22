def f(x):
	print("%s. feladat."%x)
f(1)
word=list(input("Adj meg egy szöveget:   "))
word.sort()
words=[]
for i in range(len(word)):
	if word[i-1]!=word[i] and word[i]!=' ':
		words.append(word[i])
print(words)
#2.feladat
read1=open("szotar.txt","r")
read=[x.strip('\n') for x in read1]
read1.close()
#3.feladat
read3=[list(x) for x in read]
for i in range(len(read3)):
	read3[i].sort()
ir=open('abc.txt','w')
for i in range(len(read3)):
	ir.write("".join(read3[i]))
	ir.write("\n")
ir.close()
f(4)
szo41,szo42=list(input("Adj meg egy szót:   ")),list(input("És egy másikat is:  "))
szo41.sort()
szo42.sort()
if szo41==szo42:
	print("Anagramma!")
else:
	print("Nem anagramma!")
f(5)
szo5=list(input("Adj egy szót és kikeresem az állományból!:   "))
szo5.sort()
talalt5=[]
for i in range(len(read3)):
	if read3[i]==szo5:
		talalt5.append(i)
if len(talalt5)!=0:
	print("Talált a szótárban anagramma:")
	for i in range(len(talalt5)):
		print(read[talalt5[i]])
else:
	print("Nincs  a  szótárban anagramma!")
f(6)
hossza=0
szoh=[]
for i in range(len(read3)):
	if len(read3[i])>hossza:
		hossza=len(read3[i])
for i in range(len(read3)):
	if len(read3[i])==hossza:
		szoh.append(i)
for i in range(1,len(szoh)):
	if read3[szoh[i-1]]==read3[szoh[i]]:
		print(read[szoh[i-1]])
		print(read[szoh[i]])
	elif i<len(szoh)-1:
		if read3[szoh[i-1]]==read3[szoh[i+1]]:
			print(read[szoh[i-1]])
			print(read[szoh[i+1]])
#7.feladat
rend=[[],[],[],[],[],[],[]]
rend2=[[],[],[],[],[],[],[]]
for i in range(len(read)):
	rend[len(read3[i])-4].append(read[i])
	rend2[len(read3[i])-4].append(read3[i])
rir=open('szotar2.txt','w')
for i in range(len(rend2)):
	for x in range(1,len(rend2[i])-1):
		rir.write(rend[i][x])
		rir.write(" ")
		if rend2[i][x]!=rend2[i][x+1]:
			rir.write("\n")
rir.close()