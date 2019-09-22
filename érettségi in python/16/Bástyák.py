from random import randint
tabla=[['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','','']]
x=0
while x<10:
	a1=randint(0,7)
	a2=randint(0,7)
	if tabla[a1][a2]=='':
		tabla[a1][a2]='G'
	else:
		x-=1
	x+=1
for i in range(8):
	for x in range(8):
		if tabla[i][x]=='':
			tabla[i][x]='#'
print('1-2. feladat')
def Megjelenit():
	for i in range(8):
		print(''.join(tabla[i]))
Megjelenit()

x=0
while x<5:
	a1=randint(1,6)
	a2=randint(1,6)
	if tabla[a1][a2]=='#':
		tabla[a1][a2]='B'
	else:
		x-=1
	x+=1
print('3. feladat')
Megjelenit()
