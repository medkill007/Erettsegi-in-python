#17:20
file= open("pitypang.txt","r")
adat = [x.rstrip().split()  for x in file]
file.close()

x=0
for i in range(1,len(adat)):
	y=int(adat[i][3])-int(adat[i][2])
	if y>x:
		x=y
for i in range(1,len(adat)):
	y=int(adat[i][3])-int(adat[i][2])
	if x==y:
		print(adat[i][6],"(",adat[i][2],") -",y)

össz=0
ir=open("bevetel.txt","w")
for i in range(1,len(adat)):
	if (int(adat[i][2])>=121) and (int(adat[i][2])<=243):
		y=10000
	elif int(adat[i][2])>=244:
		y=8000
	elif int(adat[i][2])<=120:
		y=9000
	n=int(adat[i][3])-int(adat[i][2])
	if adat[i][5]=="1":
		z=n*int(adat[i][1])*1100
	x=int(adat[i][1])*y*n+int(adat[i][4])*n*2000+z
	össz+=x
	ir.write(adat[i][0])
	ir.write(":")
	ir.write(str(x))
	ir.write("\n")
ir.close()
print("a szálloda teljes évi bevétele:",össz,"Ft")
#unalom 18:15 55perc