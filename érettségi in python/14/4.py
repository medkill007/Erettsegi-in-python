print('4.feladat')
jegyek=[0,0,0,0,0]
for i in range(len(file1_list)):
	if file1_list[i] == 'x':
		j = int(file2_list[i]) - 1
		if (j >= 0 and j <= 4):
			jegyek[j]+=1

maxjegy = jegyek.index(max(jegyek)) + 1
print('A legtöbb jegyet a(z) %d. árkategóriában értékesítették.' % maxjegy)