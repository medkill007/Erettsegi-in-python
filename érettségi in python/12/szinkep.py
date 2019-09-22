#10:00
file=open("kep.txt","r")
adat=[x.rstrip().split(" ") for x in file]
file.close()

def f(x):
	print("%i. feladat:"%x)

f(2)
felh=input("Adj egy RGB kodot:  ").split(" ")
x=False
for i in range(len(adat)):
	if adat[i]==felh:
		x=True
		break
if x==True:
	print("Van ilyen színkod!")
else:
	print("Nincs ilyen színkod")

f(3)
z=adat[35*50+7]
x=y=0
for i in range(35*50-1,36*50-1):
	if adat[i]==z:
		x+=1
for i in range(7,2493,50):
	if adat[i]==z:
		y+=1
print("Sorban:",x,"Oszlopban:",y)

f(4)
v=z=k=0
for i in range(len(adat)):
	if (adat[i][0]=="255") and (adat[i][1]=="0") and (adat[i][2]=="0"):
		v+=1
	if (adat[i][1]=="255") and (adat[i][0]=="0") and (adat[i][2]=="0"):
		z+=1
	if (adat[i][2]=="255") and (adat[i][1]=="0") and (adat[i][0]=="0"):
		k+=1
x=max(v,z,k)
if v==x:
	print("Vörös színből van a legtöbb a képen.")
elif z==x:
	print("Zöld színből van a legtöbb a képen.")
else:
	print("Kék színből van a legtöbb a képen.")
ir=open("keretes.txt","w")
for i in range(0,3*50+18):
	ir.write("0 0 0\n")
for i in range(50):
	for i2 in range(3):
		ir.write("0 0 0\n")
	for o in range(50):
		ir.write(adat[i*o][0])
		ir.write(" ")
		ir.write(adat[i*o][1])
		ir.write(" ")
		ir.write(adat[i*o][2])
		ir.write("\n")
	for i3 in range(3):
		ir.write("0 0 0\n")
for i in range(0,3*50+18):
	ir.write("0 0 0\n")
ir.close()
x=y=z=0
for i in range(len(adat)):
	if (adat[i][0]=="255") and (adat[i][1]=="255") and (adat[i][2]=="0"):
		z+=1
		y=i
for i in range(len(adat)):
	if (adat[i][0]=="255") and (adat[i][1]=="255") and (adat[i][2]=="0"):
		x=i
		break
def minusz50(x):
	y=0
	while True:
		x-=50
		y+=1
		if x-50<0:
			break
	return y
print("Kezd: %i, %i"%(minusz50(x),x%50))
print("Vége: %i, %i"%(minusz50(y),y%50))
print("Képpontok száma:",z)
#11:30