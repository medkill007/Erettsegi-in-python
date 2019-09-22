#15:00
read1=open("valaszok.txt","r")
read2=[x.strip('\n') for x in read1]
read =[x.split(' ') for x in read2]
read1.close()
print("1. feladat: Az adatok beolvasása ")

print("2. feladat: A vetélkedőn %i versenyző indult."%(len(read)-1))

azono=input("3. feladat: A versenyző azonosítója = ")
mo3=""
for i in range(1,len(read)-1):
	if read[i][0]==azono:
		mo3+=read[i][1]
		break
print(mo3)

print("4. feladat:\n%s"%str(read[0][0]))
ell4=[]
helyes4=""
ell4.append(list(read[0][0]))
ell4.append(list(mo3))
for i in range(len(ell4[0])):
	if ell4[0][i]==ell4[1][i]:
		helyes4+="+"
	else:
		helyes4+=" "
print(helyes4)

fs5=int(input("5. feladat: A feladat sorszáma = "))
#15:40--16:25
def feladat(x):
	j=ell4[0][x-1]
	jok=0
	for i in range(1,len(read)-1):
		z=list(read[i][1])
		if z[x-1]==j:
			jok+=1
	return jok
x=feladat(fs5)
print("A feladatra %i fő, a versenyzők %.2f%%-a adott helyes választ. "%(x,100*(x/(len(read)-1))))

for i in range(1,len(read)):
	z=list(read[i][1])
	y=0
	for o in range(len(ell4[0])+1):
		if z[o-1]==ell4[0][o-1]:
			if (o>=1) and (o<=5):
				y+=3
			elif (o>=6) and (o<=10):
				y+=4
			elif (o>=11) and (o<=13):
				y+=5
			elif o>=14:
				y+=6
	read[i].append(int(y))
ir=open("pontok.txt","w")
for i in range(1,len(read)-1):
	ir.write(read[i][0])
	ir.write(" ")
	ir.write(str(read[i][2]))
	ir.write("\n")
ir.close()
print("6. feladat: A versenyzők pontszámának meghatározása")

def maxi(x):
	m=0
	for i in range(1,len(read)-1):
		if (read[i][2]>m) and (read[i][2]<x):
			m=read[i][2]
	return m
x=60
print("7. feladat: A verseny legjobbjai:")
for i in range(1,4):
	pont=maxi(x)
	for o in range(1,len(read)-1):
		if read[o][2]==pont:
			print("%i. díj (%i pont): %s"%(i,pont,read[o][0]))
	x=pont
#17:45
#2 óra :(