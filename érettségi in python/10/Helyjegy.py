olvas1 = open("eladott.txt","r")
olvas2 = [line.strip('\n') for line in olvas1]
olvas3 = [line.split(' ') for line in olvas2]
olvas1.close()
def fa(x):
	print("%a.feladat:"%x)
fa(2)
veg=[]
arak=[]
print("A legutolsó jegyvásárló %a ülésének a sorszáma és %akm az általa beutazott távolság"%(int(olvas3[len(olvas3)-1][0]),int(olvas3[len(olvas3)-1][2])-int(olvas3[len(olvas3)-1][1])))
fa(3)
for i in range(len(olvas3)):
	if (int(olvas3[i][1])==0 and int(olvas3[i][2])==int(olvas3[0][1])):
		veg.append(str(i+1))
print("Akik  utazták  végig  a  teljes  utat:"," ".join(veg))
fa(4)
for i in range(1,len(olvas3)):
	arak.append(int(olvas3[i][2])-int(olvas3[i][1]))
print("Cég teljes bevétele: %aFt"%(sum(arak)*int(olvas3[0][2])))
fa(5)
def allomas():
	x=int(olvas3[0][1])-1
	while (x!=1):
		for i in range(len(olvas3)):
			if (x==int(olvas3[i][2])):
				return x
		x-=1
felall=leáll=0
for i in range(len(olvas3)):
	if (allomas()==int(olvas3[i][1])):
		felall+=1
	elif (allomas()==int(olvas3[i][2])):
		leáll+=1
print("A busz végállomást megelőző utolsó megállásánál %a fő szállt fel és %a fő szállt le."%(felall,leáll))
fa(6)
allomasok=0
def allomase(y):
	for i in range(1,len(olvas3)):
		if y==int(olvas3[i][1]) or y==int(olvas3[i][2]):
			return True
	return False
for i in range(1,int(olvas3[0][1])):
	if allomase(i)==True:
		allomasok+=1
print("A busz a kiinduló állomás és a célállomás között %a db helyen állt meg."%allomasok)
fa(7)
k=False
while k==False:
	fszam=int(input("Adj egy pontot a kiindulási állomástól mért távolságot.\n"))
	if fszam<int(olvas3[0][1]) and fszam>0:
		k=True
kihol=[]
for i in range(1,49):
	g=False
	for x in range(1,len(olvas3)):
		if i==int(olvas3[x][0]) and int(olvas3[x][1])<=fszam and int(olvas3[x][2])>fszam:
			g=True
			kihol.append("%a. utas"%x)
	if g==False:
		kihol.append("üres")
ir = open("kihol.txt","w")
for i in range(48):
	ir.write("%a. ülés: %s \n"%(i+1,kihol[i]))
ir.close()