# 1.feladat
file1 = open ('foglaltsag.txt', 'r')
file1_list = list(file1.read())
for i in range(len(file1_list)):
	if i<len(file1_list):
		if file1_list[i] == "\n":
			del file1_list[i]
file1.close()

file2 = open ('kategoria.txt', 'r')
file2_list = list(file2.read())
for i in range(len(file2_list)):
	if i<len(file2_list):
		if file2_list[i] == "\n":
			del file2_list[i]
file2.close()

# 2.feladat
print('2.feladat')
print('Válassz a nézőtérről egy helyet sor és szék szám alapján szóközzel elválsztva.')
sor,hely=input().split(' ')
sor,hely=[int(sor),int(hely)]
if (sor<=15) and (hely<=20):
	sor-=1
	szek=(sor*20+hely)-1
	if file1_list[szek] == 'x':
		print('Ez a szék sajnos már foglalt.')
	else:
		print('Ez még szerencsére szabad.')
else:
	print('Ilyen hely nincs.')

# 3.feladat
print('3.feladat')
foglalt=0
for i in range(len(file1_list)):
	if file1_list[i] == 'x':
		foglalt+=1
foglalttt=(foglalt/len(file1_list))*100
print('Az előadásra eddig %a jegyet adtak el, ez a nézőtér %.0f%%.' %(foglalt,foglalttt))

# 4.feladat
print('4.feladat')
jegy1=jegy2=jegy3=jegy4=jegy5=0
for i in range(len(file1_list)):
	if file1_list[i] == 'x':
		if file2_list[i] == '1':
			jegy1+=1
		elif file2_list[i] == '2':
			jegy2+=1
		elif file2_list[i] == '3':
			jegy3+=1
		elif file2_list[i] == '4':
			jegy4+=1
		elif file2_list[i] == '5':
			jegy5+=1
maxjegy=max(jegy1,jegy2,jegy3,jegy4,jegy5)
if jegy1 == maxjegy:
	print('A legtöbb jegyet a(z) 1. árkategóriában értékesítették.')
elif jegy2 == maxjegy:
	print('A legtöbb jegyet a(z) 2. árkategóriában értékesítették.')
elif jegy3 == maxjegy:
	print('A legtöbb jegyet a(z) 3. árkategóriában értékesítették.')
elif jegy4 == maxjegy:
	print('A legtöbb jegyet a(z) 4. árkategóriában értékesítették.')
elif jegy5 == maxjegy:
	print('A legtöbb jegyet a(z) 5. árkategóriában értékesítették.')

# 5.feladat
print('5.feladat')
fulljegy=(jegy1*5000)+(jegy2*4000)+(jegy3*3000)+(jegy4*2000)+(jegy5*1500)
print('A színház bevétele a pillanatnyilag eladott jegyek alapján %a Ft lenne.' %(fulljegy))

# 6.feladat
print('6.feladat')
egyedul=0
for i in range(len(file1_list)):
	if file1_list[i]=='x':
		if file1_list[i+1]=='o':
			if file1_list[i+2]=='x':
				egyedul+=1
print('Ilyen „egyedülálló” üres hely %a van a nézőtéren' %egyedul)

# 7.feladat
file = open("szabad.txt", "w")
for i in range(len(file1_list)):
	if (i%20==0) and (i!=0):
		file.write('\n')
	if file1_list[i]=='x':
		file.write(file1_list[i])
	else:
		file.write(file2_list[i])
print('7.feladat\nszabad.txt létrehozva')
file.close()