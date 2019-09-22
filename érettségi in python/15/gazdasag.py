file = open ('terulet.txt', 'r')
terulet = list(file.read())
for i in range(len(terulet)):
	if i<len(terulet):
		if terulet[i]=='\n':
			del terulet[i]
print('1600m X 2000m, területe: %aha' %(len(terulet)))
l=0
for i in range(len(terulet)):
	if terulet[i]=='L':
		l+=1
print('A legelők %.2f%% foglalnak el a gazdaság területéből!'%(100*(l/len(terulet))))
l=x=0
while l==0:
	if terulet[x]=='L':
		l=x
	x+=1
x=0
while l>16:
	l-=16
	x+=1
print('Az első legelő %am-re van az északi oldalának a szélétől.'%(x*100))
m=mmax=0
for i in range(len(terulet)):
	if terulet[i]=='M':
		m+=1
	else:
		if mmax<m:
			mmax=m
		m=0
print('Kelet-nyugati irányban %a00 méter széles a legszélesebb legelő!'%mmax)
l1=l2=lmax=x=0
for i in range(len(terulet)):
	if terulet[i]=='L':
		l1+=1
		if l1==1 and i<=270:
			x=+1
			if terulet[i+16]=='L':
				x+=1
			if terulet[i+32]=='L':
				x+=1
			if terulet[i+48]=='L':
				x+=1
	else:
		if lmax<l1:
			lmax=l1
			l2=x
		x=0
		l1=0
print('A legnagyobb területű legelő %aha.'%(lmax*l2))
