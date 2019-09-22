#18:40
file=open("jarmu.txt","r")
adat=[x.rstrip().split() for x in file]
file.close()
for i in range(len(adat)):
	adat[i][0]=int(adat[i][0])
	adat[i][1]=int(adat[i][1])
	adat[i][2]=int(adat[i][2])
def f(x):
	print('%i. feladat:'%x)
f(2)
print(adat[len(adat)-1][0]-adat[0][0])
f(3)
x=adat[0][0]
for i in range(len(adat)):
	if x==adat[i][0]:
		print('-',x,'óra',adat[i][3])
		x+=1
f(4)
#-3 perc
y=[0,0,0]
for i in range(len(adat)):
	x=list(adat[i][3])
	if x[0]=='B':
		y[0]+=1
	if x[0]=='K':
		y[1]+=1
	if x[0]=='M':
		y[2]+=1
print(y[0],'db autóbusz',y[1],'db kamion',y[2],'db motor ment jármű haladt el az ellenőrzőpont előtt.')

f(5)
y=0
y2=0
for i in range(1,len(adat)):
	x1=adat[i-1][0]*3600+adat[i-1][1]*60+adat[i-1][2]
	x2=adat[i][0]*3600+adat[i][1]*60+adat[i][2]
	x=x2-x1
	if x>y:
		y=x
		y2=i
print('%i:%i:%i - %i:%i:%i'%(adat[y2-1][0],adat[y2-1][1],adat[y2-1][2],adat[y2][0],adat[y2][1],adat[y2][2],))

f(6)
y=list(input('Adj egy rendszámot (*-al lehet helyetesíten):  '))
y2=False
print('Gyanusítot(tak):')
for i in range(len(adat)):
	x=list(adat[i][3])
	x1=0
	for o in range(len(y)):
		if (x[o]==y[o]) or (y[o]=='*'):
			x1+=1
	if x1==7:
		print('-',adat[i][3])
		y2=True
if y2==False:
	print('Nincs találat!')
#19:37
f(7)
ir=open("vizsgalt.txt","w")
y=adat[0][0]*60+adat[0][1]
for i in range(len(adat)):
	x=adat[i][0]*60+adat[i][1]
	if y+6==x:
		y+=6
		if y==x:
			ir.write(str(adat[i][0]))
			ir.write(':')
			ir.write(str(adat[i][1]))
			ir.write(':')
			ir.write(str(adat[i][2]))
			ir.write('  ')
			ir.write(adat[i][3])
			ir.write('\n')
			y+=5	
	if y==x:
		ir.write(str(adat[i][0]))
		ir.write(':')
		ir.write(str(adat[i][1]))
		ir.write(':')
		ir.write(str(adat[i][2]))
		ir.write('  ')
		ir.write(adat[i][3])
		ir.write('\n')
		y+=5
ir.close()
#20:05