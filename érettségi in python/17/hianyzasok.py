# 1. feladat
dat=[]

for x in open('naplo.txt','r'):
  dat.append(x)

dat2=[]
for x in dat:
  y = x.strip("\n").split(' ')
  if(y[0]=='#'):
    dat2.append([int(y[1]),int(y[2]),[]])
  else:
    dat2[len(dat2)-1][2].append(y)

# 2. feladat
b=0
for x in dat2:
  b+=len(x[2])
print('2. feladat\nA naploban %d bejegyzes van' % (b))

# 3. feladat
X=I=0
for x in dat2:
  for y in x[2]:
    for z in y[len(y)-1]:
      if(z=='X'):
        X+=1
      elif(z=='I'):
        I+=1
print('3. feladat\nAz igazolt hianyzasok szama %d, az igazolatlanoke %d ora' % (X,I))

# 4. feladat
def hetnapja(honap, nap):
  napnev=["vasarnap","hetfo","kedd","szerda","csutortok","pentek","szombat"]
  napszam=[0,31,59,90,120,151,181,212,243,273,304,335]
  napsorszam=(napszam[honap-1]+nap) % 7
  hetnapja=napnev[napsorszam]
  return hetnapja

# 5. feladat
print('5. feladat')
h=int(input('A honap sorszama='))
n=int(input('A nap sorszama='))
print('Azon a napon %s volt.' % (hetnapja(h,n)))

# 6. feladat
print('6. feladat')
nap=input('A nap neve=')
ora=int(input('Az ora sorszama='))-1

hianyzas=0
for x in dat2:
  if(hetnapja(x[0],x[1]) == nap):
    for y in x[2]:
      if(y[len(y)-1][ora]=='X' or y[len(y)-1][ora]=='I'):
        hianyzas+=1
print('Ekkor osszesen %d ora hianyzas tortent.' % (hianyzas))

# 7. feladat
dat3=[]
for x in dat2:
  for y in x[2]:
    found=False
    for z in range(len(dat3)):
      if(dat3[z][0] == y[0] and dat3[z][1] == y[1]):
        dat3[z][2].append(y[2])
        found=True
        break
    if(found==False):
      dat3.append([y[0],y[1],[y[2]]])
for i in range(len(dat3)):
  c=0
  for i2 in range(len(dat3[i][2])):
    for i3 in dat3[i][2][i2]:
      if(i3=='X' or i3=='I'):
        c+=1
  dat3[i].append(c)
def getKey(a):
  return a[3]
dat3=sorted(dat3,key=getKey,reverse=True)
legtobb = dat3[0][3]
tanulok = []
for i in dat3:
  if(i[3] == legtobb):
    tanulok.append(i[0])
    tanulok.append(i[1])
print('7. feladat\nA legtobbet hianyzo tanulok: %s ' % (' '.join(tanulok)))  
#35:18
