# 1.feladat
print('1.feladat')
from random import randint
x = randint(0,1)
if x > 5:
	print('I')
else:
	print('F')

# 2.feladat
print('2.feladat')
print('Fej vagy írás? :D')
print('I = irás')
print('F = fej')
n = input()
from random import randint
x = randint(0,10)
if x > 5:
	z = 'I'
else:
	z = 'F'
if n == z:
	print('Eltaláltad :D')
else:
	print('Majdnem majd legközelebb')

# 3.feladat
print('3.feladat')
file = open('kiserlet.txt').read()
h = [h_temp for h_temp in file.strip().split('\n')]
len_h = len(h)
print('A kisérletben %a dobás van.' %len_h)

# 4.feladat
print('4.feladat')
t = 0
y = 0
while t < len_h:
	if h[t] == 'F':
		y += 1
	t += 1
win = y/len_h*100
print('A kisérletben fejek aránya %.2f%% volt.' %win)

# 5.feladat
print('5.feladat')
def sorozat(g):
	s=f=0
	for i in range(0,len_h):
		if(g[i] == 'F'):
			f+=1
		else:
			if(f==2):
				s+=1
			f=0
	
	return s

print('A kisérletben %a történt pontosan 2 fej.' %sorozat(h))

# 6.feladat
print('6.feladat')
tag=start=f=0
for i in range(0,len_h):
	if h[i] == 'F':
		f+=1
	else:
		if f>tag:
			tag=f
			start=i-f
		f=0
if f>tag:
	tag=f
	start=i-f
print('A kisérletben leghosszabb fej sorozat %a és kezdete %a.' %(tag, start))

F='Lajos noob!:D'

