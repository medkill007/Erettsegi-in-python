#9:53
def mpbe(o,p,mp):
	x=3600*o+60*p+mp
	return x
file = open('hivas.txt','r')
adat=[x.rstrip().split() for x in file]
file.close()

print('3.feladat:')
for i in range(int(adat[0][0]),int(adat[len(adat)-1][0])+1):
	x=0
	for o in range(0,len(adat)):
		if int(adat[o][0])==i:
			x+=1
	if x!=0:
		print(i,'ora',x,'hivas')
	else:
		print(i,'ora')
#10:17
print('\n4.feladat:')
max4=0
y=0
for i in range(0,len(adat)):
	x=mpbe(int(adat[i][3]),int(adat[i][4]),int(adat[i][5]))-mpbe(int(adat[i][0]),int(adat[i][1]),int(adat[i][2]))
	if max4<x:
		max4=x
		y=i
print('A leghosszabb ideig vonalban levo hivo %i. sorban szerepel, a hivas hossza: %i masodperc.'%(y+1,max4))
#10:33
print('\n5.feladat:')
x=0
y=0
felh=input('Adjon meg egy idopontot! (ora perc masodperc)').split()
#10:42-10:47
felh=mpbe(int(felh[0]),int(felh[1]),int(felh[2]))
for i in range(0,len(adat)):
	x=mpbe(int(adat[i][0]),int(adat[i][1]),int(adat[i][2]))
	if felh<=x:
		break
for o in range(0,len(adat)):
	x=mpbe(int(adat[o][3]),int(adat[o][4]),int(adat[o][5]))
	if felh<=x:
		break
o=o+1
print('A varakozok szama: %i a beszelo a %i. hivo.'%(i-o,o))
#11:08
for i in range(0,len(adat)):
	if int(adat[i][0])==12:
		break

x=mpbe(int(adat[i-1][3]),int(adat[i-1][4]),int(adat[i-1][5]))-mpbe(int(adat[i-1][0]),int(adat[i-1][1]),int(adat[i-1][2]))
print('Az utolso telefonalo adatai a(z) %i. sorban vannak, %i masodpercig tart.'%(i-1,x))
#11:38