#start 10:45
read= open("tavok.txt","r")
read2= [i.strip("\n") for i in read]
read3= [i.split(" ") for i in read2]
read.close()
#----------------------
x=7
for i in range(len(read3)):
	if x>int(read3[i][0]):
		x=int(read3[i][0])
q=False
y=0
while q!=True and y<len(read3):
	if int(read3[y][0])==x and read3[y][1]=="1":
		q=True
		print("2.feladat:  %ikm"%int(read3[y][2]))
	y+=1
#--------------------------
x=1
for i in range(len(read3)):
	if x<int(read3[i][0]):
		x=int(read3[i][0])
y=1
for i in range(len(read3)):
	if y<int(read3[i][1]) and x==int(read3[i][0]):
		y=int(read3[i][1])
q=False
z=0
while q!=True and z<len(read3):
	if int(read3[z][0])==x and int(read3[z][1])==y:
		q=True
		print("3.feladat:  %ikm"%int(read3[z][2]))
	z+=1
#-----------------------
w=[]
for i in range(1,7):
	q=False
	z=0
	while q!=True and z<len(read3):
		if int(read3[z][0])==i:
			q=True
		z+=1
	if q==False:
		w.append(str(i))
print("4.feladat: Nem ment ezeken a napokan: %s"%", ".join(w))
#----------------------
w=[[],[],[],[],[],[],[]]
for i in range(len(read3)):
	w[int(read3[i][0])-1].append(int(read3[i][2]))
x=1
for i in range(len(w)):
	if x<len(w[i]):
		x=len(w[i])
q=False
z=0
while q!=True and z<len(w):
	if len(w[z])==x:
		q=True
	z+=1
print("5.feladat: A héten a %i. napján volt a legtöbb fuvar"%z)
#----------------------
#11:50
#12:50
#-----------------------
print("6.feladat:")
for i in range(len(w)):
	print("%i. nap: %i km"%(i+1,sum(w[i])))
#----------------------
print("\n7.feladat")
def er(x):
	print("A távolság értéke: %iFt"%x)
user=int(input("Adj meg  egy  tetszőleges  távolságot:    "))
def arak(x):
	if x==1 or x==2:
		er(500)
	elif x>=3 and x<=5:
		er(700)
	elif x>=6 and x<=10:
		er(900)
	elif x>=11 and x<=20:
		er(1400)
	elif x>=21 and x<=30:
		er(2000)
	else:
		print("Hibás érték!!")
arak(user)
#----------------------
adat=[]
def ar(x):
	if x==1 or x==2:
		return 500
	elif x>=3 and x<=5:
		return 700
	elif x>=6 and x<=10:
		return 900
	elif x>=11 and x<=20:
		return 1400
	elif x>=21 and x<=30:
		return 2000

for i in range(len(w)):
	for o in range(len(w[i])):
		for x in range(len(read3)):
			if int(read3[x][0])==i+1 and int(read3[x][1])==o+1:
				adat.append(["%i.nap"%(i+1),"%i. út:"%(o+1),"%i Ft"%ar(int(read3[x][2]))])
ir=open("dijazas.txt","w")
for i in range(len(adat)):
	ir.write(" ".join(adat[i]))
	ir.write("\n")
ir.close()
#----------------------
osszeg=[]
for x in range(len(read3)):
	osszeg.append(ar(int(read3[x][2])))
print("9.feladat: Összes bevétel: %iFt"%sum(osszeg))
#14:10