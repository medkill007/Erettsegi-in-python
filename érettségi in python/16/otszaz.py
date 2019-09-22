#!/usr/bin/python3

import sys

# Read file
content = []
with open('penztar.txt', 'r') as f:
	content = [line for line in f.read().splitlines()]

kosar = []
hosz = 0
for i in range(len(content)):
	if (content[i] == 'F' and hosz > 0):
		kosar.append([content[i2] for i2 in range(i-hosz,i)])
		hosz = 0
	else:
		hosz +=1

# 2
print('2. feladat: ',len(kosar))
# 3
print('3. feladat: ',len(kosar[0]))
# 4
print('4. feladat: ')
sorszam = int(input('Kérem írja be a vásárlás sorszámát! '))
aruCikk = input('Kérem írjon be egy árucikk nevet! ')
db = int(input('Kérem írja be a darabszámot! '))
# 5
print('5. feladat')

def elsoF():
	for i in range(len(kosar)):
		for i2 in range(len(kosar[i])):
			if (kosar[i][i2] == aruCikk):
				return i

elso = elsoF()

def utolsoF():
	for i in range(len(kosar)-1,elso-1,-1):
		for i2 in range(len(kosar[i])):
			if (kosar[i][i2] == aruCikk):
				return i

utolso = utolsoF()
vasarlasok = 0
for i in range(elso,utolso+1):
	for i2 in range(len(kosar[i])):
		if (kosar[i][i2] == aruCikk):
			vasarlasok += 1

print('Az első vásárlás sorszáma: ',elso)
print('Az utolsó vásárlás sorszáma: ',utolso)
print(vasarlasok,' vásárlás során vettek belőle.')
# 6 
def ertek(n):
	if (n==0):
		return 0

	price = 500
	result = 0
	end = 1
	if(n>=2):
		end = 2
	for i in range(0,end):
		result += price
		price -= 50
	if (n > 2):
		result += price*(n-2)
	return result

print('6. feladat')
print(db,' darab vételekor fizetendő: ',ertek(db))
# 7
def lista(n):
	listam = kosar[n]
	i=0
	while (i < len(listam)):
		darab = 1
		i2=i+1
		while (i2 < len(listam)):
			if (listam[i2] == listam[i]):
				darab += 1
				del listam[i2]
			i2+=1
		print(darab,listam[i])
		i+=1

print('7. feladat')
lista(sorszam)
# 8
f = open('osszeg.txt','w')
for i in range(len(kosar)):
	line = str(i+1)+': '+str(ertek(len(kosar[i])))
	f.write(line+'\n')
f.close()